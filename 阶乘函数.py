'''
用递归求阶乘
'''
def jiechen(a):
    #程序出口
    if a == 1:
        return 1
    else:
        return a * jiechen(a-1)
print(jiechen(5))
print(1*2*3*5*4)
