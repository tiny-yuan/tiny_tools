#!/usr/bin/python3
import requests
import json


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
        login_reponse = requests.post(login_url, headers=login_headers, data=login_request_body.encode('utf-8'),
                                      verify=False)
        # 默认返回的数据格式为str，我们编码为字典
        data = json.loads(login_reponse.text)
        # 获取数据中的token地址信息
        data = data['data']
        self.token = data['token']
        # 打印返回信息
        # print("{} {}\n登录成功！\n返回的token：{}".format(login_reponse.status_code,login_reponse.reason,self.token))

    def iotlist(self, device_id):
        # 获取设备iot列表
        self.login()
        iotlist_url = 'https://%s/api/iot/device/list' % self.server_ip
        lotlist_headers = {
            "Content-Type": "application/json",
            "token": "%s" % self.token
        }
        iotlist_request_body = '''
        {"id": "%s"}
        ''' % device_id
        iotlist_reponse = requests.post(iotlist_url, headers=lotlist_headers, data=iotlist_request_body.encode('utf-8'),
                                        verify=False)
        print(iotlist_reponse.text)

    def add_iot(self, device_id, class_type, model_id, name, num1, num2):
        # 对设备增加iot设备
        self.login()
        add_num = 0
        count_num = 0
        count_list = []
        for num in range(num1, num2):
            add_iot_url = 'https://%s/api/iot/device/new' % self.server_ip
            add_lot_headers = {
                "Content-Type": "application/json",
                "token": "%s" % self.token
            }
            if class_type == 'displayer':
                add_iot_request_body = '''
                {
                "id": "%s",
                "modelId": "%s",
                "device": {
                    "name": "%s%d",
                    "resource": {
                    "control": {
                        "type": "[ext]uart",
                        "interface": "rs232-3",
                        "name": "通信接口",
                        "description": "232串口控制接口",
                        "baudrate": 19200,
                        "parity": 0
                    },
                    "power": {
                        "type": "[ext]gpio",
                        "interface": "project",
                        "name": "电源控制接口",
                        "description": "电源接口"
                    },
                    "video": {
                        "type": "[ext]hdmi_out",
                        "interface": "out2",
                        "name": "视频接口",
                        "description": "视频输出到显示接口"
                    }
                    }
                }
                }''' % (device_id, model_id, name, num)
            elif class_type == 'computer':
                add_iot_request_body = '''
                {
                    "id": "%s",
                    "modelId": "%s",
                    "device": {
                        "name": "%s%d",
                        "resource": {
                            "control": {
                                "type": "[net]pcctrl",
                                "name": "远程开关机",
                                "description": "远程开关机",
                                "macaddr": "123",
                                "remote": "123"
                            },
                            "power": {
                                "type": "[ext]gpio",
                                "interface": "extend2",
                                "name": "电源",
                                "description": "电源"
                            }
                        }
                    }
                }''' % (device_id, model_id, name, num)
            add_iot_reponse = requests.post(add_iot_url, headers=add_lot_headers, data=add_iot_request_body.encode('utf-8'), verify=False)
            if add_iot_reponse.status_code == 200:
                add_num += 1
                print("完成添加第{}个Iot".format(add_num))
                count_num += 1
            else:
                count_num += 1
                count_list.append(count_num)
            # sleep(1)
        if add_num == num2 - num1:
            print("*" * 100)
            print("{}全部Iot添加完成！".format(add_num))
        else:
            print("*" * 100)
            print("完成{}台添加！剩余{}台未添加！分别为第{}台".format(add_num, num2 - num1 - add_num, count_list))

    def del_iot(self, device_id, class_type, num1, num2):
        # 删除设备iot设备
        self.login()
        count_num = 0
        count_list = []
        del_num = 0
        for num in range(num1, num2):
            del_iot_url = 'https://%s/api/iot/device/delete' % self.server_ip
            del_lot_headers = {
                "Content-Type": "application/json",
                "token": "%s" % self.token
            }
            del_iot_request_body = '''
            {"id": "%s",
            "device": {
                "index": %d,
                "class": "%s"
            }
            }''' % (device_id, num, class_type)
            del_iot_reponse = requests.post(del_iot_url, headers=del_lot_headers,
                                            data=del_iot_request_body.encode('utf-8'), verify=False)
            # 记录正常删除
            if del_iot_reponse.status_code == 200:
                del_num += 1
                count_num += 1
                print("完成删除第{}一个Iot".format(del_num))
            # 记录不正常删除
            else:
                count_num += 1
                count_list.append(count_num)
        # sleep(0.1)
        if del_num == num2 - num1:
            count_num += 1
            print("*" * 100)
            print("{}台Iot全部删除完成！".format(del_num))
        else:
            print("*" * 100)
            print("完成{}台删除！剩余{}台未删除！分别为第{}台".format(del_num, num2 - num1 - del_num, count_list))

    def scenarioctrl(self, device_id, scenario):
        # 设备场景切换
        self.login()
        switch_url = 'https://%s/api/device/scenario/switch' % self.server_ip
        switch_headers = {
            "Content-Type": "application/json",
            "token": "%s" % self.token
        }
        switch_request_body = '''
        {"id":%s,"scenario":"%s"}: 
        ''' % (device_id, scenario)
        switch_reponse = requests.post(switch_url, headers=switch_headers, data=switch_request_body.encode('utf-8'),
                                       verify=False)
        if switch_reponse.status_code == 200:
            print('{}场景执行成功!'.format(scenario))

    def del_device(self, device_id):
        # 单个设备删除
        self.login()
        del_device_url = 'https://%s/api/device/delete' % self.server_ip
        del_device_headers = {
            "Content-Type": "application/json",
            "token": "%s" % self.token
        }
        del_device_request_body = '''{"id":["%s"]}''' % device_id
        del_device_reponse = requests.post(del_device_url, headers=del_device_headers,
                                           data=del_device_request_body.encode('utf-8'), verify=False)
        if del_device_reponse.status_code == 200:
            print("完成{}删除!".format(device_id))
        else:
            print('请求报错：', del_device_reponse.text)

    def batch_del_device(self, num1, num2):
        # 批量设备删除
        self.login()
        batch_del_device_url = 'https://%s/api/device/delete' % self.server_ip
        batch_del_device_headers = {
            "Content-Type": "application/json",
            "token": "%s" % self.token
        }
        # 生成删除id的列表
        device_id = []
        for num in range(num1, num2):
            device_id.append("{}".format(num))
        device_id = json.dumps(device_id)
        del_device_request_body = '''{"id":%s}''' % device_id
        del_device_reponse = requests.post(batch_del_device_url, headers=batch_del_device_headers,
                                           data=del_device_request_body.encode('utf-8'), verify=False)
        if del_device_reponse.status_code == 200:
            print("完成{}-{}批量删除!".format(num1, num2))
        else:
            print('请求报错：', del_device_reponse.text)


if __name__ == "__main__":
    test = Api('192.168.2.250')
    test.iotlist('35ae5fae')
