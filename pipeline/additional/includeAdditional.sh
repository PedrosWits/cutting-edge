for i in *.txt
do
	cat  $i | awk -F "=" 'BEGIN{ORS=","}; {print $2};{print "\n"}' 
done
