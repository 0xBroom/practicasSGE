from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    tasks = ["prueba"]
    #session['tasks'] = []
    return render_template('home.html')

@app.route("/add")
def addTask():

    tasks = []
    task = str(request.args.get('d',0))

    if str(task) == "":
        return ""
    else:
        #home().tasks.append(task)
        tasks.append(task)
        return task



if __name__ == '__main__':
    app.run(debug=True)