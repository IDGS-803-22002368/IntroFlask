from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    grupo = "IDGS803"
    listaAlumnos = ["Alexis", "Erick", "Jorge", "Luis", "Miguel", "Oscar", "Ricardo", "Sergio", "Victor"]
    return render_template("index.html", grupo=grupo, listaAlumnos=listaAlumnos)


@app.route("/OperasBas")
def OperasBas():
    return render_template("OperasBas.html")


@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    mensaje = "El resultado de "
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        tipo = request.form.get('tipo')
        if tipo == 'suma':
            resultado = int(num1) + int(num2)
            mensaje = mensaje + "la suma de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'resta':
            resultado = int(num1) - int(num2)
            mensaje = mensaje + "la resta de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'multiplicacion':
            resultado = int(num1) * int(num2)
            mensaje = mensaje + "la multiplicacion de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'division':
            resultado = int(num1) / int(num2)
            mensaje = mensaje + "la division de " + num1 + " y " + num2 + " es: " + str(resultado)
        else:
            resultado = "No se selecciono ninguna operacion"
        return render_template("OperasBas.html", resultado=resultado, num1=num1, num2=num2, mensaje=mensaje)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")


@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

# @app.route('/hola')
# def hola():
#     return 'Hola!!!'

# @app.route("/user/<string:user>")
# def user(user):
#     return f"Hola {user}!!!"

# @app.route("/numero/<int:num>")
# def numero(num):
#     return f"Numero: {num}"

# @app.route("/user/<string:user>/<int:ID>")
# def username(user, ID):
#     return f"Hola {user}!!! Tu id es: {ID}"

# @app.route("/suma/<float:num1>/<float:num2>")
# def suma(num1, num2):
#     return f"La suma es: {num1 + num2}"

# @app.route("/default")
# @app.route("/default/<string:nombre>")
# def func(nombre='Alexis'):
#     return "El nombre de nom es " + nombre

# @app.route("/form1", methods=['GET', 'POST'])
# def form1():
#     return '''
#     <form action="/form1" method="POST">
#         <input type="text" name="nombre">
#         <input type="submit" value="Enviar" onclick="enviar()">
#     </form>
#     <script>
#         nombre = document.querySelector("input[name=nombre]");
#         function enviar() {
#             alert("Hola" + " " + nombre.value);
#         }
#     </script>
# '''


if __name__ == '__main__':
    app.run(debug=True, port=3000)
