"""Run with python3 scripts/test-sync-skills.py; requires Git and rsync."""
from pathlib import Path
import subprocess
import tempfile

script = Path(__file__).with_name('sync-skills.sh').resolve()
with tempfile.TemporaryDirectory() as temporary:
    root = Path(temporary)
    upstream = root / 'upstream'
    mappings = [('clean-coding', 'clean-development'), ('clean-code-review', 'clean-code-review')]
    for repo, skill in mappings:
        checkout = upstream / repo
        source = checkout / 'skills' / skill
        source.mkdir(parents=True)
        (source / 'SKILL.md').write_text(f'# {skill}\n')
        (source / 'reference.md').write_text('Supporting content\n')
        subprocess.run(['git', 'init', '-q', str(checkout)], check=True)
        subprocess.run(['git', '-C', str(checkout), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(checkout), '-c', 'user.name=Test', '-c',
                        'user.email=test@example.com', 'commit', '-qm', 'fixture'], check=True)
        destination = root / 'skills' / skill
        destination.mkdir(parents=True)
        (destination / 'stale.md').write_text('Remove me')
    command = ['bash', str(script), str(upstream)]
    subprocess.run(command, cwd=root, check=True)
    for repo, skill in mappings:
        source = upstream / repo / 'skills' / skill
        destination = root / 'skills' / skill
        assert sorted(p.name for p in source.iterdir()) == sorted(p.name for p in destination.iterdir())
        for path in source.iterdir():
            assert path.read_bytes() == (destination / path.name).read_bytes()
    before = {str(p.relative_to(root)): p.read_bytes() for p in (root / 'skills').rglob('*') if p.is_file()}
    subprocess.run(command, cwd=root, check=True)
    assert before == {str(p.relative_to(root)): p.read_bytes() for p in (root / 'skills').rglob('*') if p.is_file()}
    (upstream / 'clean-code-review/skills/clean-code-review/SKILL.md').unlink()
    assert subprocess.run(command, cwd=root).returncode != 0
    assert before == {str(p.relative_to(root)): p.read_bytes() for p in (root / 'skills').rglob('*') if p.is_file()}
print('PASS: complete copies, stale-file removal, idempotence, missing-source protection')
