# Built-in Abuse

Crimes against `str`, `list`, `dict`, `len`, `print`, and the general assumption that built-in names mean what the documentation says they mean.

- `overriding_builtins.py` — reaches into the `builtins` module and replaces `print` process-wide
- `redefining_len.py` — `len` is reassigned at module scope to lie about list lengths
