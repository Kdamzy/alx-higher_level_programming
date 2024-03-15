#!/usr/bin/python3
""" Script that takes in an argument and display all value in the state """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    ad = "SELECT * FROM states WHERE name LIKE BINARY '{}'"
    c.execute(ad.format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
