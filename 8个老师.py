"""
8个老师放入3教shi：

"""
import random

#定义一个列表用来保存3办公室。

office  = [[],[],[]]

#定义一个列表用来存储8位老师

teachers = ['A','B','C','D','E','F','J','H']

#定义一个函数来保存来分配

for teacher in teachers:
    #随机抽取0 - 2 的整数集
    ix = random.randint(0,2)
    #将下标给办公室集合并将教师加入办公室
    office[ix].append(teacher)
print(office)
print(30*"-")
i = 1
# 遍历办公室的人数总和以及人名
for name in office:
    #以下标为办公室名称，列表长度为总人数
    print("办公室%d的人数：%d"%(i,len(name)))
    i+=1
    #进行内层遍历
    for tname in teacher:
          print('%s'%name, end='')
    print("\n")
    print("-"*20)
















