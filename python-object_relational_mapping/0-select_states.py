#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM states;")
    my_liste = cursor.fetchall()
    for x in my_liste:
        print(x)
cursor.close()
conn.close()