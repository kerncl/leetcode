import logging
import sqlite3
from sqlite3 import Error

format = '%(asctime)s :%(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

table = {
    'World': """
    CREATE TABLE IF NOT EXISTS World(
        name TEXT NOT NULL PRIMARY KEY,
        continent TEXT,
        area INTEGER ,
        population INTEGER ,
        gdp INTEGER 
    );"""
}

data = {
    'World data': """
    INSERT INTO
        World (name, continent, area, population, gdp)
    VALUES 
        ('Afghanistan', 'Asia', 652230, 25500100, 20343000),
        ('Albania', 'Europe', 28748, 2831741, 12960000),
        ('Algeria', 'Africa', 2381741, 37100000, 188681000),
        ('Andorra', 'Europe', 468, 78115, 3712000),
        ('Angola', 'Africa', 1246700, 20609294, 100990000);
    """
}


def create_connection(path):
    connection = None
    try:
        logging.info(f'Create sql database: {path}')
        connection = sqlite3.connect(path)
        logging.info('Connection to SQLite DB successful')
    except Error as e:
        logging.error(f'{e} occured')

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        logging.info(f'{query}')
        cursor.execute(query)
        connection.commit()
        logging.info('Query excuted successfully')
    except Error as e:
        logging.error(f'{e} occured')


def excute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        logging.info(f'SQL Command: {query}')
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Done execute query')
        return result
    except Error as e:
        logging.error(f'{e} occured')

if __name__ == '__main__':
    connection = create_connection('sqlite_database/World.sqlite')
    execute_query(connection, table['World'])
    execute_query(connection, data['World data'])
    command = """
    SELECT name, population, area
    FROM World
    WHERE population > 25000000 or area > 3000000;
    """
    results = excute_read_query(connection, command)
    for result in results:
        logging.info(f'{result}')