#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

import string
import base64

myTable = [82, 57, 76, 121, 54, 78, 111, 74, 118, 115, 73, 80, 110, 87, 104, 69, 84, 89, 116, 72, 101, 52, 83, 100, 108, 43, 77, 98, 71, 117, 106, 97, 90, 112, 107, 49, 48, 50, 119, 75, 67, 114, 55, 47, 79, 68, 103, 53, 122, 88, 65, 70, 113, 81, 102, 120, 66, 105, 99, 86, 51, 109, 56, 85]
myTable = "".join(map(chr, myTable))
#  print myTable, len(myTable)

key = [101, 81, 52, 121, 52, 54, 43, 86, 117, 102, 90, 122, 100, 70, 78, 70, 100, 120, 48, 122, 117, 100, 115, 97, 43, 121, 89, 48, 43, 74, 50, 109]
key = "".join(map(chr, key))
#  print key, len(key)

stdTable = string.uppercase + string.lowercase + string.digits + "+/"
assert len(myTable) == len(stdTable)

key = key.translate(string.maketrans(myTable, stdTable))
print base64.b64decode(key)

