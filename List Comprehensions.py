#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(range(1, 11));
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1, 11):
	L.append(x * x);

[x * x for x in range(1, 11)];

[x * x for x in range(1, 11) if x % 2 == 0];

[m + n for m in 'ABC' for n in 'XYZ'];

import os;
[d for d in os.listdir('.')];

d = {'x': 'A', 'y': 'B', 'z': 'C' };
[k + '=' + v for k, v in d.items()];

L = ['Hello', 'World', 'IBM', 'Apple'];
[s.lower() for s in L];