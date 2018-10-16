from npc.npc_ import Npc
from npc.player_ import Player
def fun():
    npc1 = Npc()
    player = Player()
    while True:
        print("*********************************************")
        print("*********************************************")
        import sys
        npc1.show()
        bh=input("请输入编号：")
        if bh=="1":
            player.add()
        if bh=="2":
            player.del1()
        if bh=="o":
            sys.exit()



fun()