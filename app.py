# Importar las librerias  
from flask import Flask, render_template 
import requests

# Inicializar la aplicacion de flask 
app = Flask(__name__)

# Crear nuestra primera ruta 
@app.route('/ejemplo')
def ejemplo (): 
    print ('holis')
    return 'Hola mundo desde penguin' 

@app.route('/render_template')
def render_template_ejemplo (): 
    return render_template('ejemplo1.html')

@app.route('/enviar_datos')
def enviar_datos():
    nombre = "Jazmin"
    edad = 20
    return render_template("enviar_datos.html", nombre=nombre, edad=edad)

@app.route('/rick_and_morty')
def rick_and_morty(): 
    # Definimos la url a la que se hace el pedido 
    # Hacemos el pedido para un solo personaje 
    url = 'https://rickandmortyapi.com/api/character/1'
    
    # Hacemos el pedido a la API -- nos devuelve un diccionario
    respuesta_api = requests.get(url).json()
    
    # Creamos variables con los datos de la respuesta 
    nombre = respuesta_api['name']
    estado = respuesta_api['status']
    url_imagen = respuesta_api['image']

    # Enviamos los datos a la tarjet en html 
    return render_template('tarjeta_personaje.html', nombre=nombre, estado=estado, url_imagen=url_imagen)

@app.route('/lista_de_personajes')
def lista_de_personajes(): 
     # Definimos la url a la que se hace el pedido 
    # Hacemos el pedido para un solo personaje 
    url = 'https://rickandmortyapi.com/api/character/'
    
    # Hacemos el pedido a la API -- nos devuelve un diccionario
    respuesta_api = requests.get(url).json()
    
    lista_de_personajes = respuesta_api['results']
    print(lista_de_personajes)

    # Enviamos los datos a la tarjeta en html 
    return render_template('lista_de_personajes.html', lista_de_personajes=lista_de_personajes )

# Configuramos para correr con el boton de play
if __name__ == '__main__': 
    app.run (debug=True)

