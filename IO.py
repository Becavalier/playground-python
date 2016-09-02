#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('/user/test.txt', 'r');
# Read all
f.read();
f.close();

try:
    f = open('/user/test.txt', 'r');
    print(f.read());
except IOError as e:
    print(e);
finally:
    if f:
        f.close();


with open('/user/test.txt', 'r') as f:
    print(f.read());

with open('/user/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip());

with open('/user/test.txt', 'r') as f:
    print(f.readline());

# 打开二进制文件用 'rb'
f = open('/Users/michael/test.jpg', 'rb');
f.read();

# 读取GBK编码文件
f = open('/user/gbk.txt', 'r', encoding = 'gbk');
f.read();

f = open('/user/gbk.txt', 'r', encoding = 'gbk', errors = 'ignore');
f.read();


# 写文件
f = open('/user/test.txt', 'w');
f.write("Hello");
f.close();

with open('/user/test.txt', 'w') as f:
    f.write("Hello");

with open('/user/test.txt', 'w', encoding = 'gbk') as f:
    f.write("GBK");


# StringIO and BytesIO (在内存中读写)
from io import StringIO;
f = StringIO();
f.write("hello");
f.write('');
print(f.getvalue());
# hello 

from io import StringIO;
f = StringIO('Hello!\nHi!\nGoodbye!');
while True:
    s = f.readline();
    if s = '':
        break;
    print(s.strip());


from io import BytesIO;
f = BytesIO();
f.write('中文'.encode('utf-8'));

print(f.getvalue());
# b'\xe4\xb8\xad\xe6\x96\x87'

from io import StringIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
# b'\xe4\xb8\xad\xe6\x96\x87'


import os;
os.name;

# 'posix' - 类Unix系统, 'nt' - windows系统

os.uname();
# posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

os.environ;
# environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})

os.environ.get('PATH');
# '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
os.environ.get('x', 'default');
# 'default'

# 操作文件和目录
os.path.abspath(".");
# '/Users/michael'
os.path.join('/Users/michael', 'testdir');
# '/Users/michael/testdir'
os.mkdir('/Users/michael/testdir');
os.rmdir('/Users/michael/testdir');

os.mkdir(os.path.join(os.path.abspath("."), 'newdir'));

os.path.split('/Users/michael/testdir/file.txt');
# ('/Users/michael/testdir', 'file.txt')

os.path.splitext('/path/to/file.txt');
# ('/path/to/file', '.txt')

# 对文件重命名:
os.rename('test.txt', 'test.py');
# 删掉文件:
os.remove('test.py');

[x for x in os.listdir('.') if os.path.isdir(x)];
# ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]


[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'];
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']


# pickling
import pickle;
d = dict(name = 'bob', age = 20, score = 85);
pickle.dumps(d);
# b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

f = open('dump.txt', 'wb');
pickle.dump(d, f);
f.close();

f = open('dump.txt', 'rb');
d = pickle.load(f);
f.close();
d
# {'age': 20, 'score': 88, 'name': 'Bob'}

import json;
d = dict(name = 'Bob', age = 20, score = 88);
json.dumps(d);
# '{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}';
json.loads(json_str);
# {'age': 20, 'score': 88, 'name': 'Bob'}



def dict2student(d):
    return Student(d['name'], d['age'], d['score']);


json_str = '{"age": 20, "score": 88, "name": "Bob"}';
print(json.loads(json_str, object_hook = dict2student));

class Student(object):
    def __init__(self, name, age, score):
        self.name = name;
        self.age = age;
        self.score = score;

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default = student2dict));
print(json.dumps(s, default = lambda obj: obj.__dict__));