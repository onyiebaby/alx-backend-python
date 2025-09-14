#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """
    Generator that streams user ages one by one from the DB
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:   # 1st loop (generator)
        yield age
    cursor.close()
    connection.close()


def compute_average_age():
    """
    Compute average age using the generator without
    loading the entire dataset into memory
    """
    total, count = 0, 0
    for age in stream_user_ages():   # 2nd loop
        total += age
        count += 1
    return total / count if count else 0


if __name__ == "__main__":
    avg = compute_average_age()
    print(f"Average age of users: {avg}")
