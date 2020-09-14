"""
i = 10
while i > 1 :
    print(i)
    i = i - 1


a = 0      #chengji的下标
chengji = [80,60,59,29,99]
while a < len(chengji):   #成绩
    if chengji[a] < 60:
        print("不合格，成绩是：{}".format(chengji[a]))

    #判断成绩
    
    a = a + 1#如果成绩不合格就打印
"""

a = 60
while 0 < a < 61:
    if a < 61 and a > 55:
        print("黄灯")
    if a < 56 and a > 35:
        print("绿灯")
    if a < 36 and a > 0:
        print("红灯")
    a = a - 1
    