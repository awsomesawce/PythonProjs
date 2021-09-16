"""Changed Conda env to be on the D drive instead.

Progress on becoming a Pythonista has been coming along nicely.

## Goals

- [ ] Take a list of paths and iterate thru them.  If the path exists, return it,
otherwise if the path doesn't exist, just skip over it without throwing an exception."""

import os, sys, inspect
import pathlib, glob

mysyspath = sys.path[1:] # Only include paths that exist or are not _nothing_.

conda_activate = "conda activate"

important_projs = {
    "scripts-pwsh": pathlib.Path(os.path.expanduser("~/gitstuff/scripts-pwsh")),
    "lot": pathlib.Path(os.path.expandvars("%OneDrive%/snippets/python"))
}




print(important_projs)
