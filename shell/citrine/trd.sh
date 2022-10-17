#!/bin/bash
version=$1 
export https_proxy=192.168.2.100:8280
cd /home/liyuan/citrine
rm trdpart -rf
repo sync
cd build

./buildTrd.sh ${version}
if [ $? -eq 0 ]
    then    
        echo "jstrdpart build 完成！"
else
        echo "jstrdpart build 失败！"
fi