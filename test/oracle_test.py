import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import cx_Oracle as oracle

db = oracle.connect('apps/apps@193.168.42.68:1522/prod')

cursor = db.cursor ()

sql = "SELECT * FROM hr_operating_units"
cursor.execute(sql)
rows = cursor.fetchall() #得到所有数据集
for row in rows:
    print(row[0])
    print(row[1])
print("Number of rows returned: %d" % cursor.rowcount)

cursor.close ()
db.close ()