from app import app
from flask import render_template, request, redirect, url_for, flash
import csv


ficheromovimientos = 'data/movimientos.txt'


@app.route('/')
def index():
    #leer movimientos
    fMovimientos = open(ficheromovimientos,'r')
    csvreader = csv.reader(fMovimientos, delimiter=',', quotechar='"')
    movements = []
    for movimiento in csvreader:
        movements.append(movimiento)

       

    #enviar movimientos a index.html
    return render_template('index.html', movimientos=movements)

@app.route('/nuevacompra', methods=['GET','POST'])
def compra(): 
    print (request.method)
    if request.method == 'GET': #devuelve el formulario
        return render_template('nuevacompra.html')
    else: #graba el formulario
         #Procesar el error
        msg = validar(request.value)
        if msg =! True:
            return render_template('nuevacompra.html', error=msg)

    
        fMovimientos = open(ficheromovimientos, 'a+') #Lo abre en modo append
        precioUnitario = request.values['cantidadPagada'/ request.values['cantidadComprada']]
        registro = '{}, "{}", {}, {}, {}, {}, {}\n'.format(request.values['fecha'],
            request.values['concepto'],
            request.values['monedaComprada'],
            request.values['cantidadComprada'],
            request.values['monedaPagada'],
            request.values['cantidadPagada'],
            precioUnitario)
        fMovimientos.write(registro)
        fMovimientos.close()
        return redirect(url_for('index')) #redirige a la url de index

def validar(values):
    if values['fecha'] == '':
        return 'Debe informar la fecha'
    
    if values['concepto'] == '':
        return 'Debe informar el concepto'

    if values['cantidadComprada'] == '':
        return 'Debe informar la cantidad comprada'

    if values['cantidadPagada'] == '':
        return 'Debe informar la cantidad pagada'   

    return True 




