import numpy as np
import pandas as pd
import joblib
import math
import os


# *** Chargement des fichiers nécessaires ***
def load_files():
    # Construire les chemins absolus pour les fichiers
    current_dir = os.path.dirname(__file__)
    paths = {
        "model": os.path.join(current_dir, "final_model.pkl"),
        "preprocessor": os.path.join(current_dir, "preprocessor.pkl"),
        "features": os.path.join(current_dir, "features_names.pkl"),
        "selected_features": os.path.join(current_dir, "selected_features.pkl"),
    }

    # Charger les fichiers
    try:
        final_model = joblib.load(paths["model"])
        print("Modèle chargé avec succès.")

        preprocessor = joblib.load(paths["preprocessor"])
        print("Préprocesseur chargé avec succès.")

        feature_names = joblib.load(paths["features"])
        print("Noms des caractéristiques chargés avec succès.")

        selected_features = joblib.load(paths["selected_features"])
        print("Selected features chargées avec succès.")

        return final_model, preprocessor, feature_names, selected_features
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        print("Assurez-vous que les fichiers sont dans le même répertoire que ce script.")
        raise


# *** Prétraitement des données utilisateur ***
def preprocess_input(form_data, preprocessor, feature_names, selected_features):
    # Construire un tableau avec les données utilisateur
    input_data = np.array([[
        form_data.get('nom_region', ''),
        form_data.get('nom_espece', ''),
        form_data.get('superficie', 0),
        form_data.get('pluviometrie', 0),
        form_data.get('annee', 2019),
        form_data.get('temperature_moyenne', 0),
        form_data.get('mois_plantation', 1),
        form_data.get('log_pluviometrie', 0),
        form_data.get('categorie_pluviometrie', 'Moyenne')
    ]])

    # Convertir en DataFrame avec les colonnes nécessaires
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # Appliquer le préprocesseur
    input_transformed = preprocessor.transform(input_df)

    # Convertir les noms de colonnes en indices si nécessaire
    if isinstance(selected_features[0], str):
        feature_indices = [list(preprocessor.get_feature_names_out()).index(col) for col in selected_features]
    else:
        feature_indices = selected_features

    # Sélectionner les colonnes dans la matrice transformée
    input_transformed = input_transformed[:, feature_indices]

    return input_transformed


# *** Fonction principale ***
def main():
    # Charger les fichiers nécessaires
    final_model, preprocessor, feature_names, selected_features = load_files()

    print("Bienvenue dans l'outil de prédiction du rendement moyen !\n")

    # Collecte des données utilisateur
    user_data = {
        'nom_region': input("Entrez la région : "),
        'nom_espece': input("Entrez l'espèce à planter : "),
        'superficie': float(input("Entrez la superficie (en hectares) : ")),
        'pluviometrie': float(input("Entrez la pluviométrie (en mm) : ")),
        'temperature_moyenne': float(input("Entrez la température moyenne (en °C) : ")),
        'mois_plantation': int(input("Entrez le mois de plantation (1-12) : ")),
    }

    # Calcul des colonnes supplémentaires
    user_data['log_pluviometrie'] = math.log(user_data['pluviometrie'])

    # Définir les catégories de pluviométrie
    bins = [0, 100, 200, 300, float('inf')]
    labels = ['Faible', 'Moyenne', 'Élevée', 'Très Élevée']
    user_data['categorie_pluviometrie'] = pd.cut(
        [user_data['pluviometrie']], bins=bins, labels=labels
    )[0]

    # Prétraiter les données utilisateur
    input_transformed = preprocess_input(user_data, preprocessor, feature_names, selected_features)

    # Faire la prédiction
    rendement_tonnes = final_model.predict(input_transformed)[0]

    # Calculer la valeur en Franc CFA
    prix_par_tonne = 500000  # Exemple : 500 000 FCFA par tonne
    rendement_fcfa = rendement_tonnes * prix_par_tonne

    # Afficher le résultat
    print("\nRésultat de la prédiction :")
    print(f"Rendement estimé : {rendement_tonnes:.2f} tonnes/hectare")
    print(f"Valeur estimée en Franc CFA : {rendement_fcfa:,.2f} FCFA\n")


# *** Exécuter le programme ***
if __name__ == "__main__":
    main()
