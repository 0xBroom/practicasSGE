from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        tareas = Tareas(title=request.form.get("tarea"))
        db.session.add(tareas)
        db.session.commit()
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)