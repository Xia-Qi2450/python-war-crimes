# python-war-crimes

[![Confirm the crimes still work](https://github.com/Xia-Qi2450/python-war-crimes/actions/workflows/crimes-ci.yml/badge.svg?branch=main)](https://github.com/Xia-Qi2450/python-war-crimes/actions/workflows/crimes-ci.yml)

> *"It compiled. Ship it."*

OK why this heck does this even exist??? This is a live collection of the many cursed and badly coded Python beginners and people who experiment with random stuff do which **will** make people doubt being friend with you.

This is not really a repository of bugs. Bugs get fixed. These somehow gets *committed*.

## Rules and Regulations

All contributions are judged by one standard: **does it work, and is it horrifying?** Both conditions must be true. Code that merely fails is not a war crime, it's just broken. Code that succeeds *despite itself* is what we're after.

Read [`Geneva_Convention.md`](./Geneva_Convention.md) for the full list of rules you are absolutely encouraged to violate.

## The Repo

| Folder | Crimes Against |
|---|---|
| [`Variables/`](./Variables) | Horrifying definitions, sanity -100 |
| [`Functions/`](./Functions) | Some Functions names that will haunt you |
| [`Control_Flow/`](./Control_Flow) | YandereDev impersonations |
| [`Classes/`](./Classes) | Really badly made and used classes |
| [`Exceptions/`](./Exceptions) | `try` and `except` more like I don't care about bugs |
| [`Imports/`](./Imports) | Importing can be challenging at times, but this is way worse |
| [`Unicode_Crimes/`](./Unicode_Crimes) | See what happens if you mix different languages together |
| [`Built-in_Abuse/`](./Built-in_Abuse) | `str`, `list`, `type`, and God |
| [`Black_Magic/`](./Black_Magic) | The reason for the existence of CPython implementations |
| [`Production_Sightings/`](./Production_Sightings) | These war crimes somehow appears in real applications |

## Running the exhibits

You can definitely run each file they are all 100% safe:

```bash
python3 Functions/mutable_default_args.py
```

Each one has a docstring at the top explaining exactly why it shouldn't work. Before you run it read that first, then you may proceed, then sit with yourfeelings(*WHAT HAVE YOU DONE???*).

CI runs every exhibit on every PR across Python 3.11, 3.12, and 3.13, and fails the build if a file stops exiting `0` but there is one deliberate exception: `Black_Magic/deface_small_int.py` is *supposed* to crash, depending on CPython's internal memory layout, outcome varies by build and platform (confirmed: it segfaults on some 3.12 builds and exits cleanly on others). Check `scripts/verify_crimes.py` for more info.

## Contributing

Wait? You want to contibute to this madness that is this repository? Well you are definitely welcome to do so. Here are some steps in being able to add your own Python War Crimes into this collection:

1. Write code that breaks a rule in `Geneva_Convention.md`.
2. Confirm it actually runs. `python3 your_crime.py` must exit `0`, or the crime doesn't count — it's just a bug. (If your crime is supposed to crash the interpreter, add it to `EXPECTED_NONZERO` in `scripts/verify_crimes.py` and say why.)
3. Add a one-line docstring at the top explaining *why* this should not work.
4. Open a PR using the template. Include the Python version you tested on — some of these are CPython implementation details and will not survive contact with PyPy, or even a newer CPython.

## Disclaimer

Please **DO NOT** use any code found in this repository and use it in production.
Several entries were *found* in production. That is the tragedy, not the endorsement. See [`Production_Sightings/`](./Production_Sightings) for details, names redacted to protect the guilty.

## License

MIT. Do whatever you want with these. Frankly, someone should stop you, but it won't be this license.
