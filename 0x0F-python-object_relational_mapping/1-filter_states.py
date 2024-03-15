#!/usr/bin/python3
""" Script that lists all states with specific name from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    ad = """SELECT * FROM states WHERE name LIKE BINARY
    'N%' ORDER BY states.id"""
    c.execute(ad)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
