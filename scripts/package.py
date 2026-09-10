"""Build a portable ZIP and verify every byte against the source tree."""
import hashlib
import pathlib
import sys
import zipfile

root = pathlib.Path(__file__).resolve().parent.parent
target = pathlib.Path(sys.argv[1]).resolve()
target.parent.mkdir(parents=True, exist_ok=True)
files = sorted(
    p for p in root.rglob('*')
    if p.is_file()
    and p.resolve() != target
    and p.relative_to(root).as_posix() != 'SHA256SUMS.txt'
    and not any(x in p.parts for x in ('.git', 'node_modules', '__pycache__'))
)
manifest = []
for p in files:
    content = p.read_bytes()
    if content.startswith(b'%TSD-Header'):
        raise SystemExit('Encrypted-wrapper marker found: ' + str(p.relative_to(root)))
    content.decode('utf-8')
    manifest.append(hashlib.sha256(content).hexdigest() + '  ' + p.relative_to(root).as_posix())
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
    for p in files:
        archive.write(p, 'offline-ux-kit/' + p.relative_to(root).as_posix())
    archive.writestr('offline-ux-kit/SHA256SUMS.txt', '\n'.join(manifest) + '\n')
with zipfile.ZipFile(target) as archive:
    damaged = archive.testzip()
    if damaged is not None:
        raise SystemExit('ZIP CRC check failed: ' + damaged)
    names = archive.namelist()
    if len(names) != len(set(names)):
        raise SystemExit('ZIP contains duplicate paths')
    for p in files:
        member = 'offline-ux-kit/' + p.relative_to(root).as_posix()
        if archive.read(member) != p.read_bytes():
            raise SystemExit('ZIP round-trip mismatch: ' + str(p.relative_to(root)))
    if archive.read('offline-ux-kit/SHA256SUMS.txt') != ('\n'.join(manifest) + '\n').encode('utf-8'):
        raise SystemExit('ZIP manifest mismatch')
print(f'Verified {len(files)} UTF-8 files; ZIP round-trip identical: {target}')
print('ZIP SHA256:', hashlib.sha256(target.read_bytes()).hexdigest())
