import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Department': """
    CREATE TABLE IF NOT EXISTS department(
        id INTEGER ,
        revenue INTEGER ,
        month varchar(5) );"""
}

DATA = {
    'Department data':"""
    INSERT INTO
        department(id, revenue, month)
    VALUES 
        (1, 8000, 'Jan'),
        (2, 9000, 'Jan'),
        (3, 10000, 'Feb'),
        (1, 7000, 'Feb'),
        (1, 6000, 'Mar')
        """
}

def create_connection(file):
    connection = None
    logging.info(f'Create sql db: sqlite_databse/{file}')
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succesfully connected to database')
    except Error as e:
        logging.error(f'Unable to connected to database : {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Succefully executed query')
    except Error as e:
        logging.error(f'Fail to executed query with {e}')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Succefully executed query')
        return result
    except Error as e:
        logging.error(F'Feteched problem: {e}')

if __name__ == '__main__':
    connection = create_connection('department.sqlite')
    create_query(connection, TABLE['Department'])
    create_query(connection, DATA['Department data'])
