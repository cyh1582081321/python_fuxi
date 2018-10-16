'''
定义一个NPC类，包含4个变量，第一个字段(变量)name保存名字，第二个变量jianjie保存NPC简介，第三个变量id保存npc的编号数值，
第四个用来保存可选NPC列表（kexuan），构造函数中初始化可选NPC列表信息。
'''
class Npc:
    jianjce = []
    def __init__(self,name,id,jianjie):
        self.id = id
        self.name  = name
        self.jianjie = jianjie
        self.str = self.id +"  "+ self.name +"  "+self.jianjie
        Npc.jianjce.append(self.str)