# 打印a1,b2,c3......z26

#!/bin/bash
i=1
for j in {a..z}
do
	echo $j$i
	(( i=$i+1 ))
done