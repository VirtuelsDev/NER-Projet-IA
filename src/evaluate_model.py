from sklearn.metrics import classification_report

def evaluate_model(y_true, y_pred):
    """
    Args:
        y_true (array-like): Les étiquettes réelles (vraies classes).
        y_pred (array-like): Les étiquettes prédites par le modèle.

    Returns:
        None: Affiche le rapport de classification.
    """
    try:
        # Générer et afficher le rapport de classification
        report = classification_report(y_true, y_pred)
        print("Rapport de classification :")
        print(report)
    except Exception as e:
        # Gérer les erreurs potentielles (par exemple, si les entrées sont invalides)
        print(f"Une erreur s'est produite lors de l'évaluation du modèle : {e}")