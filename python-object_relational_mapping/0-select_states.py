#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, password=password, db=database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states;")
    my_liste = cursor.fetchall()
    for x in my_liste:
        print(x)
