#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa: pycode"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, \
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM states ORDER BY id ASC;")
    my_liste = cursor.fetchall()
    for x in my_liste:
        print(x)

conn.close()