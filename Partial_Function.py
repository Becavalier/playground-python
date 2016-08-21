#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数就是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
import functools;
int2 = functools.partial(int, base = 2);
int2('1000000');
# 64
int2('1010101');
# 85


kw = { 'base': 2 };
int('10010', **kw);

# 固定一个参数（默认会传递的参数到函数左边）
max2 = functools.partial(max, 10);
max2(5, 6, 7);
# 10

# args = (10, 5, 6, 7);
# max(*args);

