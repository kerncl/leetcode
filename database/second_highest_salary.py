from sqlite3 import Error
import sqlite3
import logging


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'employee': """
    CREATE TABLE IF NOT EXISTS Employee(
        Id INTEGER ,
        Salary INTEGER );"""
}

DATA = {
    'employee': """
    INSERT INTO
        Employee(Id, Salary)
    VALUES 
        (1, 100),
        (2, 200),
        (3, 300)"""
}


def create_connection(file):
    logging.info(f'Creating sqlite database: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succefully created db')
    except Error as e:
        logging.error(f'Unable to create db: {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Successfully executed')
    except Error as e:
        logging.error(f'Executed error: {e}')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Succefully feteched')
        return result
    except Error as e:
        logging.error(f'Failed to fetch: {e}')


if __name__ == '__main__':
    connection = create_connection('Employee2.sqlite')
    create_query(connection, TABLE['employee'])
    create_query(connection, DATA['employee'])
    command = 'select ifnull( (select DISTINCT Salary From Employee order by Salary DESC limit 1 offset 1), NULL) as SecondHighestSalary'
    create_read_query(connection, command)