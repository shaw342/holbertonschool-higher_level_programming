#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa: pycode"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, \
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)
    conn.close()