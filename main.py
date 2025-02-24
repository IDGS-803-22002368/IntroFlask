from flask import Flask, render_template, request, url_for

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
    resultado = 0
    mensaje = "El resultado de "
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        tipo = request.form.get('tipo')
        if num2 == "" or num1 == "":
            mensaje = "No puedes tener campos vacios"    
        elif tipo == 'suma':
            resultado = int(num1) + int(num2)
            mensaje = mensaje + "la suma de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'resta':
            resultado = int(num1) - int(num2)
            mensaje = mensaje + "la resta de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'multiplicacion':
            resultado = int(num1) * int(num2)
            mensaje = mensaje + "la multiplicacion de " + num1 + " y " + num2 + " es: " + str(resultado)
        elif tipo == 'division':
            if num2 == '0':
                resultado = "No se puede dividir entre 0"
                mensaje = f"No se puede dividir entre 0"
            else:
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


@app.route("/cine", methods=['GET', 'POST'])
def cine():
    return render_template("cine.html")


@app.route("/procesarBoleto", methods=['GET', 'POST'])
def procesarBoleto():
    mensaje = ""
    descuento_total = 0
    precio = 12
    subtotal = 0
    total = 0
    if request.method == "POST":
        nombre = request.form.get('nombre')
        cantidad_compradores = float(request.form.get('cantidad_compradores'))
        tarjeta = request.form.get('tarjeta')
        cantidad_boletos = float(request.form.get('cantidad_boletos'))
        validar_compra = 7 * cantidad_compradores
        if cantidad_boletos > validar_compra:
            mensaje = f"No puedes comprar mas de {validar_compra} boletos"
        else:
            if cantidad_boletos > 5:
                descuento_total = descuento_total + 0.15
            elif cantidad_boletos > 2 and cantidad_boletos < 5:
                descuento_total = descuento_total + 0.10
            elif cantidad_boletos < 3:
                descuento_total = descuento_total
            else:
                descuento_total = descuento_total
            if tarjeta == "si":
                descuento_total = descuento_total + 0.10
            else:
                descuento_total = descuento_total
            
            subtotal = cantidad_boletos * precio
            total = subtotal - (subtotal * descuento_total)
            mensaje = f"{nombre} tu compra ha sido exitosa, el total a pagar es: {total} y tu total de boletos es {cantidad_boletos}"
        return render_template("cine.html", nombre=nombre, cantidad_compradores=cantidad_compradores, tarjeta=tarjeta, cantidad_boletos=cantidad_boletos, mensaje=mensaje, descuento_total=descuento_total, subtotal=subtotal, total=total)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
