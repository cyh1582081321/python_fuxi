'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象，
    比如：list dict tuple都是
可以使用isinstace()去检测是否是可迭代对象iterable
可以直接作用于for的数据类型一般分为2种：
    1.集合
    2.generator，包括生成器和带yile的generator函数

'''
#在集合中倒入可迭代对象
from collections import Iterable
#在集合中倒入可迭代器
from collections import Iterator
#判断列表是不是可迭代对象
print(isinstance([],Iterable))
#判断元组是不是可迭代对象
print(isinstance((),Iterable))
#判断字典是不是可迭代对象
print(isinstance({},Iterable))
#判断字符串是不是可迭代对象
print(isinstance("",Iterable))
#判断 1 是不是可迭代对象
print(isinstance(1,Iterable))
'''
可以通过next()函数不断获取下一个元素，直到报错即为
获取完成，没有下一个元素了
列表、元组虽然是一个可迭代对象，但不是迭代器，需先转化

'''
#括号的作用相当于转了变量
l = (x for x in [23,56,89,54,564,2,3,26])
print(type(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

list1 = [1,2,3,45,6]
# 转化成可迭代对象
list_1 = iter(list1)
print(next(list_1))

'''
生成器

'''
def aaa(x):
    while True:
        x = x + 1
        #yield常见用法：该关键字用于函数中会把函数包装为generator。
        yield x

a = aaa(33)
print(next(a))
print(next(a))
print(next(a))
print(next(a))








