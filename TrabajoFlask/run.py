import os

from flask import Flask, render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "BD\lista.db"))
print(database_file)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Tarea(db.Model):
    id = db.Column(db.Integer, unique =True, nullable=False, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<Nombre: {}>".format(self.nombre)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        db.session.add(Tarea(nombre=request.form.get("tarea")))
        db.session.commit()
    tareas = Tarea.query.all()
    return render_template("home.html", tareas=tareas)
if __name__ == '__main__':
    app.run(debug=True)

