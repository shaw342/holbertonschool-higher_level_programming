#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    connection = MySQLdb.connect(user=username, passwd=password,
                                 db=database, host="localhost",
                                 port=3306)

    cursor = connection.cursor()
    request = "SELECT cities.name FROM cities JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s\
             ORDER BY cities.id"
    cursor.execute(request, (state_name_searched,))

    cityList = cursor.fetchall()
    cl = [cityList]
    cityNames = ', '.join([city[0] for city in cityList])

    print(cityNames.rstrip(', '))

    cursor.close()
    connection.close()
