import sqlite3
import csv
import sys
import os

# Read Arguments from Command Line
if(len(sys.argv)) != 3:
    print "Usage: python", sys.argv[0], "csv_file db_name"
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]):
    print "Not a valid input file"
else:
    csv_file = sys.argv[1]
    db_file = sys.argv[2]

# Check if file db_file already exists - if so delete
if os.path.isfile(db_file):
    os.remove(db_file)

# Prep Database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("CREATE TABLE Artefacts (accession text, name text, category text, material text, provenance text)")

with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    next(reader, None)
    for line in reader:
        values = (line['Accession identifer'],
                  line['Simple name'],
                  line['Category'],
                  line['Material'],
                  line['Provenance'])
        cursor.execute("INSERT INTO Artefacts VALUES(?, ?, ?, ?, ?)", values)


conn.commit()
conn.close()
