from flask import Flask, render_template,request
import mysql.connector

app = Flask (__name__)


@app.route("/")
def inicio():
   return render_template("index.html")

@app.route("/incidencia", methods=["POST"])
def crear_incidencia():
   # Lógica para crear la incidencia
   aula = request.form["aula"]
   usuario = request.form["usuario"]
   descripcion = request.form["descripcion"]

   print("Aula:", aula)
   print("Usuario:", usuario)
   print("Descripción:", descripcion)

   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'incidencias'
   app.config['MYSQL_PASSWORD'] = 'incidencias'
   app.config['MYSQL_DB'] = 'incidencias'

   conexion = mysql.connector.connect(
      host=app.config['MYSQL_HOST'],
      user=app.config['MYSQL_USER'],
      password=app.config['MYSQL_PASSWORD'],
      database=app.config['MYSQL_DB']
   )
   cursor = conexion.cursor()

   sql = """Insert into registro (aula, usuario, descripcion, estado) values (%s, %s, %s, %s)"""
   valores= (aula, descripcion, usuario, "Abierta")
   cursor.execute(sql, valores)
   conexion.commit()
   cursor.close()
   conexion.close()

   return "Incidencia recibida"


if __name__== "__main__":
   app.run(debug=True)