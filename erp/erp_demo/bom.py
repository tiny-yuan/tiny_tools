from ast import Num
from dataclasses import dataclass
from email import charset
import sqlite3
import pymysql
import xlrd
# 获取excel数据
# 打开excel表格
wordbook = xlrd.open_workbook('bom.xls')
# 选择sheet页数
sheet = wordbook.sheets()[0]
# 输出总行数
row_num = sheet.nrows
row_num = int(row_num)
# print("excel总行数为{}".format(row_num))
# 输出总列数
col_num = sheet.ncols
# print("excel总列数为{}".format(col_num))
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
# 确定主物料
sub_meterrial = 10010052
# sql删除语句
del_sql = "delete from bom_item where main_meterial = '%s'" %sub_meterrial 
# print(del_sql)
cursor.execute(del_sql)
# 提交修改
db.commit()
#创建sql语句存储的文件
with open ("sql.txt","w") as f:
# 编写sql语句
    for i in range(1,row_num):
                row_content = sheet.row_values(i)
                print("insert into erp.bom_item (main_meterial,sub_meterial,quantity,description) values('{}','%.0f','%.0f','{}')".format(sub_meterrial,row_content[4]) %(row_content[1],row_content[3]), file = f)
# with open('sql.txt','r') as r:
#     insert_sql = r.read()
success_num = 0
false_num = 0
for line in open("sql.txt"):
    insert_sql = line
# print(insert_sql)
    try:
        # 执行sql语句
        cursor.execute(insert_sql)
        # 提交修改
        db.commit()
        success_num += 1
        # print('bom导入成功！')
    except:
        # 发生错误时回滚
        db.rollback()
        false_num += 1
        print('语句错误，已经完成回滚！')
print("bom表格总计数据{}条，导入成功{}条，导入失败{}条！".format(row_num -1,success_num,false_num))
# sql = "SELECT * FROM erp.bom_item"
# 使用execute()方法执行SQL
# info = cursor.execute(sql)
# for i in range(info):
#     print(cursor.fetchone())
# # print(info)
cursor.close()
db.close()