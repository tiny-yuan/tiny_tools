#!/usr/bin/python3
import json
import ast
from time import sleep

import requests
from pymysql import *
from pymongo import MongoClient


class Mysql:

    idste_data = ''
    a = ''

    def __init__(self, ip, port, user, password, database):
        # 传参服务器ip
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def select(self, sql):
        # 数据库连接
        coon = connect(host=self.ip, port=self.port, user=self.user, password=self.password, database=self.database,charset="utf8")
        # 创建指针
        cs = coon.cursor()
        # sql = "SELECT Dev_Name,RtspUrl,RtspUrl1 FROM nccs.DeviceList;"
        # 执行sql语句
        info = cs.execute(sql)
        # 逐条打印输出信息
        for i in range(info):
            self.idste_data = cs.fetchone()
        cs.close()
        coon.close()

    def sql_string(self, b):
        if b == None:
            b = ''
            self.a = b
        else:
            b = str(b)
            add_punc = "( ',)"  # 自定义--中文的字符
            # all_punc = punctuation + add_punc  所有符号
            all_punc = add_punc
            temp = []
            for c in b:
                if c not in all_punc:
                    temp.append(c)
            b = ''.join(temp)
            self.a = b


class Mongodb:
    def __init__(self, ip, port):
        # 传参服务器ip
        self.ip = ip
        self.port = port

    def select(self):
        client = MongoClient(self.ip, self.port)
        # 选择数据库
        db = client["jsctrl"]
        # 选择表
        mycol = db["section"]
        # 输出是个
        with open("js_data.txt", "w") as f:
            for i in mycol.find({}, ):
                print(i, file=f)
                # print(i)

    def data(self):
        for line in open("js_data.txt"):
            line_dict = ast.literal_eval(line)


class Api:
    token = ''

    def __init__(self, server_ip):
        # 传参服务器ip
        self.server_ip = server_ip

    def login(self):
        # 登录请求信息
        login_url = 'https://%s/login' % self.server_ip
        login_headers = {"Content-Type": "application/json"}
        login_request_body = '''
        {
            "username":"admin","password":"admin"
        }
        '''
        login_reponse = requests.post(login_url, headers=login_headers, data=login_request_body.encode('utf-8'),verify=False)
        # 默认返回的数据格式为str，我们编码为字典
        data = json.loads(login_reponse.text)
        # 获取数据中的token地址信息
        data = data['data']
        self.token = data['token']
        # 打印返回信息
        # print("{} {}\n登录成功！\n返回的token：{}".format(login_reponse.status_code,login_reponse.reason,self.token))

    def add_iot(self, id, name, url):
        # 对设备增加iot设备
        self.login()
        add_iot_url = 'https://%s/api/iot/device/new' % self.server_ip
        add_lot_headers = {
            "Content-Type": "application/json",
            "token": "%s" % self.token
        }
        add_iot_request_body = '''
            {
                "id": "%s",
                "modelId": "62f20c49e3ed2550dd760b37",
                "device": {
                    "name": "%s",
                    "resource": {
                        "rtsp": {
                            "type": "[net]stream",
                            "interface": "%s"
                        }
                    }
                }
            }
            ''' % (id, name, url)
        add_iot_reponse = requests.post(add_iot_url, headers=add_lot_headers, data=add_iot_request_body.encode('utf-8'),
                                        verify=False)
        if add_iot_reponse.status_code == 200:
            print("完成id为{}的{}添加！".format(id, name))
        else:
            print("id为{}的{}添加失败！".format(id, name))


if __name__ == '__main__':
    pass
