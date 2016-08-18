#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
classmates = ['Michael', 'Bob', 'Tracy'];

len(classmates);
# 3

classmates[0];
# 'Michael'

classmates[1];
# 'Bob'

classmates[2];
# 'Tracy'

classmates[-1];
# 'Tracy'

# Append element to a list
classmates.append('Adam');

# Insert an element into a list at position 1
classmates.insert(1, 'Jack');

# Delete the element at the end of the list and return/echo
classmates.pop();

# A list in a list
s = ['python', 'java', ['asp', 'php'], 'scheme'];




# tuple (Can not change since created, but safer)
classmates = ('Michael', 'Bob', 'Tracy');

# This is a number, not a tuple
t = (1);

# This is a tuple with only on element
t = (1,);

# The list inside a tuple can be changed
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t
# ('a', 'b', ['X', 'Y'])


