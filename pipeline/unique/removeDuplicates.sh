awk -F',' '{gsub(/"/, "", $1); if (!seen[$1]++) print}' "$1"  > "$2"
#awk -F',' '!seen[$1]++' "$1" > "$2"
