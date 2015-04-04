#! /bin/bash

while getopts a:b:-: thisopt
do
        case $thisopt in
          a)echo $OPTARG;;
          b)echo $OPTARG;;
          -)val=$(echo $OPTARG  | cut -d'=' -f2)
            echo $val ;;
          *)echo "Invalid arg";;
        esac
done

exit 0