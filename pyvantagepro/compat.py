# coding: utf8
"""
    pyvantagepro.compat
    -------------------

    Compatibility utilities for Python 3.10+

    :copyright: Copyright 2012 Salem Harrache and contributors, see AUTHORS.
    :license: GNU GPL v3.

"""

from logging import NullHandler
from collections import OrderedDict
from io import StringIO


def to_char(string):
    if len(string) == 0:
        return str('')
    return str(string[0])
