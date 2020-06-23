import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('db.sqlite3')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO alumno VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    con.commit()
