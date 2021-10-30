import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Customers': """
    CREATE TABLE IF NOT EXISTS Customers(
        Id INTEGER PRIMARY KEY ,
        Name varchar (255));""",
    'Orders': """
    CREATE TABLE IF NOT EXISTS Orders(
        Id INTEGER PRIMARY KEY ,
        CustomersId INTEGER );"""
}

DATA = {
    'Customers data':"""
    INSERT INTO
        Customers(Id, Name)
    VALUES 
        (1, 'Joe'),
        (2, 'Henry'),
        (3, 'Sam'),
        (4, 'Max');""",
    'Orders data':"""
    INSERT INTO
        Orders(Id, CustomersId)
    VALUES 
        (1,3),
        (2,1)"""
}


def create_connection(file):
    logging.info(f'Create sqlite db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succefully connected to db')
    except Error as e:
        logging.error(f'Unable to connected to db: {e}')

    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info(f'Successfully executed query')
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
    connection = create_connection('Customer.sqlite')
    create_query(connection, TABLE['Customers'])
    create_query(connection, TABLE['Orders'])
    create_query(connection, DATA['Customers data'])
    create_query(connection, DATA['Orders data'])
    command = """
    SELECT Name as Customers FROM Customers LEFT JOIN Orders on (Customers.Id = Orders.CustomersId) where Orders.Id is NULL;"""
    results = create_read_query(connection, command)
    for result in results:
        logging.info(result)