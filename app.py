from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL

app = Flask (__name__)
app.config ['MYSQL_HOST'] ='localhost'
app.config ['MYSQL_USER'] ='root'
app.config ['MYSQL_PASSWORD'] =''
app.config ['MYSQL_DB'] =' DB_Floreria'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

@app.route('/')
def index():
    CC = mysql.connection.cursor();
    CC.execute('select*from tbFlores')
    CFlores= CC.fetchall()
    print(CFlores)
    rerturn render_template('index', listFLores= CFlores)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VNombre=request.form['txtNombre']
        Vcantidad=request.form['txtcantidad']
        Vprecio=request.form['txtprecio']

        BB= mysql.connection.cursor()
        BB.execute('insert into tbFlores (Nombre, cantidad, precio) values (%s,%s, %s)',(VNombre, Vcantidad, Vprecio))
        mysql.connection.commit()

        flash('Guardado')
        return redirect(url_for('index'))
    


@app.route('/consulta', methods=['POST'])
def consulta():
    if request.method == 'POST':
        VNombre=request.form['txtNombre']
        cantidad=request.form['txtcantidad']
        precio=request.form['txtprecio']

        BB= mysql.connection.cursor()
    




@app.route('/eliminarc/<id>')
def eliminarc(id):
    CB= mysql.connection.cursor()
    CB.execute('SELECT*FROM tbFlores WHERE id=%s', (id,))
    eliminarcID= CB.fetchone()
    return render_template('eliminar.html', eliminar=eliminarcID)


@app.route('/borrar/<id>', methods = ['POST'])
def borrar(id):

    if request.method == 'POST':
        BR = mysql.connection.cursor()
        BR.execute ('DELETE FROM tbFlores where id = %s',(id,))
        mysql.connection.commit()
        flash('Se elimino correctamente')
        return redirect(url_for('index'))


if __name__== '__main__':
 app.run(port= 5000, debug=True)
    #Crea un formulario en una vista para ingresar datos a la tabla d.
    # # Se necesita un lugar para consultar todos los registros y eliminar unoen específico después de una confirmación