import json
from function.api import Api
from time import sleep

# 通过API请求的方式
####################################################################################

# 操作设备开关机
# '''list_id = ["5ee7139a","6294df43","23760897","f9ac9af8","2bf735c1","d9a1ff72"
# ,"cedc53de","6d60f191","8d3bc8a8","168634c3","96f85c15","17ef488f","1323f973",
# "aa6c9a33","b463eed6","fed92d38","2bb34e76","19b457bc","1c0b99c","3ad0f52c","ab40e8af","98a13be5","5fb774b4"]'''
list_id = ["75529b04"]
list_id = json.dumps(list_id)
# print(list_id)
test = Api('192.168.2.253')
num = 5
sleep_num1 = 600
sleep_num2 = 65
count_num = 0
while True:
    # 执行上课场景
    test.scenarioctrl(list_id, '630dd22f2fc9c260a07eebec')
    sleep(sleep_num1)
    # 执行下课场景
    test.scenarioctrl(list_id, 'silent')
    sleep(sleep_num2)
    count_num += 1
    print("完成第{}次上下课场景切换！".format(count_num))
    if count_num == num:
        print("*" * 100)
        print("{}次场景切换完成！".format(num))

# #添加iot设备

# test = Api('192.168.2.250') 
# test.add_iot('35ae5fae','displayer','62d64d669c17858f3e3149ee','投影',1,30)

# #删除设备

# test = Api('192.168.2.250')
# test.del_iot('35ae5fae','computer',1,11)

# # 获取设备列表

# test = Api('192.168.1.20')
# test.iotlist('75529b04')

# #批量单个设备
# test = Api('192.168.2.250')
# test.del_device(2051)

# #批量删除设备
# test = Api('192.168.2.250')
# test.batch_del_device(2000,4001)

# 通过MQTT请求的方式
####################################################################################

# 订阅消息
# test = MqttSubscribe("192.168.2.250","tiny","jiasion/device/state")
# test = MqttSubscribe("192.168.2.250","tiny","jiasion/device/state")
# test.subscribe()
