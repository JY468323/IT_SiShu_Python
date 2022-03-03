#-*- codeing = utf-8 -*-
#@Time:2022/2/25 15:00
#@Author:张佳源
#@File:error.py
#@Sofeware:PyCharm


#捕获异常
'''
try:
    print("-----------test---1=====")
    f = open("123.txt","r") #用只读模式打开了一个不存在的文件，报错
    print("-----------test---2=====")  #这句代码不会被执行
except IOError:   #文件没找到，属于IO异常
    pass   #捕获异常后，执行的代码
'''

'''
try:
    print("-----------test---1=====")
    f = open("test1.txt", "r")  # 用只读模式打开了一个不存在的文件，报错
    print("-----------test---2=====")
    print(num)
except (NameError,IOError):   #将可能产生的所有异常类型，都放在下面的小括号中
    print("产生错误了")
'''

#获取错误描述
'''
try:
    print("-----------test---1=====")
    f = open("123.txt", "r")  # 用只读模式打开了一个不存在的文件，报错
    print("-----------test---2=====")
    print(num)
except (NameError,IOError) as result:   #将可能产生的所有异常类型，都放在下面的小括号中
    print("产生错误了")
    print(result)
'''


#捕获所有的异常
'''
try:
    print("-----------test---1=====")
    f = open("test1.txt", "r")  # 用只读模式打开了一个不存在的文件，报错
    print("-----------test---2=====")
    print(num)
except Exception as result:   #将可能产生的所有异常类型，都放在下面的小括号中
    print("产生错误了")
    print(result)
'''
'''
import time
# try   finally  和嵌套
try:
    f = open("test1.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")
# finally:
#     f.close()
#     print("文件关闭")
'''


# 作业：
# 1. 应用文件操作的相关知识，通过Python新建一个文件gushi.txt，选择一首古诗写入文件中
# 2. 另外写一个函数，读取指定文件gushi.txt，将内容复制到copy.txt中，并在控制台输出“复制完
# 毕”。
# 3. 提示：分别定义两个函数，完成读文件和写文件的操作
# 尽可能完善代码，添加异常处理。


def writePoem():
    f = open("gushi.txt", "w",encoding="utf-8")
    f.write(input("请输入古诗："))
    f.close()
def copyPoem():
    f = open("gushi.txt","r",encoding="utf-8")
    c = open("copy.txt","w",encoding="utf-8")
    content = f.readlines()
    for i in content:
        c.write(i)
    c.close()
    f.close()
writePoem()
copyPoem()