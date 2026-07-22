"""Why this shouldn't work: except BaseException catches
KeyboardInterrupt and SystemExit too, which means this "safe" step
runner will politely swallow sys.exit() and just keep going."""

import sys

def run_step(step_fn):
    try:
        step_fn()
    except BaseException as e:
        print(f"step failed quietly: {type(e).__name__}")

def step_that_exits():
    sys.exit("this should have ended the program")

run_step(step_that_exits)
print("we are still here, and sys.exit() did not exit anything")
