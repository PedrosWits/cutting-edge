head -1 "$1" > "$2"
  
sed '1d' "$1" | sort -u -t"," -k1 >> "$2"
