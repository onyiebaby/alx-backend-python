#!/usr/bin/python3
import mysql.connector

def stream_users():
    """
    Generator that streams rows from the user_data table one by one
    """
    # connect to ALX_prodev database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # change if your MySQL username is different
        password="yourpassword",  # replace with your MySQL root password
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)  # dictionary=True gives us dict rows
    cursor.execute("SELECT * FROM user_data;")

    # single loop, yielding rows one by one
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
