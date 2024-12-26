from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inad_ci.db'  # Remplacez par votre URI de base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactiver le suivi des modifications

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importer les modèles pour qu'ils soient enregistrés auprès de SQLAlchemy
from web_app.scripts.models import User, Region, Espece, Plantation, Meteorologie, Statistique

# Définir une route de base pour vérifier que l'application fonctionne
@app.route('/')
def index():
    return "Hello, INAD-CI!"

if __name__ == '__main__':
    app.run(debug=True)