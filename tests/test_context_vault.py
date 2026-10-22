import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "bin" / "jstack_context.py"


class VaultSelectionTests(unittest.TestCase):
    def execute(self, home, cwd):
        environment = dict(os.environ, HOME=str(home))
        return subprocess.run(
            [sys.executable, str(SCRIPT), "contextneedle"],
            cwd=cwd, env=environment, capture_output=True, text=True,
        )

    def test_unconfigured_vault_refuses_without_searching_current_directory(self):
        for configuration in (None, {}, {"obsidian_vault_path": ""}):
            with self.subTest(configuration=configuration), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                home, cwd = root / "home", root / "cwd"
                home.mkdir()
                cwd.mkdir()
                (cwd / "decoy.md").write_text("contextneedle CWD_MUST_NOT_BE_RETRIEVED")
                if configuration is not None:
                    (home / ".jstack").mkdir()
                    (home / ".jstack/config.json").write_text(json.dumps(configuration))
                result = self.execute(home, cwd)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("Configure vault:", result.stderr)

    def test_explicit_vault_is_searched_instead_of_current_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            home, cwd, vault = root / "home", root / "cwd", root / "vault"
            for directory in (home, cwd, vault):
                directory.mkdir()
            (home / ".jstack").mkdir()
            (home / ".jstack/config.json").write_text(json.dumps({"obsidian_vault_path": str(vault)}))
            (cwd / "decoy.md").write_text("contextneedle CWD_MUST_NOT_BE_RETRIEVED")
            (vault / "real.md").write_text("contextneedle EXPECTED_VAULT_RESULT")
            result = self.execute(home, cwd)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("EXPECTED_VAULT_RESULT", result.stdout)
            self.assertNotIn("CWD_MUST_NOT_BE_RETRIEVED", result.stdout)
            self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
