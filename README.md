# 🩸 python-war-crimes

[![Confirm the crimes still work](https://github.com/Xia-Qi2450/python-war-crimes/actions/workflows/crimes-ci.yml/badge.svg)](https://github.com/Xia-Qi2450/python-war-crimes/actions/workflows/crimes-ci.yml)

> *"It compiled. Ship it."*

A living archive of Python code that violates every principle of good engineering — and somehow, against all reason, **runs correctly**.

This is not a repository of bugs. Bugs get fixed. These get *committed*.

## The Charter

All contributions are judged by one standard: **does it work, and is it horrifying?** Both conditions must be true. Code that merely fails is not a war crime — it's just broken. Code that succeeds *despite itself* is what we're after.

Read [`Geneva_Convention.md`](./Geneva_Convention.md) for the full list of rules you are encouraged to violate.

## The Archive

| Folder | Crimes Against |
|---|---|
| [`Variables/`](./Variables) | Naming conventions, sanity |
| [`Functions/`](./Functions) | Statelessness, purity |
| [`Control_Flow/`](./Control_Flow) | Readability, your reviewer's will to live |
| [`Classes/`](./Classes) | The MRO, Liskov, common decency |
| [`Exceptions/`](./Exceptions) | Error handling, honesty |
| [`Imports/`](./Imports) | Namespaces, dependency graphs |
| [`Unicode_Crimes/`](./Unicode_Crimes) | The Latin alphabet |
| [`Built-in_Abuse/`](./Built-in_Abuse) | `str`, `list`, `type`, and God |
| [`Black_Magic/`](./Black_Magic) | The CPython implementation |
| [`Production_Sightings/`](./Production_Sightings) | Real users, real money, real regret |

## Running the exhibits

Every file is meant to be run directly:

```bash
python3 Functions/mutable_default_args.py
```

Each one has a docstring at the top explaining exactly why it shouldn't work — read that first, then run it, then sit with your feelings.

CI runs every exhibit on every PR across Python 3.11, 3.12, and 3.13, and fails the build if a file stops exiting `0` — with one deliberate exception: `Black_Magic/deface_small_int.py` is *supposed* to crash, and CI fails if it stops crashing. See `scripts/verify_crimes.py`.

## Contributing

1. Write code that breaks a rule in `Geneva_Convention.md`.
2. Confirm it actually runs. `python3 your_crime.py` must exit `0`, or the crime doesn't count — it's just a bug. (If your crime is supposed to crash the interpreter, add it to `EXPECTED_NONZERO` in `scripts/verify_crimes.py` and say why.)
3. Add a one-line docstring at the top explaining *why* this should not work.
4. Open a PR using the template. Include the Python version you tested on — some of these are CPython implementation details and will not survive contact with PyPy, or even a newer CPython.

## Disclaimer

No code in this repository should be used in production.
Several entries were *found* in production. That is the tragedy, not the endorsement. See [`Production_Sightings/`](./Production_Sightings) for details, names redacted to protect the guilty.

## License

MIT. Do whatever you want with these. Frankly, someone should stop you, but it won't be this license.
