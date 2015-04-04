#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-21 10:52:03 -0500 (Wed, 21 Jan 2015) $
#$Revision: 73329 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab01/collect_expr.bash $
if(($# < 2))
then
    echo "usage: collect_expr.bash<output file> <input file1> [input file 2] ... [input file N]"
    exit
fi
if [ -e $1 ]
then
    echo "output $1 already exists"
    exit
fi


#rm $1
touch $1
output=$1

for var in $@
do
    if [ ! -f $var ]
    then
	echo "input file $var is not a readable file"
    fi
    if [ ! -r $var ]
    then
	echo "input file $ var is not readable"
	exit
    fi
    while read line
    do
	id=$(echo "$line" | cut -d " " -f 1) 
	#echo $id
	val1=$(echo "$line" | cut -d " " -f 2)
	#echo $val1
	val2=$(echo "$line" | cut -d " " -f 3)
	val3=$(echo "$line" | cut -d " " -f 4)
	val4=$(echo "$line" | cut -d " " -f 5)
	val5=$(echo "$line" | cut -d " " -f 6)
	((total=val1+val2+val3+val4+val5))
	((avg=total/5))
	#touch $1
	#echo "$id $va1 $val2 $val3 $val4 $val5 $total $avg"
	echo "$id $val1 $val2 $val3 $val4 $val5 $total $avg" >> $1
    done < $var
done