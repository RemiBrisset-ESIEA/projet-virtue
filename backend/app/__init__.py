# Initialisation de l'application Platinium
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialisation de l'application Flask
app = Flask("Platinium")
CORS(app)

# Configuration Flask importée depuis config.py
app.config.from_object("app.config.Config")

# Initialisation de SQLAlchemy
db = SQLAlchemy(app)

# Importation des routes pour les lier à l'application
from app.routes import register_routes
register_routes(app)