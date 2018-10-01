#!/bin/sh
for FILE in `ls -rS data/*-in.txt`
do
	echo $FILE
	base=${FILE%-in.txt} #create a new variable 'base' for without the -in.txt ending
    python2 wordladders.py $base.txt $FILE > $base.yourname.out.txt # replace with your command and output to your own file
    diff $base.yourname.out.txt $base-out.txt
done
