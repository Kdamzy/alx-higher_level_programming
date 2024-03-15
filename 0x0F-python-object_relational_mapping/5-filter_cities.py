#!/usr/bin/python3
""" Script that takes in name of state as an argument and list all cities """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    ad = """SELECT cities.name FROM cities INNER JOIN states 
            ON states.id=cities.state_id WHERE states.name=%s"""
    c.execute(ad, (sys.argv[4], ))
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    c.close()
    db.close()
