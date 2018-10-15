'''
请输入5个数排序！

'''
arr = input('请输入5个数，以逗号隔开：')

list_ = arr.split(",")

print(list_)

#转变为 int 类型的参数：

i = 0
list_1 = []
while i < 5:
     a = int(list_[i])
     list_1.append(a)
     i  += 1
print(list_1)
#最原始的方法一:
print(sorted(list_1))
