import logging
import sqlite3
from sqlite3 import Error

format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Weather': """
    CREATE TABLE IF NOT EXISTS Weather(
        Id INTEGER PRIMARY KEY ,
        RecordDate DATE ,
        Temperature INTEGER);"""
}

DATA = {
    'Weather': """
    INSERT INTO
        Weather (Id, RecordDate, Temperature)
    VALUES 
        (1, '2015-01-01', 10),
        (2, '2015-01-02', 25),
        (3, '2015-01-03', 20),
        (4, '2015-01-04', 30);"""
}

def create_connection(file):
    logging.info(f'Create sql db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info(f'Succefully create db')
    except Error as e:
        logging.error(f'Unable to create db : {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Succesfully executed')
    except Error as e:
        logging.error(f'Fail to executed: {e}')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Succefully fetech')
        return result
    except Error as e:
        logging.error(f'Fail to fetched: {e}')


if __name__ == '__main__':
    connection = create_connection('Weather.sqlite')
    create_query(connection, TABLE['Weather'])
    create_query(connection, DATA['Weather'])
    Command = """
        SELECT
        weather.id AS 'Id'
    FROM
        weather
            JOIN
        weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
            AND weather.Temperature > w.Temperature
    ;"""
    create_read_query(connection, Command)