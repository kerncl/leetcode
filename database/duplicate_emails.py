import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:S')

table = {
    'Person': """
    CREATE TABLE IF NOT EXISTS Person(
        id INTEGER PRIMARY KEY ,
        Email varchar(255));"""
}

data = {
    'Person data':"""
    INSERT INTO 
        Person(id, Email)
    VALUES 
        (1, 'a@b.com'),
        (2, 'c@d.com'),
        (3, 'a@b.com');"""
}

def create_connection(file):
    logging.info(f'Create sql db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succefully connected db')
    except Error as e:
        logging.error(f'Unable to connect db: {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Query executed successfully')
    except Error as e:
        logging.error(f'{e} occured')

def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Done fetched')
        return result
    except Error as e:
        logging.error(f'{e} occured')


if __name__ == '__main__':
    connection = create_connection('Person.sqlite')
    create_query(connection, table['Person'])
    create_query(connection, data['Person data'])
    command = """
    SELECT Email FROM Person GROUP BY Email having COUNT(Email) > 1;"""
    results = create_read_query(connection, command)
    for result in results:
        logging.info(result)

    command2 = """
    SELECT Email FROM (
        SELECT Email, COUNT(Email) as num FROM Person) WHERE num > 1;"""
    results = create_read_query(connection, command2)
    for result in results:
        logging.info(result)