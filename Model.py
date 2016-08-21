#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 所有.py文件的第一行字符串都是注释
' a test module '

# 记录该文件作者名字
__author__ = 'Michael Liao'

import sys;

def test():

    # sys.argv的第一个参数为当前py文件的名字，从第二个参数开始取传入的参数
    args = sys.argv;
    if len(args) == 1:
            print('Hello, world!');
    elif len(args) == 2:
        # print函数里用“%”分割参数
        print('Hello, %s!' % args[1]);
    else:
        print('Too many arguments!');

# 判断是否是从该文件开始执行
if __name__ == '__main__':
    test();


# Define private methods
def _private_1(name):
    return 'Hello, %s' % name;

def _private_2(name):
    return 'Hi, %s' % name;

def greeting(name):
    if len(name) > 3:
        return _private_1(name);
    else:
        return _private_2(name);


# 模块搜索路径
import sys;
sys.path;

