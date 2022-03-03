#-*- codeing = utf-8 -*-
#@Time:2022/2/23 17:44
#@Author:张佳源
#@File:demo6.py
#@Sofeware:PyCharm

#namelist = [] #定义一个空的列表
namelist = ["小张","小王","小李"]
testlist = [1,"测试"]     #列表可以存储混合类型
'''
print(type(testlist[0]))
print(type(testlist[1]))
print(namelist[0])
print(namelist[1])
print(namelist[2])
'''
'''
for name in namelist:
    print(name)

length = len(namelist)
i = 0
while i < length:
    print(namelist[i])
    i += 1
'''
'''
#增： [append]
print("-----增加前，列表的数据-----")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名：")
namelist.append(nametemp)

print("-----增加后，列表的数据-----")
for name in namelist:
    print(name)
'''

'''
a = [1,2]
b = [3,4]
a.append(b)  #将列表当作一个元素，加入a列表中
print(a)

a.extend(b) #将b列表中的每个元素，逐一追加到a列表中
print(a)
'''
'''
#增： [insert]

a = [0,1,2]
a.insert(1,3)       #第一个变量表示下标，第二个表示元素(对象)
print(a)            #指定下标位置插入元素
'''

'''
#删： [del] [pop] [remove]

moviename = ["加勒比海盗","黑客帝国","第一滴血","指环王","速度与激情","指环王"]
print("-----删除前，列表的数据-----")
for name in moviename:
    print(name)

#del moviename[2]   #在指定位置删除一个元素
#moviename.pop()     #弹出末尾最后一个元素
moviename.remove("指环王")  #直接删除指定内容的数据
print("-----删除后，列表的数据-----")
for name in moviename:
    print(name)
'''

#改：
'''
print("-----修改前，列表的数据-----")
for name in namelist:
    print(name)
namelist[1] = "小红"

print("-----修改后，列表的数据-----")
for name in namelist:
    print(name)
'''

#查 ： [in . not in]
'''
findName = input("请输入你要查找的学生姓名：")

if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")
'''

'''
mylist = ["a","b","c","a","b"]

print(mylist.index("a",1,4))   #可以查找指定下标范围的元素，并返回找到对应数据的下标

print(mylist.index("a",1,3))   #范围区间，左闭右开  [1,3)
                               #找不到会报错

print(mylist.count("c"))   #统计某个元素出现几次
'''

#排序和反转
'''
a = [1,4,2,3]
print(a)

a.reverse()  #将列表所有元素反转
print(a)

a.sort()   #升序
print(a)

a.sort(reverse=True)  #降序
print(a)
'''

#schoolNames = [[],[],[]]
'''
schoolName = [["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学"]]
print(schoolName[0][0])
'''

'''
import random

offices = [[],[],[]]

names = ["A","B","C","D","E","F","G","H"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
'''
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("----- 所有商品列表 -----")
for i in range(0,len(products)):
    print(i,products[i][0],products[i][1],end="\n")
bag = []
money = []
i = 1
while i < 7 :
    que1 = int(input("请输入想要购买的商品编号:"))
    bag.append(products[que1])
    i = i + 1
    que2 = input("是否继续选购:")
    if que2 == "是":
        continue
    else:
        print("您购买的商品列表如下:")
        for i in range(0, len(bag)):
            print(i, bag[i][0], bag[i][1], end="\n")
            money.append(bag[i][1])
            sum_m = sum(money)
        print("总金额为%d,欢迎下次光临!"%sum_m)
        break