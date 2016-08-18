#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
d['Michael'];
# 95

'Thomas' in d;
# False

d.get('Thomas', -1);
# -1

# Remove element from a dict
d.pop('Bob');



# set

s = set([1, 2, 3]);

s = set([1, 1, 2, 2, 3, 3]);
s
# {1, 2, 3}

s.add(4);
s
# {1, 2, 3, 4}

s.remove(4);
s
# {1, 2, 3}

s1 = set([1, 2, 3]);
s2 = set([2, 3, 4]);
s1 & s2;
# {1, 2, 3, 4}



