#电脑随机出拳
#利用import导入模块
import random

computer = random.randint(1,3)
player =  input("请出拳，石头1剪刀2布3")
#石头1剪刀2布3

if player.isdigit() == True:
    player = int(player)
    if player > 3 or player < 1:
        print("哪来的%d?" % player)
    elif(
        (player == 1 and computer == 2)
        or(player == 2 and computer ==3)
        or(player == 3 and computer == 1)
    ):

        print("You Win!")
    elif player == computer:
        print("平局！")
    else:
        print("GG!")
else:
    print("请输入数字")
print("你出的是%d，电脑出的是%d" % (player,computer))

