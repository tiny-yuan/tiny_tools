#!/bin/bash
dir_path=/home/liyuan/sql.back
time=`date "+%Y-%m-%d_%H:%M:%S"`
mysqldump -uzhanhl -pzhanhl -R erp > sql.back/${time}_erp.sql
if [ $? -eq 0 ]
    then
        echo "back successfull!"
else
        echo "back failure!"
fi
# find ${dir_path:=/home/liyuan/sql.back} -name '*.sql' -type f -mtime +1|xargs rm -f
find ${dir_path} -name '*.sql' -type f -mtime +60|xargs rm -f
if [ $? -eq 0 ]
    then
        echo "备份完成并清理两个月以上的备份！"
else
        echo "两个月以上的备份清理失败！"
fi