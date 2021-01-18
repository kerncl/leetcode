import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')


table = {
    'cinema': """
    CREATE TABLE IF NOT EXISTS cinema(
        id INTEGER PRIMARY KEY,
        movie varchar(255),
        description varchar(255),
        rating float (2,1));"""
}

data = {
    'cinema data': """
    INSERT INTO 
        cinema( id, movie, description, rating)
    VALUES 
        (1, 'War', 'great 3D', 8.9),
        (2, 'Science', 'fiction', '8.5'),
        (3, 'irish', 'boring', 6.2),
        (4, 'Ice song', 'Fantacy', 8.6),
        (5, 'House card', 'Interesting', 9.1);"""
}

def create_connection(file):
    logging.info(f'Create sql db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Successfully connected db')
        return connection
    except Error as e:
        logging.error(f'{e} occured')


def create_query(connection, query):
    cursor = connection.cursor()
    logging.info(f'SQL command: {query}')
    try:
        cursor.execute(query)
        connection.commit()
        logging.info(f'Query executed successfully')
    except Error as e:
        logging.error(f'{e} occured')


def create_read_query(connection, query):
    cursor = connection.cursor()
    logging.info(f'SQL command: {query}')
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info(f'Done fetched')
        return result
    except Error as e:
        logging.error(f'{e} occured ')


if __name__ == '__main__':
    connection = create_connection('cinema.sqlite')
    create_query(connection, table['cinema'])
    create_query(connection, data['cinema data'])
    command = """
    SELECT * FROM cinema
        WHERE id%2 
            AND description != 'boring'
            order by rating DESC;
    """
    results = create_read_query(connection, command)
    for result in results:
        logging.info(f'{result}')