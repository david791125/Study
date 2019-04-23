from pyecharts import Pie
import cx_Oracle as oracle
import os
#饼图
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

db = oracle.connect('apps/apps@193.168.42.68:1522/prod')

cursor = db.cursor ()

cursor.execute ("select ood.ORGANIZATION_NAME, count(*) count from mtl_system_items a,org_organization_definitions ood where a.ORGANIZATION_ID=ood.ORGANIZATION_ID group by ood.ORGANIZATION_NAME")

rows = cursor.fetchall()


pie =Pie("饼图示例")
attr, value  =pie.cast(rows)
pie.add("", attr, value, is_label_show=True)
pie.show_config()
pie.render("select_oravaluecle_pie.html")

cursor.close();

db.close();