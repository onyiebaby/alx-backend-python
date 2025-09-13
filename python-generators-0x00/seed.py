#!/usr/bin/python3
import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to MySQL server (no database yet)."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # replace with your MySQL root password if any
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()
    print("Database ALX_prodev created successfully")

def connect_to_prodev():
    """Connect to ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create user_data table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    """Insert data from CSV file into user_data table."""
    cursor = connection.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Ensure user_id exists or generate one
            user_id = row.get('user_id') or str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            
            # Insert if not exists
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))
    connection.commit()
    cursor.close()
    print("Data inserted successfully")

def stream_rows(connection):
    """Generator that yields rows one by one from user_data."""
    cursor = connection.cursor(dictionary=True)  # dict for easy access
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
