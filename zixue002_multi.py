#!usr/bin/python
#encoding:gbk

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" bdwater='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml('http://tieba.baidu.com/p/2198660859')
print getImg(html)

"""
from __future__ import division
##############
def jia(x,y):
    print x+y

def jian(x,y):
    print x-y

def cheng(x,y):
    print x*y

def chu(x,y):
    print x/y

def operator(a, o, b):
    if o == '+':
        jia(a,b)
    elif o == '-':
        jian(a,b)
    elif o == '*':
        cheng(a,b)
    elif o == '/':
        chu(a,b)
    else :
        pass

operator(4,'*', 2)
print jia

####################
####使用字典实现switch####
def jia(x,y):
    return x+y

def jian(x,y):
    return x-y

def cheng(x,y):
    return x*y

def chu(x,y):
    return x/y

print jia

operatot = {'+':jia, '-':jian, '*':cheng, '/':chu}

print operatot['+']
print jia(3,2)
print operatot['+'](3,2)

#print operatot['%']
#print operatot.get('%')(3,2)

def f(x, o, y):
    print operatot.get(o)(x,y)

f(3,'/',2)

print '################'
x = 3
y = 2
operatot = '/'
result = {
    '+': x+y,
    '-': x-y,
    '*': x*y,
    '/': x/y
    }

print result.get(operatot)

#########################
#def fun1(x):
#    if(x>5):
#        return True
fun1 = lambda x:x>5

l = range(10)

l1 = filter(fun1, l)
print 'hahaha'
print l1

##############################
#并行遍历
name = ['milo', 'zou', 'tom']
age = [1, 2, 3]
tel = ['12', '23', '34']
rel = zip(name, age, tel)
print rel

rel1 = map(None, name, age, tel)
print rel1

test = [1, 2]
rel3 = zip(name, age, tel, test)
print rel3
rel4 = map(None, age, tel, test)
print rel4

a = [1,2,3]
b = [2,3,4]
def mf(x,y):
    return x*y

rel5 = map(None, a, b)
print rel5

rel6 = map(mf, a, b)
print rel6

ll = range(4)
print ll
#def bf(x,y):
#   return x+y
bf = lambda x,y:x+y
oo = reduce(bf, ll)
print oo
"""



