"""A small, dependency-free greeting CLI for testing contributions."""

import argparse


def greet(name: str = "contributor") -> str:
    """Return a greeting, using a fallback for empty or whitespace-only names."""
    name = name.strip() or "contributor"
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", nargs="?", default="contributor")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
