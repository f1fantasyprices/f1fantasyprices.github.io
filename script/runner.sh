#!/bin/sh


# try to run the script

i=0


while [ $i -le 5 ]; do

	python3 main.py

	if [ $? -eq 0 ]; then
		echo "Successfully ran script"
		pkill -f firefox
		now=$(date +'%r')

		git add .
		git commit -m "updating prices at $now"
		git push -u origin master
		break


	else
		pkill -f firefox
		sleep 10
		echo "some error"
		i=$(( i+1 ))
		echo "$i"

	fi

done

echo "failed"
