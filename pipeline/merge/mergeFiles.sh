echo "Accession identifer,Simple name,Category,Material,Provenance" > $1

for file in "${@:2}"; do
    sed '1d' $file >> $1    
done
