#!/usr/bin/env python3
# -*- coding: utf-8 -*-

abs(-1);
# 1

abs
# <built-in function abs>

x = abs(-10);
x;
# 10

# "abs" just like a pointer and point to a real method structure
f = abs;
f(-20);
# 20

def add(x, y, f):
    return f(x) + f(y);

print(add(1, -10, abs));
# 11


# map()

def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
list(r);
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]));
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce()

from functools import reduce;
def add(x, y):
	return x + y;

reduce(add, [1, 3, 5, 7, 9]);
# 25

def fn(x, y):
	return x * 10 + y;

reduce(fn, [1, 2, 3, 4]);
# 1234


from functools import reduce;
def fn(x, y):
	return x * 10 + y;

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

reduce(fn, map(char2num, '13579'));


####################################
from functools import reduce;

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
    return reduce(fn, map(char2num, s));

####################################


# Use lambda
from functools import reduce;

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s));


# filter()

def is_odd(n):
    return n % 2 == 1;

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]));
# [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip();

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']));
# ['A', 'B', 'C'];


def primes():
    yield 2
    it = _odd_iter();
    while True:
        n = next(it);
        yield n;
        it = filter(_not_divisible(n), it);

# sorted()

sorted([36, 5, -12, 9, -21]);
# [-21, -12, 5, 9, 36]

sorted([36, 5, -12, 9, -21], key = abs);
# [5, 9, -12, -21, 36]

sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower);
# ['about', 'bob', 'Credit', 'Zoo']

sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True);
# ['Zoo', 'Credit', 'bob', 'about']


def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = ax + n;
        return ax;
    return sum;

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1 == f2;
# False



def count():
    fs = [];
    for i in range(1, 4):
        def f():
             return i * i;
        fs.append(f);
    return fs;

# fs本身其实保持着对f()的三个引用，当执行到最后的时候fs为[f, f, f], 此时i为3
f1, f2, f3 = count();

f1();
f2();
f3();
# 9 9 9


def count():
    fs = [];
    for i in range(1, 4):
        def f():
             return i * i;
        fs.append(f());
    return fs;

f1, f2, f3 = count();
# 1 4 9



def count():
    def f(j):
        def g():
            return j * j
        return g;
    fs = [];
    for i in range(1, 4):
        fs.append(f(i));
    return fs;

# 已绑定到函数参数的值不变，即函数g()里面的参数j的值
f1, f2, f3 = count();

f1();
f2();
f3();
# 1 4 9



# Anonymous Function
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]));
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# lambda x: x * x 
# x is parameter
# the content after colon is the function body
def f(x):
    return x * x;

f = lambda x: x * x;
f(10);
# 100

def build(x, y):
    return lambda: x * x + y * y;

build(1, 2)();
# 5
