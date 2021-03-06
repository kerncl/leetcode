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
    command = """
    SELECT id,
    sum(case when(month='Jan') then revenue else null end) as Jan_Revenue,
    sum(case when(month='Feb') then revenue else null end) as Feb_Revenue,
    sum(case when(month='Mar') then revenue else null end) as Mar_Revenue,
    sum(case when(month='Apr') then revenue else null end) as Apr_Revenue,
    sum(case when(month='May') then revenue else null end) as May_Revenue,
    sum(case when(month='Jun') then revenue else null end) as Jun_Revenue,
    sum(case when(month='Jul') then revenue else null end) as Jul_Revenue,
    sum(case when(month='Aug') then revenue else null end) as Aug_Revenue,
    sum(case when(month='Sep') then revenue else null end) as Sep_Revenue,
    sum(case when(month='Oct') then revenue else null end) as Oct_Revenue,
    sum(case when(month='Nov') then revenue else null end) as Nov_Revenue,
    sum(case when(month='Dec') then revenue else null end) as Dec_Revenue
    from department group by id"""
    create_query(connection, command)
