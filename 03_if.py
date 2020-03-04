age = input("输入你的年龄")
#所有字符都是数字，为真返回 Ture，否则返回 False。
if age.isdigit() == True:
    age = int(age)
    if age >= 18:
        print("可以进入")
    else:
        print("不可以进入")
else:
    print("请输入数字")