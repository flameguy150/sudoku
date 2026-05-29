"""Create a text file showing the project file structure."""

from pathlib import Path


ROOT = Path(__file__).parent
OUTPUT_FILE = ROOT / "project_structure.txt"

IGNORE_DIRS = {
    ".git",
    ".history",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
}


def build_tree(directory, prefix=""):
    entries = sorted(
        [entry for entry in directory.iterdir() if entry.name not in IGNORE_DIRS],
        key=lambda entry: (entry.is_file(), entry.name.lower()),
    )

    lines = []
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "`-- " if is_last else "|-- "
        lines.append(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "    " if is_last else "|   "
            lines.extend(build_tree(entry, prefix + extension))

    return lines


def main():
    lines = [ROOT.name]
    lines.extend(build_tree(ROOT))

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Project structure written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
