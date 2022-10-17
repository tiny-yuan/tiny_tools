#!/bin/bash
#apt-get -y install pkg-config libopus-dev libopusfile-dev
version=$1
Install(){
        rm jiasion.gpg-key* -rf
        wget http://139.155.232.120/jiasion.gpg-key.asc && sudo apt-key add jiasion.gpg-key.asc
        cp /etc/apt/sources.list /etc/apt/sources.list.back 
        echo -e "deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse\ndeb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse\ndeb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse\ndeb http://139.155.232.120/mirror ./" > /etc/apt/sources.list
        apt-get update -y
        # apt-get upgrade -y
}
if [${version} = ""]
then    
        Install
        apt-get -y install jsserver
else
        Install
        apt-get -y install jsserver=${version}
fi      
if [ $? -eq 0 ]
        then
                echo 'jsserver install successfull!'
else
        echo 'jsserver install failure!'
fi
