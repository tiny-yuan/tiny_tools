#!/bin/bash
# 指定云服务器端口
port=$1
ListeningStatus(){
ssh_status="`ps  -f -C ssh -CqTfnN | grep ssh|grep -v grep | awk '{print $2}'`"
# echo "ssh连接前进程PID为:${ssh_status}"
if [ "${ssh_status}" = "" ]
# 开启进程
then
    echo "正在为您连接中！"
    ssh -CqTfnN -R 0.0.0.0:${port}:127.0.0.1:22 ubuntu@139.155.232.120
    echo "连接成功！"
    while true
        do
            ssh_status2="`ps  -f -C ssh -CqTfnN | grep ssh|grep -v grep | awk '{print $2}'`"
            # echo "ssh进程连接后第1次查询进程PID为:${ssh_status2}"
            sleep 5
            ssh_status3="`ps  -f -C ssh -CqTfnN | grep ssh|grep -v grep | awk '{print $2}'`"
            # echo "ssh进程连接后第2次查询进程PID为:${ssh_status3}"
            if [ "${ssh_status3}" = "${ssh_status2}" ]
            then
                echo "通讯正常！"
            elif [ "$ssh_status3" = "" ]
            then
                echo "通讯中断，正在重新连接！"
                ssh -CqTfnN -R 0.0.0.0:${port}:127.0.0.1:22 ubuntu@139.155.232.120
                echo "重新连接成功！"
            else
                sleep 5
            fi
        done
else
    sleep 5
fi
}
ListeningStatus