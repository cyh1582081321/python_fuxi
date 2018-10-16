'''
定义一个玩家类,包含三个方法和一个变量，一个构造函数，变量用来保存当前队伍中的NPC信息dangqian，第一个方法为增加NPC方法，
包含一个id参数，通过循环匹配npc类中的kexuan元素id，当找到ID一致的对象时，将对象加入dangqian。第二个方法删除NPC方法，
通过循环匹配npc类中的kexuan元素id，当找到ID一致的对象时，将对象从dangqian中删除，第三个方法为输出列表方法，
循环输出dangqain中的内容。
'''

from npc.npc1 import Npc

class Player:
    def __init__(self):
        self.dangqian = []
    def add_npc(self):
        id = input("请输入你要增加的队伍信息id:")
        if id == "1" :
            self.dangqian.append(Npc.jianjce[0])
        if id == "2" :
            self.dangqian.append(Npc.jianjce[1])
        if id == "3" :
            self.dangqian.append(Npc.jianjce[2])
        print("当前队伍的信息：",self.dangqian)
    def del_npc(self):
        print("当前队伍的信息：", self.dangqian)
        id = input('请输入你要删除的队伍信息id:')
        if id == "1":
            self.dangqian.pop(0)
        if id == "2":
            self.dangqian.pop(1)
        if id == "3":
            self.dangqian.pop(2)
        print("当前队伍的信息：", self.dangqian)

    def show(self):
        print("1.邀请组队")
        print("2.踢出队伍")
        print("o.完成")
        for i in self.dangqian:
            print(i)