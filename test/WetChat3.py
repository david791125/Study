from wxpy import *

bot = Bot()  # 连接微信,会出现一个登陆微信的二维码

my_group = bot.groups().search('顺德美食')[0]
my_group.send('')