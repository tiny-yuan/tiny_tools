#/bin/bash
version=$1
sudo service jsserver stop
sudo apt remove jsserver -y
sudo apt update
sudo apt install jsserver=${version} -y
if [ $? -eq 0 ]
    then    
        echo "jsserver${version}安装成功！"
else
        echo "jsserver${version}安装失败！"
fi