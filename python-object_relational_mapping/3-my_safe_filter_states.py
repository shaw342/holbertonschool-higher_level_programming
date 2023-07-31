#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

conn = MySQLdb.connect(
    host="localhost",
    user=username,
    password=password,
    database=database
)

cursor = conn.cursor()

query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id"

cursor.execute(query, (state_name,))

results = cursor.fetchall()

# Traiter les résultats
for row in results:
    print(row)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
