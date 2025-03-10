#!/usr/bin/env python

import itertools
import re
from typing import List

def variants(pron: str) -> List[str]:
    pieces = []
    for elem in re.split(r"(\(.+?\))", pron):
        if elem.startswith("(") and elem.endswith(")"):
            pieces.append((elem[1:-1], ""))
        else:
            pieces.append((elem,))
    results = [""]
    for piece in pieces:
        results = [prefix + suffix for prefix, suffix in itertools.product(results, piece)]
    return results


assert variants("foo(bar)o(mar)") == [
    "foobaromar",
    "foobaro",
    "fooomar",
    "fooo",
]
assert variants("fo(bar)o") == ["fobaro", "foo"]
assert "barm" not in variants("(bar)fonoa(m)")
assert variants("hotda(w)g") == ["hotdawg", "hotdag"]
assert variants("()") == ["", ""]
assert variants("happy") == ["happy"]
