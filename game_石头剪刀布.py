#!/usr/bin/python
# coding=utf-8

# 石头剪刀布游戏
import random

# 游戏规则
winlist = (['石头', '剪刀'], ['剪刀', '布'], ['布', '石头'])
choicelist = ('石头', '剪刀', '布')
prompt = '''可选项如下
(0)石头
(1)剪刀
(2)布
(3)退出
请输入你的选择(输入数字即可)'''

while True:
     choicenum = int(raw_input(prompt))  # 用户选择数字
     if choicenum == 3:
          print '退出'
     userchoice = choicelist[choicenum]#用户选择数字,从选择列表中拿出字符
     comchoice =random.choice(choicelist)
     bothchoice = [userchoice, comchoice]
     print '你选择了  %s , 计算机选择了 %s ' % (userchoice, comchoice)
     if userchoice == comchoice:
          print '平局'
     elif bothchoice in winlist:
          print '你赢了'
     else:
          print '你输了'



