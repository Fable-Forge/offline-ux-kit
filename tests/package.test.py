import hashlib
import pathlib
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKAGE_SCRIPT = ROOT / "scripts" / "package.py"


class PackageTests(unittest.TestCase):
    def test_archive_has_one_generated_manifest_and_identical_source_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            archive_path = pathlib.Path(temp_dir) / "offline-ux-kit.zip"
            subprocess.run(
                [sys.executable, str(PACKAGE_SCRIPT), str(archive_path)],
                check=True,
                capture_output=True,
                text=True,
            )

            source_files = sorted(
                path
                for path in ROOT.rglob("*")
                if path.is_file()
                and path.name != "SHA256SUMS.txt"
                and not any(part in (".git", "node_modules", "__pycache__") for part in path.parts)
            )
            expected_manifest = "".join(
                hashlib.sha256(path.read_bytes()).hexdigest()
                + "  "
                + path.relative_to(ROOT).as_posix()
                + "\n"
                for path in source_files
            ).encode("utf-8")
            manifest_name = "offline-ux-kit/SHA256SUMS.txt"

            with zipfile.ZipFile(archive_path) as archive:
                names = archive.namelist()
                self.assertEqual(len(names), len(set(names)))
                self.assertEqual(names.count(manifest_name), 1)
                self.assertEqual(archive.read(manifest_name), expected_manifest)
                for path in source_files:
                    member = "offline-ux-kit/" + path.relative_to(ROOT).as_posix()
                    self.assertEqual(archive.read(member), path.read_bytes())


if __name__ == "__main__":
    unittest.main()
