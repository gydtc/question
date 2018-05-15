#!/bin/bash
# 朋友要格式化一个4.24T的lv逻辑卷，要求先把里面数据urandom
# 参考了这个文档https://blog.csdn.net/adaptiver/article/details/6672592
# 生成一个16M的文件，bs1204=1k，16384*1k/1024=16M
dd if=/dev/urandom of=/home/aaa.file bs=1024 count=16384

# bs=16M,16*3200/1024=50G,i的最大值4.24*1024/50≈87，seek是每次略过数据
for(( i=0 ; i<=87 ; i++ ))
do
let snum=($i*3200)
echo $snum
dd if=/home/aaa.file of=/dev/mapper/vg名字 bs=16M count=3200 seek=$snum
done