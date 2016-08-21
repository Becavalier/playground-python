#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# function

a = abs;
a(-1);
# 1

def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x;

# Empty function
def nop():
    pass;

# Throw exception if encounter an error
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type');
    if x >= 0:
        return x;
    else:
        return -x;

# Use import
import math;

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return nx, ny;

# Default param
def power(x, n = 2):
    s = 1;
    while n > 0:
        n = n - 1;
        s = s * x;
    return s;


def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name);
    print('gender:', gender);
    print('age:', age);
    print('city:', city);

enroll('Adam', 'M', city = 'Tianjin');


def calc(numbers):
    sum = 0;
    for n in numbers:
        sum = sum + n * n;
    return sum;

calc([1, 2, 3]);


def calc(*numbers):
    sum = 0;
    for n in numbers:
        sum = sum + n * n;
    return sum;

nums = [1, 2, 3];
calc(*nums);

# Keyword params

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw);

extra = {'city': 'Beijing', 'job': 'Engineer'};
person('Jack', 24, city = extra['city'], job = extra['job']);

extra = {'city': 'Beijing', 'job': 'Engineer'}；
person('Jack', 24, **extra);


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw);


# Name params

def person(name, age, *, city, job):
    print(name, age, city, job);

person('Jack', 24, city = 'Beijing', job = 'Engineer');



def person(name, age, *args, city, job):
    print(name, age, args, city, job);

person('Jack', 24, extra = 'extra', city = 'Beijing', job = 'Engineer');




def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw);

def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw);

# Universal method
args = (1, 2, 3, 4);
kw = {'d': 99, 'x': '#'};
f1(*args, **kw);
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3);
kw = {'d': 88, 'x': '#'};
f2(*args, **kw);


