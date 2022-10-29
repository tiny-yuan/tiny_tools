#!/usr/bin/python3
from idste.add_camera.function import *

# idste数据库连接信息
ip = "202.115.116.196"
port = 3306
user = "root"
password = "iDste1057Hello"
database = "nccs"

# 连接idste数据库
idste = Mysql(ip, port, user, password, database)
# data_name.select("SELECT Dev_Name FROM nccs.DeviceList;")

name1 = "监控1"
name2 = "监控2"

# 连接jiasion数据库并输出数据到js_data.txt
js = Mongodb("202.115.116.200", 27017)
js.select()
sleep(5)
# 连接jsAPI
tiny = Api("202.115.116.200")
count_num = 0

# 逐行读取js_data.txt中的数据
for line in open("js_data.txt"):
    # 将数据类型变为字典
    line_dict = ast.literal_eval(line)
    # 获取设备的id
    id = line_dict["_id"]
    # print(len(id)) 根据id长度筛选出需要的id号
    if 8 <= len(id) <= 10:
        # 获取设备的name
        name = line_dict["name"]
        # 获取idste数据库中name对应的监控url
        idste.select("SELECT RtspUrl FROM nccs.DeviceList where Dev_Name='{}';".format(name))
        url1 = idste.idste_data
        idste.select("SELECT RtspUrl1 FROM nccs.DeviceList where Dev_Name='{}';".format(name))
        url2 = idste.idste_data
        # 将是url转换成需要的string
        idste.sql_string(url1)
        url1 = idste.a
        idste.sql_string(url2)
        url2 = idste.a
        # 调用api方法添加监控iot设备
        tiny.add_iot(id, name1, url1)
        tiny.add_iot(id, name2, url2)
        count_num += 1
        print("完成{}教室监控配置!".format(name))
    print("总共完成{}间教室监控配置!".format(count_num))




