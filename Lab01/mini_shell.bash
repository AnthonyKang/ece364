#! /bin/bash
#
#$Author: ee364f03 $
#$Date: 2015-01-21 09:57:28 -0500 (Wed, 21 Jan 2015) $
#$Revision: 73293 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab01/mini_shell.bash $
while ((1))
do
    echo "Enter a command: "
    read answer < /dev/tty
    if [[ $answer == "hello" ]]
    then
	user=$(whoami)
	echo "Hello $user"
    elif [[ $answer == "quit" ]]
    then
	echo "Exiting..."
	exit 0
    elif [[ $answer == "compile" ]]
    
    then
	echo "Enter filename: "
	read filename < /dev/tty
	if [[ -r $filename ]]
	then
	    gcc -Wall -Werror $filename
	    #returncode=$(gcc -Wall -Werror $filename)
	    if (( $? == 0 ))
	    then
		echo "Compilation succeeded"
	    else
		echo "Compilation failed"
	    fi
        else
	    echo "That file does not exist"
	fi
    else
	echo "Error Unrecognized input"
    fi
done