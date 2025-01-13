import numpy as np
import pandas as pd
import joblib
import os


# Construire les chemins absolus pour les fichiers
current_dir = os.path.dirname(__file__)  # Répertoire contenant le script
model_path = os.path.join(current_dir, "final_model.pkl")
preprocessor_path = os.path.join(current_dir, "preprocessor.pkl")
features_path = os.path.join(current_dir, "selected_features.pkl")

# Charger les fichiers
try:
    final_model = joblib.load(model_path)
    print("Modèle chargé avec succès.")

    preprocessor = joblib.load(preprocessor_path)
    print("Préprocesseur chargé avec succès.")

    feature_names = joblib.load(features_path)
    print("Noms des caractéristiques chargés avec succès.")
    
except FileNotFoundError as e:
    print(f"Erreur : {e}")
    print("Assurez-vous que les fichiers sont dans le même répertoire que ce script.")


if not isinstance(feature_names, list):
    raise ValueError("selected_features n'est pas une liste. Vérifiez le contenu.")
else:
    print("Selected features chargées avec succès :", feature_names)
    
    
# Fonction pour prétraiter les données utilisateur
def preprocess_input(form_data, preprocessor, feature_names):
    # Variables utilisateur fournies
    input_data = np.array([[
        form_data.get('superficie', 0),  # Valeur par défaut : 0
        form_data.get('pluviometrie', 0),  # Valeur par défaut : 0
        form_data.get('temperature_moyenne', 0),  # Valeur par défaut : 0
        
    ]])

    # Convertir en DataFrame avec toutes les colonnes nécessaires
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # Compléter les colonnes manquantes
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    # Appliquer le préprocesseur
    input_transformed = preprocessor.transform(input_df)
    return input_transformed

# Fonction principale
def main():
    print("Bienvenue dans l'outil de prédiction du rendement moyen !\n")
    
    # Demander les données utilisateur
    superficie = float(input("Entrez la superficie (en hectares) : "))
    pluviometrie = float(input("Entrez la pluviométrie (en mm) : "))
    temperature_moyenne = float(input("Entrez la température moyenne (en °C) : "))
    
    # Construire les données utilisateur
    user_data = {
        'superficie': superficie,
        'pluviometrie': pluviometrie,
        'temperature_moyenne': temperature_moyenne
    }
    
    # Prétraiter les données
    input_transformed = preprocess_input(user_data, preprocessor, feature_names)
    
    # Faire la prédiction
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
