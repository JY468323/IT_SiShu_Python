#-*- codeing = utf-8 -*-
#@Time:2022/2/24 16:26
#@Author:张佳源
#@File:def.py
#@Sofeware:PyCharm

'''
#函数定义
def printinfo():
    print("----------------------")
    print("  人生苦短，我用python  ")
    print("----------------------")

#函数调用
printinfo()
'''

#带参数的函数
'''
def add2Num(a,b):
    c = a + b
    print(c)

add2Num(11,22)
'''

#带返回值的参数
'''
def add2Num(a,b):
    return a+b
result = add2Num(11,22)
print(result)
'''

#返回多个值的函数
'''
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu

sh,yu = divid(5,2)   #需要返回多个值

print("商：%d，余数：%d"%(sh,yu))
'''

#全局变量和局部变量

'''
def test1():
    a = 300
    print("test1-------修改前：a=%d"%a)
    a = 100
    print("test1-------修改后：a=%d"%a)
def test2():
    a = 500
    print("test2-------a=%d"%a)

test1()
test2()
'''
'''
a = 100 #全局变量
def test1():
    print(a)
def test2():
    print(a)

test1()
test2()
'''
'''
a = 100
def test1():
    a = 300
    print("test1-------修改前：a=%d"%a)
    a = 100
    print("test1-------修改后：a=%d"%a)
def test2():
    print("test2-------a=%d"%a)  #没有局部变量，默认使用全局变量

test1()
test2()
'''
a = 100
def test1():
    global a    #声明全局变量在函数中的标识符
    print("test1-------修改前：a=%d"%a)
    a = 200
    print("test1-------修改后：a=%d"%a)
def test2():
    print("test2-------a=%d"%a)  #没有局部变量，默认使用全局变量

test1()
test2()