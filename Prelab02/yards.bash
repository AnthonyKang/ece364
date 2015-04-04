#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-22 23:53:22 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73554 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab02/yards.bash $
exec 3< $1 
largest=0
while read -a line <&3
do
	sum=0
	average=0
	variance=0
	inner=0
	numschools=0
	((numschools=${#line[*]}-1))
	#echo ${line[*]}
	for ((i = 1; i < ${#line[*]}; i++))
	do
		#echo ${line[$i]}
		((sum=sum+${line[$i]}))
	done
	((average=sum/numschools))
	if (($average > $largest)) 
	then
		largest=$average
	fi
	for ((i = 1; i < ${#line[*]}; i++))
	do
		#echo $variance
		#echo ${line[$i]}
		((inner=${line[$i]}-average))
		((inner=inner*inner))
		((variance=variance+inner))
	done
	#echo "$sum $average $variance $inner $numschools"
	((variance=variance/numschools))
	echo "${line[0]} schools averaged $average yards receiving with a variance of $variance"

done
echo "The largest average yardage was $largest"