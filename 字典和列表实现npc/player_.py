from npc.npc_ import Npc
class Player:
    def __init__(self):
        self.dangqian={}
    def  add(self):
        d=int(input("邀请组队："))
        z=Npc()
        f=z.a[d]
        self.dangqian[d]=f
        print("当前队伍NPC：")
        for i,j  in self.dangqian.items():
            print(i,j)
    def del1(self):
        for i,j  in self.dangqian.items():
            print(i,j)
        c=int(input("当前要踢队伍："))
        self.dangqian.pop(c)

