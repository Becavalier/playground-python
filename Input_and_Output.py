#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Hello", "World!");

print("300 + 100 = ", 300 + 100);


# Input

name = input("Please input your name: ");

print("Hello", name);

# Operation

print(10 / 3);
# 3.33333333

print(9 / 3);
# 3.0

print(10 // 3);
# 3

print(r'\\\t\\');
# \\\t\\

print('''line1
line2
line3''');

# line1
# line2
# line3

print('包含中文的str');
# 包含中文的str

ord('A');
# 65

ord('中');
# 20013

chr(66);
# 'B'

chr(25991);
# '文'

# Variable x is a type of byte
x = b'ABC'


'ABC'.encode('ascii');
# b'ABC'

'中文'.encode('utf-8');
# b'\xe4\xb8\xad\xe6\x96\x87'

'中文'.encode('ascii');
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

b'ABC'.decode('ascii');
# 'ABC'

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8');
# '中文'


len('ABC');
# 3

len('中文');
# 2

len(b'\xe4\xb8\xad\xe6\x96\x87');
# 6


'Hello, %s' % 'world';
# 'Hello, world'

'Hi, %s, you have $%d.' % ('Michael', 1000000);
# 'Hi, Michael, you have $1000000.'

'%2d-%02d' % (3, 1);
# ' 3-01'

'%.2f' % 3.1415926;
# '3.14'

'growth rate: %d %%' % 7;
# 'growth rate: 7 %'

