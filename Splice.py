#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A list
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'];

# Get first three elements
# 1
[L[0], L[1], L[2]];

# 2
r = [];
for i in range(3):
	r.append(L[i]);
print r;


# Use splice
L[0:3];

# Same as
L[:3];

# -1, -2 ['Bob', 'Jack']
L[-2:];

#
L = list(range(100));

L[:10:2];

# Copy a list
L[:];

# The third param is detemine you want this number as a interval step [0, 5, 10]
L[::5];


# Splice feature on string
'ABCDEFG'[:3];

'ABCDEFG'[::2];

d = {'a': 1, 'b': 2, 'c': 3};
for key in d:
    print(key);

for value in d.values():
	print(value);

for k, v in d.items():
	print(k, v);

for ch in 'ABC':
	print(ch);

# detemine if an object is an iterable object
from collections import Iterable;
isinstance('abc', Iterable);
isinstance([1,2,3], Iterable);
isinstance(123, Iterable);

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value);



