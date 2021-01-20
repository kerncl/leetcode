import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'courses': """
    CREATE TABLE IF NOT EXISTS courses(
        student varchar (255),
        class varchar (255));"""
}

DATA = {
    'courses': """
    INSERT INTO 
        courses(student, class)
    VALUES 
        ('A', 'Math'),
        ('B', 'English'),
        ('C', 'Math'),
        ('D', 'Biology'),
        ('E', 'Math'),
        ('F', 'Computer'),
        ('G', 'Math'),
        ('H', 'Math'),
        ('I', 'Math')"""
}


def create_connection(file):
    logging.info(f'Creating db sqlite: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succeful create db')
    except Error as e:
        logging.error(f'Unable to create db: {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Succefully execute')
    except Error as e:
        logging.error(f'Fail to executed: {e}')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Succefully fetched')
        return result
    except Error as e:
        logging.error(f'Fail to fetch data : {e}')


if __name__ == '__main__':
    connection = create_connection('courses.sqlite')
    create_query(connection, TABLE['courses'])
    create_query(connection, DATA['courses'])
    command = 'select class from courses GROUP BY  class having COUNT(distinct student)>= 5'
    create_read_query(connection, command)
