import xlrd # 读excel数据的模块

# 打开excel表格
workbook = xlrd.open_workbook("bom.xlsx")
# 选择页数为第一页
sheet = workbook.sheets()[0]
# 数据总行数
row_num = sheet.nrows
print('数据总行数：',row_num)
# 获取列数
clo_num = sheet.ncols
print('表格总列数',clo_num)
#创建sql语句存储的文件
with open ("sql.txt","w") as f:
    # 输出所有的内容
    for i in range(1,row_num):
        # 赋值bom的主物料编号
        sub_meterrial = 10010024
        row_content = sheet.row_values(i)
        # print(row_content)
        print("insert into erp.bom_item (main_meterial,sub_meterial,quantity,description) values('{}','{}','%.0f','{}');".format(sub_meterrial,row_content[2],row_content[5]) % row_content[4], file = f)
# 读取文件
# r = open("sql.txt","r")
# sql_content = r.read()
# r.close()
# for i in range(0,row_num):
#     print(sheet.row_values(i))
# 输出第一列所有行
# row_list = sheet.col_values(1)
# print(row_list) 
# 获取单元格的数据
# print(sheet.cell_value(0,0))
# print(sheet.cell(1,0).value)
# for i in range(row_num):
#     if i % 2 == 0:
#         print(sheet.cell_value(i,0))