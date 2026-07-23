#!/usr/bin/env python3
"""CI enforcement: every exhibit in this repo must actually run.

Default expectation: exit code 0. A small number of Black_Magic
entries are genuinely unpredictable by design -- see UNSTABLE below.
Those are logged, never graded pass/fail: there is no "correct" exit
code to hold them to.
"""

import pathlib
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

# path (relative to repo root) -> human-readable reason its outcome
# is INTENTIONALLY unpredictable. These depend on CPython's internal
# memory layout, which varies by version, build, and platform -- a
# clean exit, a crash, or an actually-defaced integer are all
# consistent with the crime. They're run and logged, but never
# graded pass/fail, because there is no "correct" exit code to check
# against. (Confirmed in the wild: this segfaults on some builds of
# 3.12 and exits 0 cleanly on others. Both are the demonstration.)
UNSTABLE = {
    "Black_Magic/deface_small_int.py": (
        "depends on CPython's internal PyLongObject layout -- may exit 0, "
        "crash, or actually deface the integer, depending on version/build/platform"
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
    unstable = 0

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

        if rel in UNSTABLE:
            reason = UNSTABLE[rel]
            print(f"INFO   {rel}  -- exited {code} ({reason})")
            unstable += 1
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

    graded = len(exhibits) - skipped - unstable
    print()
    print(f"{graded - len(failures)}/{graded} crimes confirmed functional "
          f"({skipped} helper module(s) skipped, {unstable} logged as unstable-by-design).")

    if failures:
        print("\nThe following exhibits did not commit their crime correctly:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
