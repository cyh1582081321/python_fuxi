'''
静态方法：当函数不需要使用self点的一些东西的就给他编程静态函数
          在调用的时候通过类名直接调用
          如果加了staticmethod这个装饰器之后，可以无视self，将这个方法当作普通的函数
          来使用
类方法：classmethod 第一个参数不是self,是cls，他代表类本身
实例（对象）方法：第一次参数是self ， 代表实例本身

         实例方法只能被实例调用，静态方法和类方法可以被类和类的实例调用

'''
class Cat:
    age = 10
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃饭",self.name)
        print(Cat.age)

    @staticmethod
    def fun1():
        print("很深刻，很像你")
    @classmethod
    def fun2(cls):
        print(cls.age)
c = Cat("a")
print(c.name)
c.eat()
Cat.fun1()
Cat.fun2()
