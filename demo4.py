#-*- codeing = utf-8 -*-
#@Time:2022/1/23 19:35
#@Author:张佳源
#@File:demo4.py
#@Sofeware:PyCharm

'''
for i in range(10):
    print(i,end=" ")
'''
 
'''
for i in range(0,10,3):
    print(i,end=" ")
'''

'''
for i in range(-10,-100,-30):
    print(i,end=" ")
'''

'''
name = "chengdu"

for x in name:
    print(x,end=" ")
'''

'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''

'''
i = 0
while i < 5 :
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i += 1
'''

'''
ans = 0
i = 1
while i <= 100 :
    ans = ans + i
    i += 1
print("1到 %d 的和为: %d"%(i,ans))
'''

'''
count = 0
while count < 5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于或等于5")
'''

'''
i = 0
while i < 10:
    i = i + 1
    print("-"*30)
    if i==5:
        break
    print(i)
'''

'''
i = 0
while i < 10:
    i = i + 1
    print("-"*30)
    if i==5:
        continue   #结束本次循环
    print(i)
'''

for i in range(1,10):
    for j in range(1,10):
        if(i<j):
            continue
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print("\n")
