#/bin/bash
version=$1
sudo service jstrdpart stop
sudo apt remove jstrdpart -y
sudo apt update
sudo apt install jstrdpart=${version} -y
if [ $? -eq 0 ]
    then    
        echo "jstrdpart${version}安装成功！"
else
        echo "jstrdpart${version}安装失败！"
fi