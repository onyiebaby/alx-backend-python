import sqlite3

class ExecuteQuery:
    """Custom context manager that manages connection and executes a query."""

    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params else ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Open DB connection
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        # Execute the query with params
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        
        return self.results  # Returned directly to the `with` block

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit if no errors, otherwise rollback
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            print(f"Error occurred: {exc_value}")
        
        # Close cursor and connection
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# ✅ Usage example
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery("mydb.sqlite3", query, params) as results:
    print(results)
