#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass;

s = Student();

s.name = "Jony";
print(s.name);
# Jony

def set_age(self, age):
    self.age = age;

from types import MethodType;
# 将方法绑定在实例上，但其他实例并不能共享
s.set_age = MethodType(set_age, s);
s.set_age(25);
s.age;
# 25

# 将方法绑定在类上，所有其他实例均共享
Student.set_age = set_age;




class Student(object):

    def set_age(self, age):
        self.age = age;



# 使用 __slots__ 限制可以给类添加的属性（仅对当前类实例起作用，继承类不作用）

class Student(object):
    __slots__ = ("name", "age");

s = Student();
s.name = "Michale";
s.score = 90;
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'



class Student(object):
    def get_score(sefl):
        return self._score;

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!');
        else if value < 0 or value > 100：
            raise ValueError('score must between 0 ~ 100!');

        self._score = score;


class Student(object):
    @property
    def score(self):
        return self._score;

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!');
        else if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!');

        self._score = score;


class Student(object):
    @property
    def birth(self):
        return self._birth;

    @birth.setter
    def birth(self, value):
        self._birth = value;

    @property
    def age(self):
        return 2016 - self._birth;


class Student(object):
    @def foo():
        doc = "The foo property."
        def fget(self):
            return self._foo
        def fset(self, value):
            self._foo = value
        def fdel(self):
            del self._foo
        return locals()
    foo = property(**foo())



# Multi Inheritence (MixIn)

# 多进程模式的TCP服务
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

# 多线程模式的UDP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass



class A:  
    def method(self, arg):    
        pass;
  
class B(A):  
    def method(self, arg):  
        A.method(self,arg);            # 1  
        super(B, self).method(arg);    # 2  
        super().method(arg);


class Student(object):
    def __init__(self, name):
        self.name = name;

print(Student('Michale'));
# <__main__.Student object at 0x109afb190>


class Student(object):
    def __init__(self, name):
        self.name = name;

    def __str__(self):
        return 'Student object (name: %s)' % self.name;

    __repr__ = __str__;

print(Student("Jony"));
# Student object (name: Jony)
a = Student("Michale");
a
# Student object (name: Michale)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1;

    def __iter__(self):
        return self;

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b;
        if self.a > 10000:
            raise StopIteration();
        return self.a;

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1;
            for x in range(n):
                a, b = b, a + b;
            return a;
        if isinstance(n, slice):
            start = n.start;
            stop = n.stop;
            if start is None:
                start = 0;
            a, b = 1, 1;
            L = [];
            for x in range(stop):
                if x >= start:
                    L.append(a);
                a, b = b, a + b;
            return L;
        # 访问该类没有的属性或方法时会调用该方法
        def __getattr__(self, attr):
            if attr == "age":
                return lambda: 25;
            if attr == "score":
                return 99;
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr);

for n in Fib():
    print(n);
# ...
Fib()[5];
# ...

list(range(100))[5:10];
# [5, 6, 7, 8, 9]

class Chain(object):
    def __init__(self):
        self._path = path;

    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path));

    def __str__(self):
        return self._path;

    __repr__ = __str__;

Chain().status.user.timeline.list
# '/status/user/timeline/list'

class Student(object):
    def __init__(self, name):
        self.name = name;

    def __call__(self):
        print('My name is %s.' % self.name);

a = Student("Jony");
a();
# My name is Jony

callable(Student());
# True
callable(max);
# True
callable([1, 2, 3]);
# False
callable(None);
# False
callable('str');
# False



# Enum Class
JAN = 1;

from enum import Enum;
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value);


from enum import Enum, unique;

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Tue.value);
# 2

# hello.py
class Hello(object):
    def hello(self, name = "world"):
        print("Hello, %s." % name);

from hello import Hello;
h = Hello();
h.hello();
print(type(Hello));
# <class 'type'>
print(type(h));
# <class 'hello.Hello'>


def fn(self, name = 'world'):
    print("Hello, %s." % name);

# Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class.
Hello = type('Hello', (object,), dict(hello = fn));
h = Hello();
h.hello();
# Hello, world.



# metaclass 先定义metaclass，就可以创建类，最后创建实例。
# metaclass 是类的模板，所以从 type 类型派生
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
class ListMetaClass(type):
    #__new__()方法接收到的参数依次是:
    #
    # 1\当前准备创建的类的对象；
    # 2\类的名字；
    # 3\类继承的父类集合；
    # 4\类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value);
        return type.__new__(cls, name, bases, attrs);

class MyList(list, metaclass = ListMetaClass):
    pass;


