#-*- codeing = utf-8 -*-
#@Time:2022/1/23 16:20
#@Author:张佳源
#@File:demo3.py
#@Sofeware:PyCharm
'''
if False:
    print("True")
else:
    print("False")
'''
'''
score = 67

if score >= 90 and score <= 100:
    print("本次考试，等级为A")
elif score >= 80 and score < 90:
    print("本次考试，等级为B")
elif score >= 70 and score < 80:
    print("本次考试，等级为C")
elif score >= 60 and score < 70:
    print("本次考试，等级为D")
else:                 #else和elif一起使用
    print("本次考试，等级为E")
'''
'''
xingBie = 1 # 1代表男生，0代表女生
danShen = 1 # 1代表单身，0代表有男/女朋友

if xingBie == 1:
    print("男生")
    if danShen == 1:
        print("我给你介绍一个吧")
    else:
        print("你给我介绍一个吧")
else:
    print("女生")
    print("...")
'''

'''
import random

in_put = int(input("请输入：剪刀(0)、石头(1)、布(2):"))
print("你的输入为：%d"%in_put)
randomnum = random.randint(0,2)
print("随机生成数字为:%d"%randomnum)
if (in_put == 0 and randomnum == 0) or (in_put == 1 and randomnum == 1) or (in_put == 2 and randomnum == 2):
    print("平局，再来一次吧",end="")
elif(in_put == 0 and randomnum == 1) or (in_put == 1 and randomnum == 2) or (in_put == 2 and randomnum == 0):
    print("哈哈，你输了",end="")
else:
    print("恭喜，你赢了",end="")
'''
