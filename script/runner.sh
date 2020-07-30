#!/bin/sh


# try to run the script

i=0


while true; 
do

	python test.py

	if [ $? -eq 0 ]
	then
		echo "Successfully ran script"
		pkill -f firefox		
		
		now=$(date +'%r')
		
		git add .
		git commit -m "updating prices at $now"
		git push -u origin master
		
		break		
		

	else
		pkill -f firefox
		sleep 30
		echo "some error"
		i =$((i+1))
		if [ i > 5 ]
		then
			echo "failed"
		
			break

		fi

	fi
done
