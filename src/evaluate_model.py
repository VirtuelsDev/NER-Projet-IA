from sklearn.metrics import classification_report

def evaluate_model(y_true, y_pred):
    """
    Évalue la performance du modèle en utilisant la précision, le rappel et le F1-score.
    """
    print(classification_report(y_true, y_pred))