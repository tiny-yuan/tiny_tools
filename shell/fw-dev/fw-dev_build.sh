#!/bin/bash
version=$1
source /opt/fsl-imx-x11/4.1.15-2.1.0/environment-setup-cortexa7hf-neon-poky-linux-gnueabi
cd /home/liyuan/rock
sudo rm * -rf
repo sync
cd build
export https_proxy=192.168.2.100:8280
./build ${version}
if [ $? -eq 0 ]
then
        echo "编译完成！"
else
        echo "编译失败！"
fi

sleep 2
cd ../
tar -cvf release.tar release/
if test -e /var/www/html/firmware/${version}
then 
        sudo cp /home/liyuan/rock/release/jiasion_dev_${version}.swu /var/www/html/firmware/${version}/ 
        sudo cp release.tar /var/www/html/firmware/${version}/
        echo "发布完成！"
else
        sudo mkdir /var/www/html/firmware/${version}
        sudo cp /home/liyuan/rock/release/jiasion_dev_${version}.swu /var/www/html/firmware/${version}/ 
        sudo cp release.tar /var/www/html/firmware/${version}/
        echo "发布完成！"
fi