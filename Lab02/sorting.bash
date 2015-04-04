#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-28 10:50:14 -0500 (Wed, 28 Jan 2015) $
#$Revision: 74347 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab02/sorting.bash $

if (($# != 1))
then
    echo "Usage: sorting.bash <input file>"
    exit 1
fi

if [ ! -r $1 ]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi
exec 3< $1
echo "Your choices are:"
echo "1) First 10 people"
echo "2) Last 5 names by highest zipcode"
echo "3) Address of 6th-10th by reverse e-mail"
echo "4) First 12 companies"
echo "5) Pick a number of people"
echo "6) Exit"
read -p "Your choice: " choice
if (( $choice > 6))
then
    echo "Error! Invalid Selection!"
    exit
fi
if (( $choice == 1))
then
    sort -k7,7 -k5,5 -k2,2 -k1,1 -t, $1 | head
fi
if (( $choice == 2))
then
    sort -k8,8 -n -t, $1 | tail -n 5 | cut -f1,2 -d,
fi
if (( $choice == 3))
then
    sort -k11,11 -r -t, $1 | head -n 10 | cut -f4 -d, | tail -n 5
fi
if (( $choice == 4))
then
    sort -k3,3 -t, $1 | head -n 12 | cut -f3 -d,
fi
if (( $choice ==5))
then
    read -p "Enter a number: " num
    sort -k2 -k1 -t, $1 | head -n $num
fi
if (( $choice == 6))
then
    echo "Have a nice day!"
    exit 0
fi
exit 0