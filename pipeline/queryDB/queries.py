import sqlite3
import os
import sys

def selectDaggers(cursor):
        cursor.execute("SELECT * FROM Artefacts WHERE category='Daggers';")
        results = cursor.fetchall()
        return results;

def selectMadeOfBronze(cursor):
        cursor.execute("SELECT count(Material) FROM Artefacts WHERE Material='Bronze';")
        results = cursor.fetchall()
        return results;

def selectProvenanceUnknown(cursor):
        cursor.execute("SELECT *  FROM Artefacts  WHERE provenance='' OR provenance='Unknown' OR provenance LIKE '%?%';")
        results = cursor.fetchall()
        return results;

def writeToFile(lst, filename):
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path + "/" + filename, "w") as tfile:
        for item in lst:
            tfile.write(", ".join(map(str, item)))
            tfile.write("\n")

def main(dbfile):
    # Running the queries and saving the results to disk
    if not os.path.isfile(dbfile):
        print("Given file is not valid.")
        sys.exit(2)
    connection = sqlite3.connect(dbfile)
    cursor = connection.cursor()

    writeToFile(selectDaggers(cursor), "Daggers.txt")
    writeToFile(selectMadeOfBronze(cursor), "TotalMadeOfBronze.txt")
    writeToFile(selectProvenanceUnknown(cursor), "ProvenanceUnknown.txt")

    connection.close()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage:", sys.argv[0], "db_file")
        sys.exit(1)
    main(sys.argv[1])
