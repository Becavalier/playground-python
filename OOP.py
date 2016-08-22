#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This class inherit from "object" class
class Student(object):
    pass;

bart = Student();
bart;

bart.name = 'Bart Simpson';
bart.name;
# 'Bart Simpson'


class Student(object):
    # Constructor
    # The parameter "self" just like "this" in a class
    def __init__(self, name, score):
        self.name = name;
        self.score = score;


bart = Student('Bart Simpson', 59);
bart.name;
# 'Bart Simpson'
bart.score;
# 59


class Student(object):

    def __init__(self, name, score):
        self.name = name;
        self.score = score;

    def print_score(self):
        print('%s: %s' % (self.name, self.score));


# Access control

class Student(object):

    def __init__(self, name, score):
        # Private variables
        # _Student__name
        # _Student__score
        self.__name = name;
        self.__score = score;

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score));

    def get_name(self):
        return self.__name;

    def get_score(self):
        return self.__score;

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score;
        else:
            raise ValueError('bad score');


# Inheriance

class Animal(object):
    def run(self):
        print('Animal is running...');

class Dog(Animal):
    pass;

class Cat(Animal):
    pass;


dog = Dog();
dog.run();

cat = Cat();
cat.run();


class Dog(Animal):

    def run(self):
        print('Dog is running...');

    def eat(self):
        print('Eating meat...');


a = list();
b = Animal(); 
c = Dog();

isinstance(a, list);
# True
isinstance(b, Animal);
# True
isinstance(c, Dog);
# True
isinstance(c, Animal);
# True



# Determine the type of an object

type(123);
# <class 'int'>
type('str');
# <class 'str'>
type(None);
# <type(None) 'NoneType'>

import types
def fn():
    pass;

type(fn) == types.FunctionType;
# True
type(abs) == types.BuiltinFunctionType;
# True
type(lambda x: x) == types.LambdaType;
# True
type((x for x in range(10))) == types.GeneratorType;
# True


# 判断是不是某类型中的一种
isinstance([1, 2, 3], (list, tuple));
# True
isinstance((1, 2, 3), (list, tuple));
# True

# 获得一个对象的所有属性和方法
dir('ABC');



len('ABC');
# 3
'ABC'.__len__();
# 3


class MyDog(object):
    def __len__(self):
        return 100;

dog = MyDog();
len(dog);
# 100


class MyObject(object):
    def __init__(self):
        self.x = 9;
    def power(self):
        return self.x * self.x;

obj = MyObject();

hasattr(obj, 'x');
# True
obj.x;
# 9
hasattr(obj, 'y');
# False
setattr(obj, 'y', 19);
hasattr(obj, 'y');
# True
getattr(obj, 'y');
# 19
obj.y;
# 19
getattr(obj, 'z', 404);
# 404

hasattr(obj, 'power');
# True
getattr(obj, 'power');
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power');
fn 
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn()
# 81


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp);
    return None;

# Python鸭子类型


# Class attributes (static attributes/functions)

class Student(object):
    name = 'Student';

print(Student.name);
# Student

s.name = 'Michael';
del s.name;

