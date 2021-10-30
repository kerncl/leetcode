import logging
import sqlite3
from sqlite3 import Error


format = '%(asctime)s: %(message)s'
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

TABLE = {
    'Person': """
    CREATE TABLE IF NOT EXISTS Person(
        PersonID INTEGER PRIMARY KEY, 
        FirstName varchar (255),
        LastName varchar (255));""",
    'Address': """
    CREATE TABLE IF NOT EXISTS Address(
        AddressID INTEGER PRIMARY KEY ,
        PersonID INTEGER ,
        City varchar (255),
        State varchar (255));"""
}

DATA = {
    'Person data': """
    INSERT INTO 
        Person(PersonID, LastName, Firstname)
    VALUES 
        (1, 'Wang', 'Allen');""",
    'Address data': """
    INSERT INTO 
        Address(AddressID, PersonID, City, State)
    VALUES 
        (1, 2, 'New York City', 'New York');"""
}

def create_connection(file):
    logging.info('Create sql db: sqlite_database/' + file)
    connection = None
    try:
        connection = sqlite3.connect('sqlite_database/' + file)
        logging.info('Succefully connected db')
    except Error as e:
        logging.error(f'{e} occured')
    return connection


def create_query(connection, query):
    logging.info(f'SQL Command : {query}')
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info('Succefully executed query')
    except Error as e:
        logging.error(f'{e} occured')


def create_read_query(connection, query):
    logging.info(f'SQl Command: {query}')
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info(f'Succefully feteched data')
        return result
    except Error as e:
        logging.error(f'{e} occured')


if __name__ == '__main__':
    connection = create_connection('Person2.sqlite')
    create_query(connection, TABLE['Person'])
    create_query(connection, TABLE['Address'])
    create_query(connection, DATA['Person data'])
    create_query(connection, DATA['Address data'])
    command = """
    SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address on Person.PersonID = Address.PersonId"""
    results = create_read_query(connection, command)
    for result in results:
        logging.info(f'{result}')