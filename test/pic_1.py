# -*- coding:utf-8 -*-
# 准备数据
import ggplot as gp # 不太喜欢import *
import pandas as pd
meat = gp.meat
p=gp.ggplot(gp.aes(x='date',y='beef'),data=meat)+gp.geom_point(color='red')+gp.ggtitle(u'散点图')
print(p)


