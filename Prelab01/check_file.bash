#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 20:13:15 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72140 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/check_file.bash $
if (($# != 1))
then
	#echo "Usage: line_num.bash <filename>"
	exit
fi
#check if file exists
if [ -e $@ ]
then
	echo "$@ exists"
else
	echo "$@ does not exist"
fi
#check if file is a directory
if [ -d $@ ]
then
	echo "$@ is a directory"
else
	echo "$@ is not a directory"
fi
#check if file is an ordinary file
if [ -f $@ ]
then
	echo "$@ is an ordinary file"
else
	echo "$@ is not an ordinary file"
fi
#check if file is readable
if [ -r $@ ]
then
	echo "$@ is readable"
else
	echo "$@ is not readable"
fi
#check if file is writeable
if [ -w $@ ]
then
	echo "$@ is writeable"
else
	echo "$@ is not writeable"
fi
#check if file is executable
if [ -x $@ ]
then
	echo "$@ is executable"
else
	echo "$@ is not executable"
fi