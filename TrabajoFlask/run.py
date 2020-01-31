import os

from flask import Flask, render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "../BD/lista.db"))

app = Flask(__name__)
app.config["SQL_ALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Tareas(db.Model):
    id = db.Column(db.Integer, unique =True, nullable=False, primary_key=True, sqlite_autoincrement=True)
    tarea = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        tareas = Tareas(tarea=request.form.get("tarea"))
        db.session.add(tareas)
        db.session.commit()
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

