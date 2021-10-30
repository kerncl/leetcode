import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Person':"""
    CREATE TABLE IF NOT EXISTS Person(
        Id INTEGER PRIMARY KEY ,
        Email varchar (255));"""
}

DATA = {
    'Person data': """
     INSERT INTO 
        Person(Id, Email)
    VALUES 
        (1, 'john@example.com'),
        (2, 'bob@example.com'),
        (3, 'john@example.com');"""
}


def create_connection(file):
    logging.info(f'Create sql db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info(f'Sucessfully conencted to db')
    except Error as e:
        logging.error(f'Unable to connected to db: {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info(f'Succesfully executed query')
    except Error as e:
        logging.error(f'{e} occured')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Done fetch')
        return result
    except Error as e:
        logging.error(f'{e} occured')

if __name__ == '__main__':
    connection = create_connection('person3.sqlite')
    create_query(connection, TABLE['Person'])
    create_query(connection, DATA['Person data'])
    command = """
    DELETE FROM PERSON WHERE Id NOT IN (SELECT MIN(p.ID) FROM (SELECT * FROM Person) p GROUP BY p.Email); 
    """
    create_query(connection, command)