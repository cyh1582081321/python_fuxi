class Npc:
    def __init__(self):
        self.a={1:"阿尔萨斯   使用霜之哀伤攻击敌人",
                2:"吉安娜    使用奥数法术远程攻击敌人",
                3:"乌瑟尔     使用圣光力量治愈盟友"}
    def show(self):
        print("NPC可选：")
        for i,j in self.a.items():
            print(i,j)
        print("请选择您进行的操作")
        print("1.邀请组队")
        print("2.踢出队伍")
        print("o.完成")
