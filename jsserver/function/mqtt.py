#!/usr/bin/python3
from paho.mqtt import client as mqtt
import time


class MqttPublish:
    def __init__(self, server_ip, client_id, topic, msg):
        # 传参MQTT服务器地址
        self.server_ip = server_ip
        self.client_id = client_id
        self.mqttClient = mqtt.Client(self.client_id)
        self.topic = topic
        self.msg = msg

    # 连接MQTT服务
    def mqtt_connect(self):
        # 生成客户端ID
        # client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))   
        MQTTHOST = "192.168.2.250"  # MQTT服务器地址
        MQTTPORT = 1883  # MQTT端口
        # mqttClient.username_pw_set("username", "password") # mqtt服务器账号密码
        self.mqttClient.connect(self.server_ip, MQTTPORT, 60)  # 超时时间为60秒
        self.mqttClient.loop_start()  # 启用子线程连接

    # 发布消息
    def publish(self):
        self.mqtt_connect()
        self.mqttClient.publish(self.topic, self.msg, 2)
        self.mqttClient.loop_stop()  # 断开连接


class MqttSubscribe:
    def __init__(self, server_ip, client_id, topic):
        # 传参MQTT服务器地址
        self.server_ip = server_ip
        self.client_id = client_id
        self.topic = topic

    # 回调函数
    def on_connect(self, client, userdata, flags, rc):
        # """一旦连接成功, 回调此方法"""
        if rc == 0:
            print('连接成功！ 回码为：', rc)
        else:
            print("连接失败！回码为：", rc)
        client.subscribe(self.topic, 2)  # 发布主题 服务质量qos

    def on_message(self, client, userdata, msg):
        # """一旦订阅到消息, 回调此方法"""
        payload = str(msg.payload.decode('utf-8'))  # 客户端返回的消息,使用gb2312编码中文不会报错
        print(payload)

    # 监听消息
    def server_connect(self, client):
        client.on_connect = self.on_connect  # 启用订阅模式
        client.on_message = self.on_message  # 接收消息
        # client.username_pw_set("username", "password") # mqtt服务器账号密码
        client.connect(self.server_ip, 1883, 60)  # 链接
        client.loop_forever()  # 以forever方式阻塞运行。

    def subscribe(self):
        client = mqtt.Client(self.client_id, transport='tcp')
        self.server_connect(client)


if __name__ == '__main__':
    for num in range(100):
        msg = '''
            {
            "DeviceID": "%d",
            "base": {
                "devid": "%d",
                "name": "虚拟测试设备%d",
                "location": "%d",
                "ipaddr": "192.168.2.%d",
                "server": "192.168.2.250",
                "version": {
                    "hardware": "",
                    "software": "1.3.2"
                }
            },
            "platform": {
                "video": {
                    "displayer": [
                        {
                            "class": "displayer",
                            "index": 0,
                            "enable": false,
                            "name": "投影",
                            "states": {
                                "power": {
                                    "value": "off",
                                    "working": false,
                                    "Async": false
                                },
                                "source": {
                                    "value": "none",
                                    "working": false,
                                    "Async": false
                                }
                            }
                        },
                        {
                            "class": "displayer",
                            "index": 1,
                            "enable": false,
                            "name": "显示器",
                            "states": {
                                "power": {
                                    "value": "off",
                                    "working": false,
                                    "Async": false
                                },
                                "source": {
                                    "value": "none",
                                    "working": false,
                                    "Async": false
                                }
                            }
                        }
                    ]
                },
                "audio": {
                    "enable": false,
                    "lineVolume": 1,
                    "lineMute": true,
                    "micVolume": 1,
                    "micMute": true,
                    "LineSrc": 0,
                    "MicSrc": 0
                },
                "computer": {
                    "class": "computer",
                    "index": 0,
                    "enable": true,
                    "name": "电脑",
                    "states": {
                        "power": {
                            "value": "off",
                            "working": true,
                            "Async": true
                        }
                    }
                }
            },
            "scenario": {
                "user": "",
                "scenario": "课间",
                "list": [
                    "上课"
                ],
                "exit": false,
                "enter": true,
                "standby": true,
                "consistent": true
            },
            "ipcall": {
                "state": "idle"
            },
            "broadcast": {
                "taskid": "",
                "taskname": "",
                "state": "stop",
                "addr": ""
            },
            "iot": {
                "computer": [
                    {
                        "class": "computer",
                        "index": 0,
                        "enable": true,
                        "name": "电脑",
                        "states": {
                            "power": {
                                "value": "off",
                                "working": true,
                                "Async": true
                            }
                        }
                    }
                ],
                "displayer": [
                    {
                        "class": "displayer",
                        "index": 0,
                        "enable": false,
                        "name": "投影",
                        "states": {
                            "power": {
                                "value": "off",
                                "working": false,
                                "Async": false
                            },
                            "source": {
                                "value": "none",
                                "working": false,
                                "Async": false
                            }
                        }
                    },
                    {
                        "class": "displayer",
                        "index": 1,
                        "enable": false,
                        "name": "显示器",
                        "states": {
                            "power": {
                                "value": "off",
                                "working": false,
                                "Async": false
                            },
                            "source": {
                                "value": "none",
                                "working": false,
                                "Async": false
                            }
                        }
                    }
                ]
            }
        }''' % (num, num, num, num, num)
        msg1 = '''{"deviceID": "%d"}''' % (num)
        test = MqttPublish('192.168.2.250', 'tiny', "jiasion/device/state", msg)
        test.publish()
        time.sleep(2)
        test = MqttPublish('192.168.2.250', 'tiny', "jiasion/device/offline", msg1)
        test.publish()
        time.sleep(2)
        # test = Mqtt_Subscribe('192.168.2.250','tiny',"jiasion/device/state")
