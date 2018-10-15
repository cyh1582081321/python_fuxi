'''
九九乘法表

'''
#方法一：

i = 1
sum = 0
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d\t'%(i,j, i*j),end='')
        j+= 1
    i+= 1
    print()

#方法二：
print(20*"*")
for i in range(1,10):
    for j in range(1,i+1):
       print('%d*%d=%d\t'%(i,j, i*j),end='')
    print()
       
