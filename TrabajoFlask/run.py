import os

from flask import Flask, render_template, redirect
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "BD\lista.db"))
print(database_file)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

''' 
Inicializamos la base de datos.
'''
class Tarea(db.Model):
    id = db.Column(db.Integer, unique =True, nullable=False, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    marcado = db.Column(db.Integer, unique=False, nullable= False, primary_key= False)

    def __repr__(self):
        return "<Nombre: {}>".format(self.nombre)

'''
Ruta por defecto, antes de mostrar la vista verificará la base de datos
en busca de un nuevo elemento en la lista.
'''
@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        tarea = Tarea(nombre=request.form.get("tarea"))
        tarea.marcado = 0
        db.session.add(tarea)
        db.session.commit()
    tareas = Tarea.query.all()
    return render_template("home.html", tareas=tareas)

'''
Maneja la eliminación de la tarea de la base de datos, por id.
'''
@app.route("/delete", methods=["POST"])
def delete():
    id_ = request.form.get("id")
    tarea = Tarea.query.filter_by(id=id_).first()
    db.session.delete(tarea)
    db.session.commit()
    return redirect("/")

'''
Actualiza el campo marcado de la base de datos que hará que en la vista esta tarea se tache.
'''
@app.route("/update", methods=["POST"])
def update():
    id_ = request.form.get("id")
    tarea = Tarea.query.filter_by(id=id_).first()
    tarea.marcado = 1
    db.session.commit()
    return redirect ("/")

if __name__ == '__main__':
    app.run(debug=True)

