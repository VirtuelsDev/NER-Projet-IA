import spacy

# Charger le modèle de langue français de spaCy
nlp = spacy.load("fr_core_news_sm")

def preprocess_text(text):
    """
    Nettoie et prétraite le texte.
    """
    doc = nlp(text)
    # Supprimer les stopwords et les ponctuations, et lemmatiser
    cleaned_text = " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    return cleaned_text