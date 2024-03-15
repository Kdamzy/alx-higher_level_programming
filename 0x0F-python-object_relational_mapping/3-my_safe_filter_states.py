#!/usr/bin/python3
""" Script that takes in an argument and display all value in the state """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    ad = """SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states ON states.id=cities.state_id"""
    c.execute(ad)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
