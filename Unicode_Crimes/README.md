# Unicode Crimes

Crimes against the assumption that two identifiers which look identical on screen are, in fact, the same identifier.

- `homoglyph_variables.py` — Latin `a` vs. Cyrillic `а`, two different variables, one visual
- `combining_diacritics.py` — two identifiers that render nearly identically, one wearing five invisible stacked accent marks
- `emoji_in_data.py` — emoji can't be identifiers, but nothing stops them from being everything else
