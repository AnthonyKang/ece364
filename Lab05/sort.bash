#! /bin/bash
val1=0

while getopts f:-: thisopt
do
	case $thisopt in
		f) if [ ! -e $OPTARG ]
then
    echo "Error: File does not exist"
    exit 1
fi
			exec 3<$OPTARG
			f=$OPTARG;;
		-)val1=$(echo $OPTARG  | cut -d'=' -f2)
			if (($val1 > 4))
			then
			echo "Error: Column number $val1 does not exist."
			
			fi;;
         
         *)echo "Error: Unknown option."
			exit 1;;			
	esac
done


read line <&3

if (( $val1 == 0))
then
	echo "Error: Insufficient information"
	exit 1
fi
((val1=val1+1))
sort -k$val1 -n $f >"test.sorted" 
echo "File sorted."
exit 0
