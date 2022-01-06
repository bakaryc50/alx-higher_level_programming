#!/usr/bin/python3
""" Script that list all states from a MySQL db on localhost at port 3306 """

import MySQLdb
import sys


def list_all_states():
    """ lists all states in db """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password, db=db_name, port=port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    cursor.close()
    db.close()

    if __name__ == '__main__':
        list_all_states()
