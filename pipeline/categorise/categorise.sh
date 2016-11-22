awk -F "," '/,,,,,,,,,/{flag=1; a=$1; next} BEGIN{OFS= ","} {$1=a FS $ (1) ; print} ; /,,,,,,,,,/{flag=0} ' $1 > $2
sed -i.old '1s;^;Category;' $2
