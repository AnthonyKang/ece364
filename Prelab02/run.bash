#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-26 13:54:06 -0500 (Mon, 26 Jan 2015) $
#$Revision: 74025 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Prelab02/run.bash $
gcc $1 -o quick_sim
runtime=0
fastesttime=99999
fastwidth=0
fastcache=0
procc="Intel Core i7"
if (($? == 1))
then
	echo "error: quick_sim could not be compiled!"
	exit
fi

if [ -e $2 ]
then
	read -p "$2 exists. Would you like to delete it? " answer
	echo $answer
	if [ $answer == "n" ]
	then
		read -p "Enter a new filename: " newfile
		touch $newfile
		exec 4>>$newfile
	elif [ $answer == "y" ]
	then
		rm $2
		touch $2
		exec 4>>$2
	else
		echo "please enter y or n"
		exit 0	
	fi
fi
#exec 4>>$newfile

for ((i = 0; i < 6; i++))
do
	for (( j = 0; j < 5; j++))
	do
		#convert the string to an actual equation
		cache=$(echo "2^$i" | bc)
		issue=$(echo "2^$j" | bc)
		quick_sim $cache $issue a >&4	
		runtime=$(quick_sim $cache $issue a | cut -d ":" -f 10)
		if ((runtime < fastesttime))
		then
			fastesttime=$runtime
			procc="AMD Opteron"
			fastcache=$cache
			fastwidth=$issue
		fi
		quick_sim $cache $issue i >&4
		runtime=$(quick_sim $cache $issue i | cut -d ":" -f 10)	
		if ((runtime < fastesttime))
		then
			fastesttime=$runtime
			procc="Intel Core i7"
			fastcache=$cache
			fastwidth=$issue
		fi

	done
done
echo "Fastest run time achieved by $procc with cache size $fastcache and issue width $fastwidth was $fastesttime"
