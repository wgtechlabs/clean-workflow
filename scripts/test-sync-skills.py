"""Run with python3 scripts/test-sync-skills.py. No network or writes outside temp dirs."""
import importlib.util
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('sync_skills', Path(__file__).with_name('sync-skills.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
assert module.latest_release([[{'draft': False, 'prerelease': True, 'published_at': '2026-02-01'}]]) is None
stable = {'draft': False, 'prerelease': False, 'published_at': '2026-01-01'}
assert module.latest_release([[stable], [{'draft': True, 'prerelease': False, 'published_at': '2026-03-01'}]]) == stable
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for skill in module.SOURCES.values():
        destination = root / 'skills' / skill
        destination.mkdir(parents=True)
        (destination / 'stale.md').write_text('old')
    def snapshot():
        return {str(p.relative_to(root)): p.read_bytes() for p in (root / 'skills').rglob('*') if p.is_file()}
    before = snapshot()
    module.sync(root, lambda repo, temp: None)
    assert snapshot() == before
    def fetch(repo, temp):
        source = temp / repo / 'skills' / module.SOURCES[repo]
        source.mkdir(parents=True)
        (source / 'SKILL.md').write_text('# Released skill')
        (source / 'reference.md').write_text('Released supporting file')
        return {'tag': 'v0.1.0', 'release_id': 1, 'commit': 'a' * 40}, temp / repo
    module.sync(root, fetch)
    assert len(json.loads((root / 'skills/upstream-releases.json').read_text())) == 2
    assert not list((root / 'skills').rglob('stale.md'))
    assert len(list((root / 'skills').rglob('reference.md'))) == 2
    before = snapshot()
    module.sync(root, fetch)
    assert snapshot() == before
    def moved(repo, temp):
        release, checkout = fetch(repo, temp)
        release['commit'] = 'b' * 40
        return release, checkout
    try:
        module.sync(root, moved)
        raise AssertionError('Moved tag accepted')
    except ValueError:
        pass
    assert snapshot() == before
    def incomplete(repo, temp):
        release, checkout = fetch(repo, temp)
        release['tag'] = 'v0.2.0'
        release['commit'] = 'c' * 40
        if repo == 'clean-code-review':
            (checkout / 'skills' / module.SOURCES[repo] / 'SKILL.md').unlink()
        return release, checkout
    try:
        module.sync(root, incomplete)
        raise AssertionError('Missing skill accepted')
    except ValueError:
        pass
    assert snapshot() == before
print('PASS: stable filtering, no-release preservation, full copy, deletions, repeat runs, moved-tag rejection')
