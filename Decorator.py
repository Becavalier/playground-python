#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def now():
    print('2015-3-25');

f = now;
f();

# __name__

now.__name__;
# 'now'
f.__name__;
# 'now'

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__);
        return func(*args, **kw);
    return wrapper;

# Define a decorator
# now = log(now);
@log
def now():
    print('2015-3-25');

now();
# call now():
# 2015-3-25

import functools;

def log(func):
    @functools.wraps(func);
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__);
        return func(*args, **kw);
    return wrapper;

# A decorator method with parameters
import functools;

def log(text):
    def decorator(func):
        @functools.wraps(func);
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__));
            return func(*args, **kw);
        return wrapper;
    return decorator;