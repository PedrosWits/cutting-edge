def daggersArtf(cursor):
        cursor.execute("SELECT * FROM Artefacts WHERE category='Daggers';")
        results = cursor.fetchall()
        cursor.close()
        return results;

def bronzeArtf(cursor):
        cursor.execute("SELECT count(Material) FROM Artefacts WHERE Material='Bronze';")
        results = cursor.fetchall()
        cursor.close()
        return results;

def provenanceUnkn(cursor):
        cursor.execute("SELECT *  FROM Artefacts  WHERE provenance='' OR provenance='Unknown' OR provenance LIKE '%?' OR provenance LIKE '%?%';")
        results = cursor.fetchall()
        cursor.close()
        return results;


import sqlite3
connection = sqlite3.connect("cutting_edge.db")
cursor = connection.cursor()
connection.close()