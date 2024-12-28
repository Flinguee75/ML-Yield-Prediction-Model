from faker import Faker
from datetime import datetime
import random
from app import app, db
from models import Region, Espece, Meteorologie, Statistique

fake = Faker()

# Générer des données pour la table Regions
def generate_regions_data():
    regions = [
        {'id_region': 1, 'nom_region': 'Abidjan'},
        {'id_region': 2, 'nom_region': 'Bouaké'},
        {'id_region': 3, 'nom_region': 'Daloa'},
        {'id_region': 4, 'nom_region': 'Yamoussoukro'},
        {'id_region': 5, 'nom_region': 'San-Pédro'},
        {'id_region': 6, 'nom_region': 'Korhogo'},
        {'id_region': 7, 'nom_region': 'Man'},
        {'id_region': 8, 'nom_region': 'Divo'},
        {'id_region': 9, 'nom_region': 'Gagnoa'},
        {'id_region': 10, 'nom_region': 'Soubré'}
    ]
    return regions

# Générer des données pour la table Especes
def generate_especes_data():
    especes = [
        {'id_espece': 1, 'nom_espece': 'Cacao'},
        {'id_espece': 2, 'nom_espece': 'Café'},
        {'id_espece': 3, 'nom_espece': 'Hévéa'},
        {'id_espece': 4, 'nom_espece': 'Palmier à huile'},
        {'id_espece': 5, 'nom_espece': 'Coton'},
        {'id_espece': 6, 'nom_espece': 'Anacarde'},
        {'id_espece': 7, 'nom_espece': 'Banane'},
        {'id_espece': 8, 'nom_espece': 'Mangue'},
        {'id_espece': 9, 'nom_espece': 'Maïs'},
        {'id_espece': 10, 'nom_espece': 'Riz'}
    ]
    return especes

# Générer des données pour la table Meteorologie
def generate_meteo_data(num_records):
    meteo_data = []
    for _ in range(num_records):
        meteo_data.append({
            'pluviometrie': round(random.uniform(50.0, 200.0), 2),
            'temperature_min': round(random.uniform(15.0, 25.0), 2),
            'temperature_max': round(random.uniform(25.0, 35.0), 2),
            'id_region': random.randint(1, 10),
            'date_meteo': fake.date_between(start_date='-2y', end_date='today')
        })
    return meteo_data

# Générer des données pour la table Statistique avec des relations logiques
def generate_statistique_data(num_records):
    statistique_data = []
    for _ in range(num_records):
        id_region = random.randint(1, 10)
        id_espece = random.randint(1, 10)
        pluviometrie_moyenne = round(random.uniform(50.0, 200.0), 2)
        temperature_moyenne = round(random.uniform(20.0, 30.0), 2)
        taux_survie_plants = round(random.uniform(50.0, 100.0), 2)
        
        # Calculer le rendement moyen en fonction des autres variables
        rendement_moyen = round((pluviometrie_moyenne / 200.0) * (temperature_moyenne / 30.0) * (taux_survie_plants / 100.0) * 10, 2)
        
        statistique_data.append({
            'id_region': id_region,
            'id_espece': id_espece,
            'pluviometrie_moyenne': pluviometrie_moyenne,
            'temperature_moyenne': temperature_moyenne,
            'taux_survie_plants': taux_survie_plants,
            'rendement_moyen': rendement_moyen,
            'annee': random.randint(2018, 2023)
        })
    return statistique_data

# Insérer les données générées dans la base de données
def insert_data():
    with app.app_context():
        # Insérer les données dans la table Regions
        regions_data = generate_regions_data()
        for data in regions_data:
            region = Region(**data)
            db.session.add(region)
        
        # Insérer les données dans la table Especes
        especes_data = generate_especes_data()
        for data in especes_data:
            espece = Espece(**data)
            db.session.add(espece)
        
        # Insérer les données dans la table Meteorologie
        meteo_data = generate_meteo_data(100)
        for data in meteo_data:
            meteo = Meteorologie(**data)
            db.session.add(meteo)
        
        # Insérer les données dans la table Statistique
        statistique_data = generate_statistique_data(100)
        for data in statistique_data:
            statistique = Statistique(**data)
            db.session.add(statistique)
        
        db.session.commit()

