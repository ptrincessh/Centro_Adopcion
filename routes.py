from flask import Flask, render_template, request, redirect, url_for
import database
import models

app = Flask(__name__)

@app.route('/')
def index():
    try:
        dogs_data = database.get_available_dogs()
        available_dogs = [models.Dog(row[0], row[1], row[2], row[3]) for row in dogs_data]
        return render_template('catalogo.html', dogs=available_dogs)
    except Exception as e:
        return f"Error al cargar el catálogo: {e}", 500

@app.route('/adoptar/<int:dog_id>')
def form_adopcion(dog_id):
    dog = database.get_dog_by_id(dog_id)
    if not dog:
        return "Perrito no encontrado.", 404
    dog_obj = models.Dog(dog[0], dog[1], dog[2], dog[3])
    return render_template('confirmacion.html', dog=dog_obj)

@app.route('/historial')
def historial():
    adopciones = database.get_adoption_history()
    # Pasamos la lista de adopciones al HTML
    return render_template('historial.html', adopciones=adopciones)
    
@app.route('/confirmar_adopcion', methods=['POST'])
def procesar_adopcion():
    dog_id = request.form['dog_id']
    name = request.form['name']
    lastname = request.form['lastname']
    address = request.form['address']
    id_card = request.form['id_card']
    
    success = database.register_adoption_transactional(dog_id, name, lastname, address, id_card)
    
    if success:
        # REDIRECCIÓN AUTOMÁTICA AL HISTORIAL
        return redirect(url_for('historial'))
    else:
        return "<h2>Error al procesar la adopción.</h2><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)