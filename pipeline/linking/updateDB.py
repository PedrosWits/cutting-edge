import parseApache
import sqlite3
import sys
import os

def createTableImageUrls(cursor, urls):
    cursor.execute("CREATE TABLE Images (accession text, url text)")    
    for url in urls:
	accession = url.split('-')[0]
        cursor.execute("INSERT INTO Images VALUES(?, ?)", (accession, url))

def selectProvenanceUnknown(cursor):
        cursor.execute("SELECT *  FROM Images;")
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

    # Get artefact image urls
    urls = parseApache.getUrlOfArtefactImages()
    # Create table for image urls
    createTableImageUrls(cursor, urls)
    # Run query and write result to disk
    writeToFile(getUrls(cursor), "URLs.txt")

    connection.close()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage:", sys.argv[0], "db_file")
        sys.exit(1)
    main(sys.argv[1])

