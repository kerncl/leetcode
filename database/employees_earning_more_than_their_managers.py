import logging
import sqlite3
from sqlite3 import Error

format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Employee': """
    CREATE TABLE IF NOT EXISTS Employee (
        Id INTEGER PRIMARY KEY ,
        Name varchar (255),
        Salary INTEGER,
        ManagerId INTEGER );"""
}

DATA = {
    'Employee data': """
    INSERT INTO
        Employee(Id, Name, Salary, ManagerId)
    VALUES 
        (1, 'Joe', 70000, 3),
        (2, 'Henry', 80000, 4),
        (3, 'Sam', 60000, Null),
        (4, 'Max', 90000, NULL);"""
}


def create_connection(file):
    logging.info(f'Create sql db: sql_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/'+ file)
        logging.info('Successfully connected')
    except Error as e:
        logging.error(f"Unable to connected to database with {e}")
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info(f'Query executed successfully')
    except Error as e:
        logging.error(f'{e} occured')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Successfully fetched data')
        return result
    except Error as e:
        logging.error(f'{e} occured')


if __name__ == '__main__':
    connection = create_connection('employee.sqlite')
    create_query(connection, TABLE['Employee'])
    create_query(connection, DATA['Employee data'])
    command = """
    SELECT a.Name AS Employee 
        FROM Employee AS a, Employee AS b 
            WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;"""
    results = create_read_query(connection, command)
    for result in results:
        logging.info(result)
        