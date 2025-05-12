from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = ''
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 2)
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'
        resultado = f'Promedio: {promedio} - Estado: {estado}'

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = ''
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        resultado = f'Nombre más largo: {nombre_largo} - Caracteres: {len(nombre_largo)}'

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
