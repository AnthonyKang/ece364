#! /bin/bash
#
#$Author$
#$Date$
#$Revision$
#$HeadURL$
A=(1 2 3 hello)
echo ${A[*]}
echo ${!A[*]}
A[27]="x"
A[6]="y"
A[86]="z"
echo ${!A[*]}
for I in ${A[*]}
do
	echo "$I"
done
for ((I = 0; I < ${#A[*]}; I++))
do
	echo ${A[$I]}
done