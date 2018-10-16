from npc.npc1 import Npc
from npc.player import Player
print("NPC可选：")
p1=Npc("阿尔萨斯","1","使用霜之哀伤攻击敌人")
p2=Npc("吉安娜","2","使用奥数法术远程攻击敌人")
p3=Npc("乌瑟尔","3","使用圣光力量治愈盟友")
for i in Npc.jianjce:
    print(i)
def fun():
    import sys
    p = Player()
    while  True:
        p.show()
        bh = input("请选择您进行的操作:")
        if bh == "1":
            p.add_npc()
        if bh == "2":
            p.del_npc()
        if bh == "o":
            sys.exit()
fun()