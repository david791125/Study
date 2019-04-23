from pyecharts import Pie
from pyecharts import Bar
from pyecharts import Page
import cx_Oracle as oracle
import os
#饼图
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

db = oracle.connect('apps/apps@193.168.42.68:1522/prod')

cursor = db.cursor ()

cursor.execute ("select a.organization_id,count(*) count from mtl_system_items a group by a.organization_id")

rows = cursor.fetchall()

page = Page()         # step 1

bar = Bar("标记线和标记点示例")
attr, value  =bar.cast(rows)
bar.add("库存物料数量", attr, value)
page.add(bar)

pie =Pie("饼图示例")
attr, value  =pie.cast(rows)
pie.add("库存物料数量", attr, value, is_label_show=True)

page.add(pie)

page.render("pic_merge.html")

cursor.close();

db.close();