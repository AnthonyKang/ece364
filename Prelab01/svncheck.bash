#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-15 20:13:15 -0500 (Thu, 15 Jan 2015) $
#$Revision: 72140 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab01/svncheck.bash $
if (($# != 1))
then
	echo "Usage: svncheck.bash <filename>"
	exit
fi
while read -r filename || [[ -n $filename ]]
do
	status=$(svn status)
	# if its not in the svn
	if [[ $status == *$filename* ]]
	then
		# if it exists
		#echo "$filename"
		if [[ -e $filename ]]
		then
			#echo "$filename not in svn but exists"
			# check if the file is executable
			if [[ ! -x $filename ]]
			then
				# ask user if wnat to make executable
				echo "Would you like to make $filename executable"
				read answer < /dev/tty
				if [[ $answer == "y" ]]
				then
					chmod +x $filename
				fi
			fi
			svn add $filename
		else
			echo "Error:File $filename appears to not exist here or in svn"
		fi
		#echo "$filename not in svn"
	else
		svn propset svn:executable ON $filename
	fi
done < $@
svn commit -m "Auto-committing code"