#!/bin/bash
version=$1 
export https_proxy=192.168.2.100:8280
cd /home/liyuan/citrine
rm * -rf
repo sync
cd build

./buildSrv.sh ${version}
if [ $? -eq 0 ]
    then    
        echo "jsserver build 完成！"
else
        echo "jsserver build 失败！"
fi