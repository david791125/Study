from threading import Timer
from wxpy import *
import requests

bot = Bot()  # 连接微信,会出现一个登陆微信的二维码

my_friend = bot.friends().search(u'Joy')[0]  # 这里是你微信好友的昵称
my_friend.send(u'广东欢迎你！')