# -*- coding:utf-8 -*-
import math
import string
from functools import reduce

n1 = 255
n2 = 1000
hex_n1 = hex(n1)
hex_n2 = hex(n2)
print('n1的hex：', hex_n1)
print('n2-hex:', hex_n2)


def my_sum(num1, num2):
    sum = num1 + num2
    return sum


print('two number sum is:', my_sum(n1, n2))

'''x = math.sqrt(100)
print('x:', int(x))
'''


def x_n(x, n):
    num = 1
    if n >= 0:
        while n > 0:
            num = num * x
            n = n - 1
        return num
    if n < 0:
        n = abs(n)
        while n > 0:
            num = num * x
            n = n - 1
        return 1 / num


print(x_n(100, 2))

'''
def mov(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        mov(n - 1, a, c, b)
        mov(1, a, b, c)
        mov(n - 1, b, a, c)


mov(3, 'A', 'B', 'C')


print('input string:')
str = input()
'''


def trim(s):
    strNumber = len(s)
    start = 0
    if s[0:1] == ' ':
        s = s[1:]
        trim(s)
    elif s[-1:] == ' ':
        s = s[:-1]
        trim(s)

    return s


# print('output:', trim(str))


def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


l = 'chen'
print(findMinAndMax(l))

L1 = ['hello', 'world', 18, 'apple']
L2 = []
for i in L1:
    if isinstance(i, type(str)):
        L2.append(i)
# L2 = [i.lower() for i in L1 if isinstance(i,str)]
print(L2)


def triangles(max):
    b = [1, ]
    for n in range(max):
        max += 1
        yield b
        c = []
        for i in range(n + 1):
            if i < n:
                c += [b[i] + b[i + 1]]
        b = [1, ] + c + [1, ]
    return 'done'


'''
for x in triangles(100):
    print(x)
'''

'''
def f(x):
    return x * x


r = map(float, [0, 1, 2, 3])
print(list(r))


def f(x, y):
    return x + y


r =  reduce(f, [0, 1, 2, 3])
print(r)
'''
def normalize(name):
    length = len(name)
    l1 = []
    for k in range(length):
        l1.append( name[k][0].upper() + name[k][1:].lower())
    return l1

print( normalize(['jioNFJK','HJHDjhe','sdlkrgjlJ']))

def odd_fliter():
    n = 3
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = odd_fliter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break

l = 9845234
l = str(l)
print(l[::-1])

class Student(object):
    def __init__(self,name,score):  # 此处需要两个下划线
        self.name = name
        self.__score = score

    def printScore(self):
        print('%s:%s'%(self.name,self.__score))
    def getScore(self):
        return self.__score
    def setScore(self,score):
        self.__score = score

bart = Student('deffand',99)
print(bart.getScore())
bart.setScore(100)
print(bart.getScore())
