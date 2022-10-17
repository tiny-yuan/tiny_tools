#!/bin/bash
dir_path=/home/liyuan/redmine_back
time=`date "+%Y-%m-%d_%H:%M:%S"`
mysqldump -uroot -proot -R redmine > redmine_back/${time}_redmine.sql
if [ $? -eq 0 ]
    then
        echo "back successfull!"
else
        echo "back failure!"
fi
# find ${dir_path:=/home/liyuan/sql.back} -name '*.sql' -type f -mtime +1|xargs rm -f
find ${dir_path} -name '*.sql' -type f -mtime +30|xargs rm -f
if [ $? -eq 0 ]
    then
        echo "一月以上的备份已经完成清理！"
else
        echo "一月以上的备份已经清理失败！"
fi
