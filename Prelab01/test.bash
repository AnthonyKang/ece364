#! /bin/bash
#while read line
#do
#    echo "$line"
#done < 1.txt
status=$(svn status)
#echo $status
if [[ $status == *1.txt* ]]
then
	echo "hi"
fi