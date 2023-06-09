# Las importaciones son al reves, primero le dices desde dónde y luego que quieres importar.
from flask import Flask
from flask_cors import CORS

from src.webserver import app

# Cada vez que cambio algo en el código, con debug = True recarga automáticamente los cambios. Esto hace que no tengas que estar cerrando y abriendo el servidor constantemente.
app.run(debug=True)