import re
from scapy.all import *
import time,struct,random
# 编写ping一个包的函数。
def ping_one(dst = '36.152.44.95',ttl_no = 64,id_no = 345,seq_no = 5):
  start_time = time.time()
  # 将时间转换为二进制序列。
  time_to_bytes = struct.pack('>d',start_time)
  # 进行发送ICMP包,发送出去一个，收回来一个。
  ping_one_result = sr1(IP(dst = dst,ttl = ttl_no)/ICMP(seq = seq_no,id = id_no)/time_to_bytes, timeout = 1, verbose=False)
  # print(ping_one_result.show())
  # 判断收回来的包是不是ICMP的应答包，和序列号是否相同。
  try:
    if ping_one_result.getlayer('ICMP').type == 0 and ping_one_result.getlayer('ICMP').seq == seq_no:
      # print('进行解析包')
      # 提取IP头部中的源IP地址，也就是我们ping的IP地址。
      reply_src_IP = ping_one_result.getlayer('IP').src
      # 提取序列号。
      reply_icmp_seq = ping_one_result.getlayer('ICMP').seq
      # 提取ttl
      reply_icmp_ttl = ping_one_result.getlayer('IP').ttl
      # 数据长度等于 数据长度（Raw） + 垫片长度（Padding） + 8字节（ICMP头部长度）
      if ping_one_result.getlayer(Raw) != None:
        Raw_length = len(ping_one_result.getlayer(Raw).load)
      else:
        Raw_length = 0
      if ping_one_result.getlayer(Padding) != None:
        Padding_length = len(ping_one_result.getlayer(Padding).load)
      else:
        Padding_length = 0
      # 计算数据长度。
      reply_data_length = Raw_length + Padding_length + 8
      # 取出数据部分，这里的数据部分是我们发送ICMP请求包的时候填入的时间。
      reply_data = ping_one_result.getlayer(Raw).load
      # 定义我们收包的时间。
      end_time = time.time()
      # 将数据时间部分进行转换。
      reply_data_time = struct.unpack('>d',reply_data)
      # 然后打印出转换后的类型。
      # print(type(reply_data_time))
      # print(reply_data_time)
      time_to_pass_ms = (end_time - reply_data_time[0]) * 1000
      # （接收时间 - 发送时间） * 1000为毫秒数为消耗时间的毫秒数
      # print(time_to_pass_ms)
      return reply_data_length,reply_src_IP,reply_icmp_seq,reply_icmp_ttl,time_to_pass_ms
  except Exception as e:
    # 打印出错误。
    # print('e', e)
    # 匹配错误是否为NoneType类型。
    if re.match('.*NoneType.*', str(e)):
      print('错误了')
      # 如果没有回应，就返回None
      return None
def ping(dst = '36.152.44.95'):
  # 这里其实可以取进程号的，但是我们用随机生成一个数字模拟一下。
  id_no = random.randint(0,65535)
  # print(id_no)
  # 然后进行发送5个数据包。
  for i in range(1,6):
    # 调用ping一个包函数,入参为目的需要ping的IP地址。ttl，id，和序列号。seq。
    ping_result = ping_one(dst,64,id_no,i)
    if ping_result != None:
      print('%d bytes from %s: icmp_seq=%d ttl=%d time=%4.2f ms' % (ping_result[0], ping_result[1], ping_result[2], ping_result[3], ping_result[4]))
    else:
      print('.',end = '',flush = True)
    # 这里我们暂停一秒。
    time.sleep(1)

if __name__ == "__main__":
  ping('36.152.44.95')