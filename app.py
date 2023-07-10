from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import pymysql

# Configuración de la base de datos
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_NAME = 'form'

# Configuración de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de SQLAlchemy y Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelo de la tabla 'formulario'
class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

# Esquema de serialización con Marshmallow
class FormularioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono')

formulario_schema = FormularioSchema()
formularios_schema = FormularioSchema(many=True)

# Crear la base de datos si no existe
def crear_basedatos():
    connection = pymysql.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD)
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    connection.close()

# Ruta para guardar los datos del formulario
@app.route('/form', methods=['POST'])
def guardar_formulario():
    nombre = request.json['nombre']
    telefono = request.json['telefono']

    nuevo_formulario = Formulario(nombre=nombre, telefono=telefono)
    db.session.add(nuevo_formulario)
    db.session.commit()

    return formulario_schema.jsonify(nuevo_formulario)


# Ruta para obtener todos los formularios guardados
@app.route('/form', methods=['GET'])
def obtener_formularios():
    formularios = Formulario.query.all()
    result = formularios_schema.dump(formularios)
    return jsonify(result)

# # Ruta para obtener reporte todos los formularios guardados
# @app.route('/reporte', methods=['GET'])
# def obtener_reporte():
#     formularios = Formulario.query.all()
#     reporte = [{'nombre': formulario.nombre, 'telefono': formulario.telefono} for formulario in formularios]
#     return jsonify(reporte)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file('form.html')

# Configuración CORS
CORS(app)



if __name__ == '__main__':
    crear_basedatos()
    with app.app_context():
        db.create_all()

    app.run(port=5000, debug=True)
