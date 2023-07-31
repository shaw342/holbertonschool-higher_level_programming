#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb as MC
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]
    conn = MC.connect(port=3306, user=sys.argv[1],
                      password=sys.argv[2], db=sys.argv[3])

    with conn.cursor() as cursor:
        query = "SELECT * FROM states WHERE\
            BINARY name = %s ORDER BY states.id"
        cursor.execute(query, (state_name,))
        my_list = cursor.fetchall()
        for x in my_list:
            print(x)

    conn.close()
