#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-26 13:54:06 -0500 (Mon, 26 Jan 2015) $
#$Revision: 74025 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab02/process_temps.bash $
line=0
skip=1
if (( $# < 1 ))
then
	echo "Usage: process_temps.bash <input file>"
	exit 1
fi
if [ ! -e $1 ]
then
	echo "Error: <filename> is not a readable file."
	exit 2
fi
exec 3< $1
while read -a line <&3
do
	((numservers=${#line[*]}-1))
	sum=0
	for ((i = 1; i < ${#line[*]}; i++))
	do
		#echo ${line[$i]}
		((sum=sum+${line[$i]}))
	done
	((average=sum/numservers))
	if (( skip == 0 ))
	then
		echo "Average temperature for time ${line[0]} was $average C."
	fi
	skip=0
done