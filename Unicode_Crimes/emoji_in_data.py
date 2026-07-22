"""Why this shouldn't work (or rather, why you'd assume it can't):
Python identifiers can't be emoji -- they aren't valid ID_Start/
ID_Continue characters. But nothing stops you from using emoji as
dict keys, de facto enum values, or f-string content."""

status = {
    "\u2705": "passed",
    "\u274c": "failed",
    "\U0001F525": "on fire, technically still running",
}

for emoji, meaning in status.items():
    print(f"{emoji}: {meaning}")

DEPLOY_STATE = "\U0001F680"  # a rocket, functioning as an enum value
if DEPLOY_STATE == "\U0001F680":
    print("deployed")
