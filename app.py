# Importar las librerias  
from flask import Flask, render_template 

# Inicializar la aplicacion de flask 
app = Flask(__name__)

# Crear nuestra primera ruta 
@app.route('/ejemplo')
def ejemplo (): 
    print ('holis')
    return 'Hola mundo desde penguin' 

@app.route('/render_template')
def render_template (): 
    return render_template('ejemplo1.html')

@app.route('/enviar_datos')
def enviar_datos():
    nombre = "Esteban"
    edad = 20
    return render_template("enviar_datos.html")


# Configuramos para correr con el boton de play
if __name__ == '__main__': 
    app.run (debug=True)

