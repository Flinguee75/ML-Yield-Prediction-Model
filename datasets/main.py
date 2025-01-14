import numpy as np
import pandas as pd
import joblib
import math
import os


# Construire les chemins absolus pour les fichiers
current_dir = os.path.dirname(__file__)  # Répertoire contenant le script
model_path = os.path.join(current_dir, "final_model.pkl")
preprocessor_path = os.path.join(current_dir, "preprocessor.pkl")
features_path = os.path.join(current_dir, "features_names.pkl")
selected_features = os.path.join(current_dir, "selected_features.pkl")

# Charger les fichiers
try:
    final_model = joblib.load(model_path)
    print("Modèle chargé avec succès.")

    preprocessor = joblib.load(preprocessor_path)
    print("Préprocesseur chargé avec succès.")

    feature_names = joblib.load(features_path)
    
    print(feature_names)
    print("Noms des caractéristiques chargés avec succès.")


except FileNotFoundError as e:
    print(f"Erreur : {e}")
    print("Assurez-vous que les fichiers sont dans le même répertoire que ce script.")


if not isinstance(feature_names, list):
    raise ValueError("selected_features n'est pas une liste. Vérifiez le contenu.")
else:
    print("Selected features chargées avec succès :")
    
    
    
# Fonction pour prétraiter les données utilisateur
def preprocess_input(form_data, preprocessor, feature_names):
    # Variables utilisateur fournies
   # Variables utilisateur fournies
    input_data = np.array([[
        form_data.get('nom_region', ''),  # Par exemple : 'Abidjan'
        form_data.get('nom_espece', ''),  # Par exemple : 'Cacao'
        form_data.get('superficie',0 ),  # Par exemple : 311.35
        form_data.get('pluviometrie',0 ),  # Par exemple : 221.88
        form_data.get('annee', 2019),  # Par exemple : 2019
        form_data.get('temperature_moyenne',0),  # Par exemple : 25.67
        form_data.get('mois_plantation', 1),  # Par exemple : 4
        form_data.get('log_pluviometrie', 0),  # Par exemple : 5.406634
        form_data.get('categorie_pluviometrie', 'Moyenne')  # Par exemple : 'Moyenne'
    ]])

    # Convertir en DataFrame avec toutes les colonnes nécessaires
    input_df = pd.DataFrame(input_data, columns=feature_names)

    print(input_df)

    # Appliquer le préprocesseur
    input_transformed = preprocessor.transform(input_df)
    
    return input_transformed


# Fonction principale
def main():
    print("Bienvenue dans l'outil de prédiction du rendement moyen !\n")
    
    # Demander les données utilisateur
    nom_region = input("Entrez la région : ")
    nom_espece = input("Entrez l'espèce à planter : ")
    superficie = float(input("Entrez la superficie (en hectares) : "))
    pluviometrie = float(input("Entrez la pluviométrie (en mm) : "))
    temperature_moyenne = float(input("Entrez la température moyenne (en °C) : "))
    mois_plantation = int(input("Entrez le mois de plantation (1-12) : "))
    
    # Construire les données utilisateur
    user_data = {
        'nom_region': nom_region,
        'nom_espece': nom_espece,
        'superficie': superficie,
        'pluviometrie': pluviometrie,
        'annee': 2019,
        'temperature_moyenne': temperature_moyenne,
        'mois_plantation': mois_plantation,
        'log_pluviometrie': math.log(pluviometrie),
    }
    
    # Définir les bins et labels pour pd.cut
    bins = [0, 100, 200, 300, float('inf')]  # Définir les seuils
    labels = ['Faible', 'Moyenne', 'Élevée', 'Très Élevée']  # Étiquettes correspondantes

    # Transformer une valeur unique en série pour utiliser pd.cut
    user_data['categorie_pluviometrie'] = pd.cut(
        [user_data['pluviometrie']], bins=bins, labels=labels
    )[0]  # [0] pour extraire la valeur unique de la série

    # Prétraiter les données
    input_transformed = preprocess_input(user_data, preprocessor, feature_names)
    
    # Faire la prédiction
    
    print(input_transformed)
    
    rendement_tonnes = final_model.predict(input_transformed)[0]
    
    # Convertir en Franc CFA
    prix_par_tonne = 500000  # Exemple : 500 000 FCFA par tonne
    rendement_fcfa = rendement_tonnes * prix_par_tonne
    
    # Afficher le résultat
    print("\nRésultat de la prédiction :")
    print(f"Rendement estimé : {rendement_tonnes:.2f} tonnes/hectare")
    print(f"Valeur estimée en Franc CFA : {rendement_fcfa:,.2f} FCFA\n")

# Exécuter le programme
if __name__ == "__main__":
    main()
