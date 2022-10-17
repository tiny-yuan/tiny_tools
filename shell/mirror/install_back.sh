#!/bin/bash
#apt-get -y install pkg-config libopus-dev libopusfile-dev
version=$1
rm jiasion.gpg-key* -rf
wget http://139.155.232.120/jiasion.gpg-key.asc && sudo apt-key add jiasion.gpg-key.asc
echo "deb http://139.155.232.120/jiasion ./" >> /etc/apt/sources.list
apt-get update
apt-get -y install jsserver=${version}
if [ $? -eq 0 ]
        then
                echo 'jsserver install successfull!'
else
        echo 'jsserver install failure!'
fi
