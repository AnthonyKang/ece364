#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 20:13:15 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72140 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/sum.bash $
sum=0
for arg in $@
do
	#echo $arg
	((sum=$arg+sum))
done
echo $sum