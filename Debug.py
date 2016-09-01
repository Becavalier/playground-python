#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    print('try...');
    r = 10 / 0;
    print('result:', r);
except ZeroDivisionError as e:
    print('except:', e);
except ValueError as e:
    print('ValueError:', e);
else:
    print('no error!');
finally:
    print('finally');
print('end');

# Exception hierarchy
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

import logging;

def foo(s):
    return 10 / int(s);

def bar(s):
    return foo(s) * 2;

def main():
    try:
        bar('0');
    except Exception as e:
        logging.exception(e);

main();
print('END');


# Throw an exception maunally
class FooError(ValueError):
    pass;

def foo(s):
    n = int(s);
    if n == 0:
        raise FooError("invalid value: %s" % s);
    return 10 / n;

foo('0');



def foo(s):
    n = int(s);
    if n == 0:
        raise ValueError("invalid value %s" % s);
    return 10 / n;

def bar():
    try:
        foo('0');
    except ValueError as e:
        print("ValueError");
        # 将异常向上抛到上层
        raise;

bar();


# 断言
def foo(s):
    n = int(s);
    assert n != 0, 'n is zero!';
    return 10 / n;

def main():
    foo('0');

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!

# python3 -O err.py (-O 命令来关闭断言)


# logging

import logging;
# 设置输出的错误级别
logging.basicConfig(level = logging.INFO);

s = '0';
n = int(s);
logging.info('n = %d' % n);
print(10 / n);

# pdb
s = '0';
n = int(s);
print(10 / n);

# python3 -m pdb err.py (Python单步调试)
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000


# 单元测试
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191629979802b566644aa84656b50cd484ec4a7838000

# 文档测试
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000

