#!/usr/bin/env python3
"""CI enforcement: every exhibit in this repo must actually run.

Default expectation: exit code 0. A small number of Black_Magic
entries are ALLOWED (required, even) to crash -- see
EXPECTED_NONZERO below. If one of those starts exiting 0, that's not
progress, that's a regression: someone accidentally fixed a crime.
"""

import pathlib
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

# path (relative to repo root) -> human-readable reason it's allowed to crash
EXPECTED_NONZERO = {
    "Black_Magic/deface_small_int.py": (
        "corrupts a cached small int badly enough to segfault on exit "
        "-- that IS the demonstration, not a bug"
    ),
}

# Helper modules that are imported by other exhibits, not meant to be
# run standalone. Running them directly is harmless (they just define
# functions) but proves nothing, so they're skipped rather than graded.
SKIP = {
    "Imports/_wildcard_source.py",
    "Imports/circular_a.py",
    "Imports/circular_b.py",
}

TIMEOUT_SECONDS = 15


def find_exhibits():
    return sorted(
        p for p in REPO_ROOT.rglob("*.py")
        if ".git" not in p.parts and "scripts" not in p.parts
    )


def relpath(path):
    return str(path.relative_to(REPO_ROOT))


def main():
    exhibits = find_exhibits()
    failures = []
    skipped = 0

    for path in exhibits:
        rel = relpath(path)

        if rel in SKIP:
            print(f"SKIP   {rel}  (helper module, not a standalone exhibit)")
            skipped += 1
            continue

        try:
            result = subprocess.run(
                [sys.executable, str(path)],
                cwd=path.parent,
                capture_output=True,
                timeout=TIMEOUT_SECONDS,
                text=True,
            )
            code = result.returncode
        except subprocess.TimeoutExpired:
            print(f"FAIL   {rel}  -- timed out after {TIMEOUT_SECONDS}s")
            failures.append(rel)
            continue

        if rel in EXPECTED_NONZERO:
            reason = EXPECTED_NONZERO[rel]
            if code == 0:
                print(f"FAIL   {rel}  -- expected a crash ({reason}), "
                      f"but it exited cleanly. Did someone fix the bug? Revert that.")
                failures.append(rel)
            else:
                print(f"PASS   {rel}  -- exited {code}, as chaotically expected ({reason})")
            continue

        if code != 0:
            print(f"FAIL   {rel}  -- exited {code}")
            if result.stdout.strip():
                print("  stdout:", result.stdout.strip().replace("\n", "\n          "))
            if result.stderr.strip():
                print("  stderr:", result.stderr.strip().replace("\n", "\n          "))
            failures.append(rel)
        else:
            print(f"PASS   {rel}")

    graded = len(exhibits) - skipped
    print()
    print(f"{graded - len(failures)}/{graded} crimes confirmed functional "
          f"({skipped} helper module(s) skipped).")

    if failures:
        print("\nThe following exhibits did not commit their crime correctly:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
