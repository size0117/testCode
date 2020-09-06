

username = input("ID：")
password = input("password:")
if len(username) >5 and len(username) <8:
    if username =="张三12345" and password =="123456":
        print("登陆成功")
    else:
        print("登陆失败")
else:
    print("登陆失败")