"""Why this shouldn't work: this script reads its own source file
off disk, appends a marker line to itself, and writes that back to
disk -- while it is still running. Run it more than once and it
remembers, in its own body, how many times it's been run."""

import pathlib

THIS_FILE = pathlib.Path(__file__)
MARKER = "#" + " RAN:"  # assembled at runtime so this line doesn't itself count as a marker

def run_count():
    text = THIS_FILE.read_text()
    return text.count(MARKER)

count = run_count()
print(f"this file has rewritten itself {count} time(s) before now")

with THIS_FILE.open("a") as f:
    f.write(f"\n{MARKER} {count + 1}\n")
