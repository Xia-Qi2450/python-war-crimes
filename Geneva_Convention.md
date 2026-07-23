# The Geneva Convention (Python Edition)

*Ratified by nobody. Enforced by nobody. Violated by everybody in this repository.*

This document lists the customary laws of civilized Python development. Contributors to `python-war-crimes` are expected to have read these rules **in order to break them intelligently** — accidental crimes are bugs, not art.

---

### Article I — You Shall Not Shadow Built-ins
Do not name a variable `list`, `dict`, `str`, `type`, `id`, `input`, or `len`. The interpreter will let you. It will not warn you. It will simply wait, patiently, for the worst possible moment.
> *Violations: [`Built-in_Abuse/`](./Built-in_Abuse)*

### Article II — You Shall Not `except: pass`
An error was raised. Something, somewhere, went wrong. Silently discarding it does not mean it didn't happen — it means nobody will know it happened until it happens again, in production, on a Friday.
> *Violations: [`Exceptions/`](./Exceptions)*

### Article III — You Shall Not Nest More Than 3 Levels of Control Flow
Beyond three levels of indentation, you are no longer writing logic. You are writing a maze, and you are also the rat.
> *Violations: [`Control_Flow/`](./Control_Flow)*

### Article IV — You Shall Not Use Mutable Default Arguments
`def f(x, cache=[])` does not create a new list every call. It creates one list, forever, shared across every call, silently accumulating state like a haunted house accumulates ghosts.
> *Violations: [`Functions/`](./Functions)*

### Article V — You Shall Not `from module import *`
You do not know what you just imported. Neither does your linter. Neither, increasingly, does the module.
> *Violations: [`Imports/`](./Imports)*

### Article VI — You Shall Not Monkey-Patch Built-in Types
`int`, `str`, and `list` are not yours to modify. That some of them can be, with enough `ctypes`, is not permission. It is a loophole, and loopholes are how wars start.
> *Violations: [`Black_Magic/`](./Black_Magic)*

### Article VII — You Shall Not `eval`/`exec` Strings You Built at Runtime
If your program writes programs which your program then runs, you no longer have a program. You have an ecosystem, and ecosystems have predators.
> *Violations: [`Black_Magic/`](./Black_Magic)*

### Article VIII — You Shall Not Write Homoglyph or Zero-Width Identifiers
A variable named with a Cyrillic `а` looks exactly like a variable named with a Latin `a`. It is not the same variable. Your reviewer will not notice. Neither will you, six months from now.
> *Violations: [`Unicode_Crimes/`](./Unicode_Crimes)*

### Article IX — You Shall Not Use Exceptions as `goto`
`raise` is for errors, not for jumping out of a nested loop because you didn't want to write a flag variable.
> *Violations: [`Control_Flow/`](./Control_Flow), [`Exceptions/`](./Exceptions)*

### Article X — You Shall Not Ship Code That Only Works By CPython Accident
Reference counting quirks, dict insertion order, small-int caching — these are implementation details, not language guarantees. Code that depends on them is not clever. It is a time bomb with a CPython-shaped fuse.
> *Violations: [`Black_Magic/`](./Black_Magic), [`Production_Sightings/`](./Production_Sightings)*

---

**Signed in bad faith by everyone who has ever pushed directly to `main`.**
