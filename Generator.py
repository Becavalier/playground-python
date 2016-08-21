#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Initial a generator
g = (x * x for x in range(10));
next(g);

for n in g:
	print(n);

# 吐槽：跟ES6的生成器简直用法一模一样

def fib(max):
    n, a, b = 0, 0, 1;
    while n < max:
        print(b);
        a, b = b, a + b;
        n = n + 1;
    return 'done';


a, b = b, a + b;
# The same as
# t = (b, a + b);
# a = t[0];
# b = t[1];


g = fib(6);
while True:
    try:
        x = next(g);
        print('g:', x);
    except StopIteration as e:
        print('Generator return value:', e.value);
        break;