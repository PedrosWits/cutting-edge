# Get TXT files
zipfile="txtfiles.zip"
curl -s -o $zipfile http://homepages.cs.ncl.ac.uk/matthew.forshaw/teaching/csc8622/cswk/data/cuttingedge.zip

txtdir="txt"
mkdir -p $txtdir
unzip -o -q $zipfile -d $txtdir

rm $zipfile

# Create CSV
outfile=$1
echo "Accession identifier, Simple name, Category, Material, Provenance" > $outfile

for filename in $(ls -p $txtdir | grep -v /); do
    while read -r line || [ -n "$line" ]; do
        word=$(echo "$line" | cut -d '=' -f 2)
        printf '\"%q\",' "$word" >> "$outfile"
    done <"$(PWD)/$txtdir/$filename"
    echo >> $outfile
done

cat $outfile | tr -d $ | sed -e 's/\\r//g' | tr -d \\ | tr -d \' | sed s'/,$//' > $outfile
