"""Why this shouldn't work: this is a real Python easter egg.
`import antigravity` is a fully functional standard-library module
whose entire job is to open a browser tab to an XKCD comic about
how easy Python is. It ships with every CPython install."""

import antigravity  # opens https://xkcd.com/353/ in your default browser
print("if a browser tab just opened, that's not a bug -- that's the stdlib")
