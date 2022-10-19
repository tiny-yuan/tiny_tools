from datetime import date
from unicodedata import name
import xlrd
import pymysql
class ERP:
    # msyql连接信息
    erp_ip = "192.168.2.23"
    erp_user = "zhanhl"
    erp_password = "zhanhl"
    erp_database = "erp"
    erp_port = 3306
    erp_charset ="utf8"
    #erp主物料编号
    sub_meterrial = 10010274
    def __init__(self,name):
        self.row_num = ""
        self.name = name
    def data(self):
        # 获取excel数据
        # 打开excel表格
        wordbook = xlrd.open_workbook('./ERP/bom_整机.xls')
        # 选择sheet页数
        sheet = wordbook.sheets()[3]
        # 输出总行数
        row_num = sheet.nrows
        self.row_num = int(row_num)
        # print("excel总行数为{}".format(row_num))
        # 输出总列数
        # col_num = sheet.ncols
        # print("excel总列数为{}".format(col_num))
        # 编辑msyql连接信息
        #创建sql语句存储的文件
        with open ("./ERP/sql.txt","w") as f:
        # 编写sql语句
            f.write("insert into erp.bom_item (main_meterial,sub_meterial,quantity,description) values ('10010274','10010023','1','中控整机'),('10010274','10010037','1','控制面板')\n")
            for i in range(1,row_num):
                        row_content = sheet.row_values(i)
                        print("insert into erp.bom_item (main_meterial,sub_meterial,quantity,description) values('{}','%.0f','%.0f','{}')".format(ERP.sub_meterrial,row_content[2])%(row_content[0],row_content[3]), file = f)
        with open('./ERP/sql.txt', 'r') as r:
            insert_sql = r.read()
            # print(insert_sql)

    def mysql(self):
            db = pymysql.connect(host=ERP.erp_ip,user=ERP.erp_user,database=ERP.erp_database,port=ERP.erp_port,charset=ERP.erp_charset,passwd=ERP.erp_password)
            # 创建游标对象
            cursor = db.cursor() 
            # sql删除语句
            del_sql = "delete from bom_item where main_meterial = '%s'" %ERP.sub_meterrial
            # print(del_sql)
            cursor.execute(del_sql)
            # 提交修改
            db.commit()
            success_num = 0
            false_num = 0
            # 逐行读取sql语句
            for line in open("./ERP/sql.txt"):
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
            print("bom表格总计数据{}条，导入成功{}条，导入失败{}条！".format(self.row_num - 1, success_num, false_num))
            cursor.close()
            db.close()


if __name__ == "__main__":
    erp1 = ERP("tiny")
    erp1.data()
