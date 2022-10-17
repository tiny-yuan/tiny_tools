#/bin/bash
# 杀掉进程
version=$1 
sudo kill `ps -ef|grep erp |grep -v grep| awk '{print $2}'`
# 添加代理
export https_proxy=192.168.2.100:8280
# 删除原代码
rm server/ web/ -rf
# 获取后端代码
git clone git@dev.jiasion.cn:erp/server.git
# 获取前端代码
git clone git@dev.jiasion.cn:erp/web.git
#编译前端代码
cd server/
go build -o erp main.go
# 部署到启动路径
sudo cp erp /usr/bin
# 对应版本备份后端执行程序
if test -e ../erp.back/${version}/srv
    then
        cp erp ../erp.back/${version}/srv
    else
        mkdir -p ../erp.back/${version}/srv
        cp erp ../erp.back/${version}/srv
fi
# 编译前端代码
cd ../web/
npm install
npm run build
# 对应版本备份前端执行程序
if test -e ../erp.back/${version}/web
    then
        cp dist ../erp.back/${version}/web -rf
    else
        mkdir -p ../erp.back/${version}/web
        cp dist ../erp.back/${version}/web -rf
fi
cd dist
# 部署前端代码
sudo cp * -r /opt/erp -rf
# 运行erp程序
sudo nohup erp > /dev/null &