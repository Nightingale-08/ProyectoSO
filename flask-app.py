import time
import psycopg2
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
try:
 conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
 )
 cursor=conexion.cursor()
 cursor.execute("CREATE TABLE IF NOT EXISTS hits (id INTEGER PRIMARY KEY, count INTEGER); INSERT INTO hits (id, count) VALUES (1, 0) ON CONFLICT DO NOTHING;")
 cursor.close()
 conexion.autocommit = True
 cursor.close() 
except psycopg2.Error as e:  
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
contador =0


@app.route('/')
def hello():
    conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT count FROM hits where id=1")
    row=cursor.fetchone()
    for data in row:
      contador=(row[0])
    return("Contador= {}".format(contador+1))

@app.route('/get', methods=['GET'])
def get_count():
    conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT count FROM hits where id=1")
    row=cursor.fetchone()
    for data in row:
      contador=(row[0])
    return("Contador= {}".format(contador))


@app.route('/put/<int:count>', methods=['PUT'])
def puts(count):
 conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
    )
 cursor=conexion.cursor()
 cursor.execute("UPDATE hits SET count = %s WHERE id = 1", (id,))
 cursor.execute("SELECT count from hits WHERE id=1")
 row=cursor.fetchone()
 for data in row :
    contador=(int(data))

 return("Contador = {}".format(contador))

@app.route('/post/<int:count>', methods=['POST'])
def post(count):
 conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
    )
 cursor=conexion.cursor()
 cursor.execute("UPDATE hits SET count = %s WHERE id = 1", (id,))
 cursor.execute("SELECT count from hits WHERE id=1")
 row=cursor.fetchone()
 for data in row :
    contador=(int(data))

 return("Contador = {}".format(contador))

@app.route('/delete', methods=['DELETE'])
def delete():
 conexion = psycopg2.connect(
    host='localhost',
    user='root',
    password='root',
    database='postgres'
    )
 cursor=conexion.cursor()
 cursor.execute("UPDATE hits SET count = 1 WHERE id = 1")
 cursor.execute("SELECT count from hits WHERE id=1")
 row=cursor.fetchone()
 for data in row :
    contador=(int(data))

 return("Contador = {}".format(contador))

