#!/usr/bin/env bash

file="file"

if [ -e "$file" ];then
    if [ ! -s "$file" ];then
        echo 1
    else
        echo 0
    fi
else
    echo 2
fi