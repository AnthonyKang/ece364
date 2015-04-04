#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 20:13:15 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72140 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/line_num.bash $
if (($# != 1))
then
	echo "Usage: line_num.bash <filename>"
	exit
fi
if [ ! -r $@ ]
then
	echo "Cannot read $@"
	exit
fi
linenum=1
while read line
do
	echo "$linenum:$line"
	((linenum=linenum+1))
done < $@
