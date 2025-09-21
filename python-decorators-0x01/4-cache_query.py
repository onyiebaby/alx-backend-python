import time
import sqlite3 
import functools

query_cache = {}

def with_db_connection(func):
    """Decorator to open and close a database connection automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("mydb.sqlite3")  # Change db name as needed
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def cache_query(func):
    """Decorator to cache query results based on SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Extract the query argument
        query = kwargs.get("query") if "query" in kwargs else (args[0] if args else None)
        
        if query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]
        
        # Execute the function and store result in cache
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print(f"Cache stored for query: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
