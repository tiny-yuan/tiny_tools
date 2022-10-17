from pip import main
from pymysql import *
# 数据库连接信息
ip = "127.0.0.1"
port = 3306
user = "root"
password = "123456"
database = "python"
# 数据库连接
coon = connect(host=ip,port=port,user=user,password=password,database=database,charset="utf8")
# 创建指针
cs1 = coon.cursor()
# # 创建学生班级表
# sql_1 = "create table classes (id int unsigned primary key auto_increment not null,name varchar(10));"
# # 创建学生信息表
# sql_2 = "create table students(id int unsigned primary key auto_increment not null,name varchar(10),age int unsigned default 0,height decimal(5,2),gender enum('男','女','保密'),cls_id int unsigned default 0);"
# 插入班级信息表
# sql_3 = "insert into python.classes (name) values ('高一三班');"
# 插入学生信息
sql_4 = "insert into python.students (name,age,height,gender) values ('李大爷a111111',1,15,'男');"
# 执行sql语句并获取打印信息
# sql_5 = "select * from students"
sql_6 = "select * from students"
# cs1.execute(sql_1)
# cs1.execute(sql_2)
# cs1.execute(sql_3)
cs1.execute(sql_4)
info = cs1.execute(sql_6)
# cs1.execute(sql_2)
# 逐条打印输出信息
for i in range (info):
    print(cs1.fetchone())
cs1.close()
coon.close()
if __name__=="__main__":
    main()

