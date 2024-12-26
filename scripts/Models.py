from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inad_ci.db'  # Remplacez par votre URI de base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactiver le suivi des modifications
db = SQLAlchemy(app)

# Définir la table User
class User(db.Model):
    __tablename__ = 'users'  # Nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    username = db.Column(db.String(100), unique=True, nullable=False)  # Nom d'utilisateur unique
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email unique
    password = db.Column(db.String(200), nullable=False)  # Mot de passe
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())  # Date de création (par défaut, la date du moment)

    # Optionnel : ajouter d'autres champs comme l'adresse, numéro de téléphone, etc.

# Créer les tables dans la base de données
with app.app_context():
    db.create_all()