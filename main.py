from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola mundo!!! Nuevo'


@app.route('/hola')
def hola():
    return 'Hola!!!'


@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"


@app.route("/numero/<int:num>")
def numero(num):
    return f"Numero: {num}"


@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Hola {user}!!! Tu id es: {id}"


@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    return f"La suma es: {num1 + num2}"


@app.route("/default")
@app.route("/default/<string:nombre>")
def func(nombre='Alexis'):
    return "El nombre de nom es " + nombre


if __name__ == '__main__':
    app.run(debug=True, port=3000)
