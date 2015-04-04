#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 22:34:18 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72160 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/sensor_sum.sh $
if (($# != 1))
then
	echo "Usage: sensor_sum.sh <filename>"
	exit
fi
if [ ! -r $@ ]
then
	echo "$@ is not a readable file"
	exit
fi
linenum=1
while read line
do
	id=$(echo "$line" | cut -d "-" -f 1) 
	val1=$(echo "$line" | cut -d " " -f 3)
	val2=$(echo "$line" | cut -d " " -f 5)
	val3=$(echo "$line" | cut -d " " -f 7)
	((total=val1+val2+val3))
	echo "$id $total"
		
done < $@
