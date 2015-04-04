#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 20:13:15 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72140 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/exist.bash $
for arg in $@
do
	if [ -r $arg ]
	then
		echo "File $arg is readable!"
	else
		if [ ! -e $arg ]
		then
			touch $arg
		fi
	fi
done