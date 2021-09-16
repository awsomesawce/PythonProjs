#!/usr/bin/env python
"""Try to find a file using globbing"""

import os, sys, glob, inspect
import pathlib, hashlib


def findThatFile(pattern: str):
    if glob.glob(pattern):
        with open(glob.glob(pattern)[0]) as f:
                  return f.read()


print(findThatFile('*Amazing*'))
