import os
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


# Conexión con MySQL.
# En local se usan los valores por defecto; en Railway se toman
# de las variables de entorno DB_HOST, DB_USER, DB_PASSWORD, DB_NAME y DB_PORT.
def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "institucion"),
        port=int(os.getenv("DB_PORT", "3306"))
    )


# Página principal
@app.route("/")
def inicio():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aprendices")
    aprendices = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("index.html", aprendices=aprendices)


# Registrar aprendiz
@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO aprendices (nombre, correo)
        VALUES (%s, %s)
    """
    cursor.execute(sql, (nombre, correo))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect("/")


# Eliminar aprendiz (solo por POST)
@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM aprendices WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
