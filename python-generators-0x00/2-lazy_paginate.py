#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily paginates user_data table
    Fetches the next page only when needed
    """
    offset = 0
    while True:  # one loop only
        page = paginate_users(page_size, offset)
        if not page:  # stop if no more data
            break
        yield page
        offset += page_size
