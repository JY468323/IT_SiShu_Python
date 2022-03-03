#-*- codeing = utf-8 -*-
#@Time:2022/2/24 11:35
#@Author:张佳源
#@File:Tuple.py
#@Sofeware:PyCharm

'''
tup1 = ()  #创建空的元组
print(type(tup1))

# tup2 = (50)  #<class 'int'>
#tup2 = (50,)
tup2 = (50,60,70)
print(type(tup2))
'''

'''
tup1 = ("abc","def",2000,2020)

print(tup1[0])
print(tup1[-1])
print(tup1[1:5])  #左闭右开，进行切片
'''

#增  （连接）
'''
tup1 = (12,34,56)
tup2 = ("abc","xyz")

tup = tup1 + tup2
print(tup)
'''

#删
'''
tup1 = (12,34,56)
print(tup1)
del tup1   #删除了整个元组变量
print("删除后：")
print(tup1)
'''

#改
'''
tup1 = (12,34,56)

tup1[0] = 100  #报错，不能修改
'''

#查