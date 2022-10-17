#!/bin/bash
export https_proxy=192.168.2.100:8280
cd /home/liyuan/citrine
repo sync
cd build

./buildMongo.sh 
if [ $? -eq 0 ]
    then    
        echo "mongo build 完成！"
else
        echo "mongo build 失败！"
fi