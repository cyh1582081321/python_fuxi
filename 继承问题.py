"""
子承父业
继承好处：
       1.减少代码量，不用自己在写了
继承的应用场景：
       1.多个类出现相同代码
       2.满足is  a 满足谁是谁的一种条件
子类拥有的功能多于父类
子类（派生类）
父类：（基类 ）（超类）
间接继承：比如儿子的儿子bisicat于animal也叫多重继承
继承多个类，这种现象叫多继承

"""
class Person:
'''
  构造函数无参的
  子类也必须调用父亲的构造函数
  构造函数有参数的情况
  子类必须给父亲构造函数赋值

'''
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def study(self):
        print("每个人都在学习~~！！")
class Student(Person):
    #构造方法中必须将父级所需要继承的属性都写上
    def __init__(self,score,name,age,sex):
        
        #继承方法有两种：
        #方法一：
        super(Student, self).__init__(name,age,sex)
        #2.person.__init__(self,name,age)
        self.score = score
        print(name, age, score)
s1=Student("张三",15,'男',99)
