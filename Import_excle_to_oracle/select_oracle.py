import cx_Oracle as oracle
from pyecharts import Bar
import os
#柱状图/条形图
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
db = oracle.connect('apps/apps@193.168.42.68:1522/prod')

cursor = db.cursor ()

cursor.execute ("select a.organization_id,count(*) count from mtl_system_items a group by a.organization_id")

rows = cursor.fetchall()
print(rows)

bar = Bar("标记线和标记点示例")
attr, value  =bar.cast(rows)
bar.add("库存物料数量", attr, value)
bar.render("select_oracle.html")

cursor.close();

db.close();