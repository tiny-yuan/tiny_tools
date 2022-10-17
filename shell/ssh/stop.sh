#!/bin/bash
start_pid=`ps  -f -C ssh -C start |grep -v grep | grep ./start| awk '{print $2}'`
kill -9 ${start_pid}
if [ $? -eq 0 ]
    then
        echo "start 进程结束"
else
        echo "start 进程结束失败"
fi
ssh_status="`ps  -f -C ssh -CqTfnN | grep ssh|grep -v grep | awk '{print $2}'`"
kill -9 ${ssh_status}
if [ $? -eq 0 ]
    then
        echo "ssh 反向连接进程关闭"
else
        echo "ssh 反向连接进程关闭"
fi