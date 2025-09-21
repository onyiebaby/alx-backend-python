import time
import sqlite3 
impoRT functools

def with_db_connection(func):
    """Decorator to open and close a database connection automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("mydb.sqlite3")  # Change database name as needed
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=2):
    """Decorator to retry a function on failure due to transient errors."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except sqlite3.OperationalError as e:  # handles transient DB errors
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                except Exception as e:
                    # If it's a non-transient error, stop immediately
                    raise e
            # If all retries fail, raise last exception
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
