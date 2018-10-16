class Person:

    #限制添加属性用的，赋的值是一个元组
    #如果在元组内没有写这个变量就不能用self去添加
    #强制添加会报错。下面代码就只能添加name和age
    __slots__ = ("name","age")
    def __init__(self):
        self.name=None
        self.age=None



p1=Person()
p1.name="aa"
p1.age=10

print(p1.name,p1.age)