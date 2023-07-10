from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/form'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class FormularioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono')

formulario_schema = FormularioSchema()
formularios_schema = FormularioSchema(many=True)

@app.route('/form', methods=['POST'])
def guardar_formulario():
    nombre = request.json['nombre']
    telefono = request.json['telefono']

    nuevo_formulario = Formulario(nombre=nombre, telefono=telefono)
    db.session.add(nuevo_formulario)
    db.session.commit()

    return formulario_schema.jsonify(nuevo_formulario)

@app.route('/form', methods=['GET'])
def obtener_formularios():
    formularios = Formulario.query.all()
    result = formularios_schema.dump(formularios)
    return jsonify(result)

@app.route('/reporte', methods=['GET'])
def obtener_reporte():
    formularios = Formulario.query.all()
    data = formularios_schema.dump(formularios)
    return jsonify(data)

CORS(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
