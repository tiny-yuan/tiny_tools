from dataclasses import dataclass
from email import charset
from multiprocessing.sharedctypes import Value
import sqlite3
import pymysql
# 编辑msyql连接信息
erp_ip = "192.168.2.23"
erp_user = "zhanhl"
erp_password = "zhanhl"
erp_database = "erp"
erp_port = 3306
erp_charset ="utf8"
# 打开数据库连接
db = pymysql.connect(host=erp_ip,user=erp_user,database=erp_database,port=erp_port,charset=erp_charset,passwd=erp_password)
# 创建游标对象
cursor = db.cursor()
# 插入
# sql = "insert into bom_item (main_meterial,sub_meterial,quantity,description) values('10010024','10010036','100','test')"
# 查询
# sql = "SELECT * FROM erp.bom_item"
# 删除
sql = "delete from bom_item where sub_meterial ='10010036'"
# info = cursor.execute(sql)
# for i in range(info):
#     print(cursor.fetchone())
cursor.execute(sql)
db.commit()
cursor.close()
db.close()