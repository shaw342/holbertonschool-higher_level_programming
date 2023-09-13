#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb as MC
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    States = session.query(State).order_by(State.id).first()
    if States:
        print("{}: {}".format(States.id, States.name))
    else:
        print("Nothing")
    session.close()
