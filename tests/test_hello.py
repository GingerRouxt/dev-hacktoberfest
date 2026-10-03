import subprocess
import sys
import unittest
from pathlib import Path

from hello import greet


ROOT = Path(__file__).resolve().parents[1]


class GreetingTests(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, contributor!")

    def test_whitespace_fallback_and_trimming(self):
        self.assertEqual(greet("  "), "Hello, contributor!")
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_unicode_name(self):
        self.assertEqual(greet("Zoë"), "Hello, Zoë!")

    def test_cli_default(self):
        result = subprocess.run(
            [sys.executable, "hello.py"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout, "Hello, contributor!\n")
        self.assertEqual(result.stderr, "")

    def test_cli_name(self):
        result = subprocess.run(
            [sys.executable, "hello.py", "Ada"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout, "Hello, Ada!\n")

    def test_cli_rejects_unknown_option(self):
        result = subprocess.run(
            [sys.executable, "hello.py", "--not-a-real-option"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("unrecognized arguments", result.stderr)


if __name__ == "__main__":
    unittest.main()
