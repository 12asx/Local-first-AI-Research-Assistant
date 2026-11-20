"""Read-only initial guardrail for a public ResearchAgent repository.

Does not guarantee that code or Git history is safe. Read the flagged files,
check submodules and Git history, and use dedicated secret scanning tools.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BAD_PATH = re.compile(
    r'(^|/)(data|papers|private|secrets|backups|logs|uploads|chats|conversations|memory|references)/'
    r'|(?:^|/)(?:\.env(?:\..*)?|settings\.json|settings\.local\.json|running\.json)$'
    r'|\.(?:pdf|caj|docx|sqlite3?|db|pem|p12|key)$', re.I
)
TOKEN_PATTERNS = [
    ('GitHub personal access token', re.compile(r'gh[pousr]_[A-Za-z0-9_]{25,}')),
    ('Generic live-looking API key', re.compile(r'\bsk-[A-Za-z0-9_-]{24,}\b')),
    ('AWS access key', re.compile(r'AKIA[0-9A-Z]{16}')),
    ('Possible embedded bearer credential', re.compile(r'(?i)Authorization\s*[:=]\s*["\']Bearer\s+[^"\']{20,}')),
    ('Absolute Windows personal path', re.compile(r'[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\\\s"\']+')),
]

def tracked_candidates():
    cmd = ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z']
    p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        print('Git repository not initialized. Run: git init  (after copying .gitignore)')
        return None
    return [Path(p.decode('utf-8', errors='replace')) for p in p.stdout.split(b'\0') if p]


def main():
    files = tracked_candidates()
    if files is None: return 2
    errors = 0
    for rel in files:
        normalized = rel.as_posix()
        if BAD_PATH.search(normalized):
            print('[BLOCK] Private/sensitive path could be committed:', normalized)
            errors += 1
            continue
        path = ROOT / rel
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            data = path.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            continue
        for name, pattern in TOKEN_PATTERNS:
            if pattern.search(data):
                print(f'[REVIEW] {name}: {normalized}')
                errors += 1
    if errors:
        print(f'\nFound {errors} possible publication risks. Inspect manually; do not push yet.')
        return 1
    print(f'Checked {len(files)} candidate files. No obvious flags. MANUAL review still required.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
