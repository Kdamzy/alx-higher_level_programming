#!/usr/bin/python3
""" script that print the first state object from the database """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).first()
    if records is None:
        print("Nothing")
    else:
        print(records.id, records.name, sep=": ")
