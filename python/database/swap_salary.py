import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')


table = {
    'salary': """
    CREATE TABLE IF NOT EXISTS salary(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar (100),
        sex char char(1),
        salary int);"""}

data = {
    'salary data': """
    INSERT INTO 
        salary(name, sex, salary)
    VALUES 
        ('A', 'm', 2500),
        ('B', 'f', 1500),
        ('C', 'm', 5500),
        ('D', 'f', 500)
        
    ;"""
}
def create_connection(file):
    connection = None
    try:
        logging.info(f'Create sql db : sqlite_database/{file}')
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Successful Connectedd')
    except Error as e:
        logging.error(f'{e} occured')
    return connection


def create_query(connection, query):
    cursor = connection.cursor()
    try:
        logging.info(f'SQL Command: {query}')
        cursor.execute(query)
        connection.commit()
        logging.info('Query executed succefully')
    except Error as e:
        logging.error(f'{e} occured')


def create_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        logging.info(f'SQL Command: {query}')
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info(f'Done fetched')
        return result
    except Error as e:
        logging.error(f'{e} occured')


if __name__ == '__main__':
    connection = create_connection('salary.sqlite')
    create_query(connection, table['salary'])
    create_query(connection, data['salary data'])
    command = """
    UPDATE salary
        SET salary = CASE salary
            WHEN 'm' THEN 'f'
            ELSE 'm'
            END;
    """
    create_query(connection, command)