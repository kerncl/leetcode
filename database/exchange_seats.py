import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'seat': """
    CREATE TABLE IF NOT EXISTS seat(
        id INTEGER ,
        student varchar (255));"""
}

DATA = {
    'seat data':"""
    INSERT INTO
        seat(id, student)
    VALUES 
        (1, 'Abbot'),
        (2, 'Doris'),
        (3, 'Emerson'),
        (4, 'Green'),
        (5, 'Jeames')"""
}


def create_connection(file):
    logging.info(f'Create sqlite db: sqlite_database/{file}')
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info(f'Succesfully Created db')
    except Error as e:
        logging.error(f'Unable to create database: {e}')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Excuted succefully')
    except Error as e:
        logging.error(f'Fail to executed: {e}')


def create_read_query(connection, query):
    logging.info(f'SQL Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info('Excuted succefully')
        return result
    except Error as e:
        logging.error(f'Fail to executed: {e}')


if __name__ == '__main__':
    connection =  create_connection('seat.sqlite')
    create_query(connection, TABLE['seat'])
    create_query(connection, DATA['seat data'])
    Command = """
        select
        (case
            when (id%2) !=0 AND counts != id then id + 1
            when (id%2) !=0 AND counts = id then id
            else id -1
        end) as id,
        student
    from
         seat, (select
                       count(*) as counts
             from seat) as seat_counts
    order by id ASC"""
    create_read_query(connection, Command)