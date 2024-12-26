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

# Définir la table Regions
class Region(db.Model):
    __tablename__ = 'regions'
    id_region = db.Column(db.Integer, primary_key=True)
    nom_region = db.Column(db.String(100), nullable=False)

# Définir la table Especes
class Espece(db.Model):
    __tablename__ = 'especes'
    id_espece = db.Column(db.Integer, primary_key=True)
    nom_espece = db.Column(db.String(100), nullable=False)
    type_espece = db.Column(db.String(50))

# Définir la table Plantations
class Plantation(db.Model):
    __tablename__ = 'plantations'
    id_plantation = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    superficie = db.Column(db.Float, nullable=False)
    id_espece = db.Column(db.Integer, db.ForeignKey('especes.id_espece'))
    id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'))

# Définir la table Meteorologie
class Meteorologie(db.Model):
    __tablename__ = 'meteorologie'
    id_meteo = db.Column(db.Integer, primary_key=True)
    pluviometrie = db.Column(db.Float)
    temperature_min = db.Column(db.Float)
    temperature_max = db.Column(db.Float)
    id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'))
    date_meteo = db.Column(db.Date)
    __table_args__ = (db.UniqueConstraint('id_region', 'date_meteo', name='unique_region_date'),)

# Définir la table Statistiques
class Statistique(db.Model):
    __tablename__ = 'statistiques'
    id_stat = db.Column(db.Integer, primary_key=True)
    id_region = db.Column(db.Integer, db.ForeignKey('regions.id_region'))
    id_espece = db.Column(db.Integer, db.ForeignKey('especes.id_espece'))
    pluviometrie_moyenne = db.Column(db.Float)
    temperature_moyenne = db.Column(db.Float)
    taux_survie_plants = db.Column(db.Float)
    rendement_moyen = db.Column(db.Float)
    annee = db.Column(db.Integer)
    __table_args__ = (db.UniqueConstraint('id_region', 'id_espece', 'annee', name='unique_stat'),)

# Créer les tables dans la base de données
with app.app_context():
    db.create_all()