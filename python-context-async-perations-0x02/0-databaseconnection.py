import sqlite3

class DatabaseConnection:
    """Custom context manager to handle database connections automatically."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_name)
        return self.conn   # return the connection so it can be used inside 'with'

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit if no exception, otherwise rollback
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            print(f"Error occurred: {exc_value}")
        # Close the connection in any case
        self.conn.close()


# ✅ Usage
with DatabaseConnection("mydb.sqlite3") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
