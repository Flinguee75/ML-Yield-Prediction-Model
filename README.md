# Projet : Tableau de bord interactif pour Inad-Ci

## Description du projet

Le projet vise à concevoir un tableau de bord interactif pour l’entreprise ivoirienne **Inad-Ci**, qui permettra de :

- Suivre l’évolution des plantations.
- Intégrer des données météorologiques.
- Fournir des statistiques clés pour une meilleure prise de décision.

L’application sera une **application web** construite avec :

- **Python (Flask)** pour le backend.
- **HTML, CSS, JavaScript** pour le frontend.
- Une base de données relationnelle **PostgreSQL** pour le stockage des informations.

---

## Fonctionnalités principales

1. **Tableau de bord interactif** :
   - Visualisation des plantations et de leur état (progression, statut : vivante, morte, etc.).
   - Cartes interactives pour localiser les plantations.
2. **Données météorologiques** :
   - Affichage des conditions climatiques locales.
   - Historique des données météorologiques par emplacement.
3. **Statistiques clés** :
   - Analyse des données de performance des plantations.
   - Graphiques et tableaux comparatifs.
4. **Gestion des utilisateurs** :
   - Authentification et autorisation.
   - Rôles administratifs pour gérer les données.

---

## Technologies utilisées

### Backend

- **Flask** : Framework web léger pour Python.
- **SQLAlchemy** : ORM pour interagir avec PostgreSQL.
- **Flask-WTF** : Gestion des formulaires.
- **Flask-RESTful** : Création d’API REST.
- **Flask-CORS** : Gestion des permissions inter-domaines (CORS).

### Frontend

- **HTML5** : Structure des pages web.
- **CSS3** : Design et mise en forme.
- **JavaScript** : Interactivité et manipulation dynamique des éléments.
- **Bibliothèques front-end** :
  - [Chart.js](https://www.chartjs.org/) pour les graphiques.
  - [Leaflet](https://leafletjs.com/) pour les cartes interactives.

### Base de données

- **PostgreSQL** : Système de gestion de base de données relationnelle robuste.

---

## Installation et exécution

### Prérequis

- Python 3.8 ou supérieur.
- PostgreSQL installé et configuré.
- Un gestionnaire de paquets comme `pip` ou `pipenv`.

### Étapes d’installation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/votre-repertoire/inad-ci-dashboard.git
   cd inad-ci-dashboard
   ```

2. **Créer et activer l’environnement virtuel** :

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate   # Windows
   ```

3. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données** :

   - Créer une base de données PostgreSQL.
   - Mettre à jour le fichier `config.py` avec les informations de connexion (nom de la base, utilisateur, mot de passe).

5. **Initialiser la base de données** :

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Lancer l’application** :

   ```bash
   flask run
   ```

   L’application sera accessible sur `http://127.0.0.1:5000`.

---


## Auteurs

- **Loic Abby** : Développeur backend.
- **Cisse Tidiane** : Développeur frontend.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d’informations.

