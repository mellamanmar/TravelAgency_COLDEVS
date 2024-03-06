# TravelAgency_COLDEVS

## Descripción del proyecto

Se realiza con el fin de realizar una API RESTful utilizando Flask para gestionar el booking de tours. La API permitirá a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar), se realizan estas consultas desde la aplicación de Postman sobre los tours y las reservas como prueba técnica de la empresa COLDEVS.


## Funcionalidades
### Tours
<ul>
    <li>Crear un nuevo tour</li>
    <li>Listar todos los tours disponibles</li>
    <li>Actualizar un tour</li>
    <li>Obtener detalles de un tour específico por su id</li>
    <li>Eliminar un tour</li>
</ul>

### Reservas
<ul>
    <li>Crear una nueva reserva</li>
    <li>Listar todos las reservas disponibles</li>
    <li>Obtener las reservas de un usuario</li>
    <li>Cancelar una reserva</li>
</ul>

## Tecnologías utilizadas
<ul>
    <li>Python</li>
    <li>Pip</li>
    <li>Flask</li>
    <li>SQLAlchemy</li>
    <li>Flask-SQLAlchemy</li>
    <li>SQLite</li>
    <li>Virtualenv</li>
    <li>Postman</li>
</ul>

## Uso

Para comenzar se debe activar el entorno virtual en la ruta mediante el comando <b> source bin/activate </b>

Posterior instalar las dependencias desde <b>pip install -r requirements.txt</b>

Luego ejecutar <b>python init_db.py</b> para iniciar la base de datos y <b>python run.py</b> para iniciar el servidor.

Desde Postman probar con la dirección http://127.0.0.1:5000 las siguiente funcionalidades, las cuales se solicitan y ejecutan en formato JSON.

### Tours
POST   http://127.0.0.1:5000/tour (Crear un tour)
GET    http://127.0.0.1:5000/tour (Listar los tours existentes)
GET    http://127.0.0.1:5000/tour/'id' (Obtener los detalles de un tour específico)
PUT    http://127.0.0.1:5000/tour/'id' (Actualizar un tour por su id)
DELETE http://127.0.0.1:5000/tour/'id' (Eliminar un tour por su id)

        {
          "name" : "Medellín local",
          "descrption" : "Tour por Medellin",
          "user_id" : "100000",
          "date" : "20-05-2024"
          }

### Usuario
POST http://127.0.0.1:5000/user (Crear un usuario para relacionarlo con una reserva)
        {
          "user" : "Usuario de prueba" 
          }

### Reservas
POST   http://127.0.0.1:5000/booking/ (Crear un reserva)
GET    http://127.0.0.1:5000/tour/'id_user' (Listar las reservas que tiene un usuario)
DELETE http://127.0.0.1:5000/tour/'id' (Eliminar una reserva)

        {
          "date" : "20-05-2024",
          "quantity" : 5,
          "user_id" : 1,
          "tour_id" : 1
          }