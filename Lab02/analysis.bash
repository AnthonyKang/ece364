#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-28 10:50:14 -0500 (Wed, 28 Jan 2015) $
#$Revision: 74347 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab02/analysis.bash $

if (($# != 1))
then
    echo "Usage: analysis.bash <input file>"
    exit 1
fi

if [ ! -r $1 ]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi
exec 3< $1
watt=0
while read -a line <&3
do
    sum=0
    average=0
    numcores=0
    #watt=0
    #topcore=0
    #topnum=0
    ((numcores=${#line[*]}-3))
    for ((i = 2; i < ${#line[*]}-1; i++))
    do
	((sum=sum+${line[$i]}))
    done
    ((average=sum/numcores))
    #echo $sum
    ((newwatt=$average/${line[${#line[*]}-1]}))
    if (($newwatt > $watt))
    then
	watt=$newwatt
	topcore=${line[0]}
	topnum=${line[1]}
    fi
    for ((i = 2; i <${#line[*]}-1; i++))
    do
	run=0
	if ((${line[$i]} < ($average*9/10)))
	then
	    ((run=$i-1))
	    echo "Run $run for ${line[0]} ${line[1]} with score ${line[$i]} was 90% less than average"
	fi
    done
    echo "${line[0]} ${line[1]} scored an average of $average"
done
echo "The best performance per watt was achieved by $topcore $topnum at $watt"
exit 0