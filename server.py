# Author : Nemuel Wainaina

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
import psycopg2 as psy

# obtain and return the current date and time
def curDateTime():
    dt = datetime.now().strftime('%x')
    tm = datetime.now().strftime('%X')
    return dt, tm

# connect to the database and return connection and cursor object
def dbConnect():
    conn = psy.connect(
        database='fdbackdb',
        user='postgres',
        password='password123'
    )
    curs = conn.cursor()
    return conn, curs

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        msg = request.form['msg']
        dt, tm = curDateTime()
        q = 'INSERT INTO feedback VALUES(%s, %s, %s, %s, %s, %s);'
        conn, curs = dbConnect()
        curs.execute(q, (dt, tm, name, email, mobile, msg))
        conn.commit()
        curs.close()
        conn.close()

    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True) # for production, ensure to set debug to False