import sqlite3 
import functools

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

def transactional(func):
    """Decorator to manage database transactions (commit/rollback)."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()   # Commit if everything worked
            return result
        except Exception as e:
            conn.rollback() # Rollback if an error occurred
            raise e
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

# Example usage
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
