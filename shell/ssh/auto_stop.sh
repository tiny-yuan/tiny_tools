#!/bin/bash
while true
    do
        start_pid=`ps  -f -C ssh -C start |grep -v grep | grep ./start| awk '{print $2}'`
        if [ "${start_pid}" = "" ] 
        then
            break
        else
            sudo kill ${start_pid}
        fi
    done