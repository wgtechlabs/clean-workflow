"""Import published stable releases; run from the Clean Workflow repository root."""
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

SOURCES = {'clean-coding': 'clean-coding', 'clean-code-review': 'clean-code-review'}


def latest_release(pages):
    stable = [r for page in pages for r in page if not r['draft'] and not r['prerelease']]
    return max(stable, key=lambda r: r['published_at'], default=None)


def fetch_release(repo, temporary):
    pages = json.loads(subprocess.check_output(
        ['gh', 'api', f'repos/wgtechlabs/{repo}/releases', '--paginate', '--slurp'], text=True))
    release = latest_release(pages)
    if release is None:
        return None
    checkout = temporary / repo
    subprocess.run(['git', 'clone', '--quiet', '--depth', '1', '--branch', release['tag_name'],
                    '--', f'https://github.com/wgtechlabs/{repo}.git', str(checkout)], check=True)
    commit = subprocess.check_output(['git', '-C', str(checkout), 'rev-parse', 'HEAD'], text=True).strip()
    tag_commit = subprocess.check_output(
        ['git', '-C', str(checkout), 'rev-parse', f"refs/tags/{release['tag_name']}^{{commit}}"],
        text=True).strip()
    if commit != tag_commit:
        raise ValueError(f'{repo}: checkout does not match the release tag')
    return {'tag': release['tag_name'], 'release_id': release['id'], 'commit': commit}, checkout


def sync(root, fetch=fetch_release):
    lock = root / 'skills/upstream-releases.json'
    previous = json.loads(lock.read_text()) if lock.exists() else {}
    updated = dict(previous)
    pending = []
    with tempfile.TemporaryDirectory() as directory:
        for repo, skill in SOURCES.items():
            result = fetch(repo, Path(directory))
            if result is None:
                print(f'{repo}: no stable release; keeping bundled skill')
                continue
            release, checkout = result
            if previous.get(repo) == release:
                continue
            old = previous.get(repo)
            if old and old['tag'] == release['tag'] and old['commit'] != release['commit']:
                raise ValueError(f'{repo}: published tag moved; investigate before importing')
            source = checkout / 'skills' / skill
            if not (source / 'SKILL.md').is_file():
                raise ValueError(f'{repo}: release is missing {skill}/SKILL.md')
            if any(p.is_symlink() for p in [source, *source.rglob('*')]):
                raise ValueError(f'{repo}: skill contains symlinks')
            pending.append((source, root / 'skills' / skill))
            updated[repo] = release
        # Resolve and validate every release before modifying bundled content.
        for source, destination in pending:
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(source, destination)
        if pending:
            lock.write_text(json.dumps(updated, indent=2, sort_keys=True) + '\n')
    print(f'{len(pending)} release update(s) imported')


if __name__ == '__main__':
    sync(Path.cwd())
