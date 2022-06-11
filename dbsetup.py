# Author : Nemuel Wainaina

import psycopg2 as psy

conn = psy.connect(
    user='postgres',
    password='password123' 
)

curs = conn.cursor()

q0 = 'CREATE DATABASE fdbackdb;'
q1 = '''CREATE TABLE feedback(
        date VARCHAR(10), 
        time VARCHAR(10), 
        name VARCHAR(15), 
        email VARCHAR(20), 
        mobile VARCHAR(15),
        message TEXT
    );'''

curs.execute(q0)
curs.execute(q1)

curs.close()
conn.close()