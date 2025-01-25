import spacy
from spacy.pipeline import EntityRuler

# Charger le modèle de langue français de spaCy
nlp = spacy.load("fr_core_news_sm")

# Ajouter un EntityRuler au pipeline
ruler = nlp.add_pipe("entity_ruler")  # Utiliser le nom du composant

# Ajouter des motifs personnalisés
patterns = [
    # Technologies
    {"label": "TECHNOLOGY", "pattern": "Machine Learning"},
    {"label": "TECHNOLOGY", "pattern": "Deep Learning"},
    {"label": "TECHNOLOGY", "pattern": "Neural Networks"},
    {"label": "TECHNOLOGY", "pattern": "Artificial Intelligence"},
    {"label": "TECHNOLOGY", "pattern": "Natural Language Processing"},
    {"label": "TECHNOLOGY", "pattern": "Computer Vision"},
    {"label": "TECHNOLOGY", "pattern": "Reinforcement Learning"},

    # Concepts
    {"label": "CONCEPT", "pattern": "Supervised Learning"},
    {"label": "CONCEPT", "pattern": "Unsupervised Learning"},
    {"label": "CONCEPT", "pattern": "Semi-Supervised Learning"},
    {"label": "CONCEPT", "pattern": "Transfer Learning"},
    {"label": "CONCEPT", "pattern": "Generative Adversarial Networks"},
    {"label": "CONCEPT", "pattern": "Convolutional Neural Networks"},
    {"label": "CONCEPT", "pattern": "Recurrent Neural Networks"},

    # Outils et frameworks
    {"label": "TOOL", "pattern": "TensorFlow"},
    {"label": "TOOL", "pattern": "PyTorch"},
    {"label": "TOOL", "pattern": "Keras"},
    {"label": "TOOL", "pattern": "Scikit-learn"},
    {"label": "TOOL", "pattern": "OpenCV"},
    {"label": "TOOL", "pattern": "NLTK"},
    {"label": "TOOL", "pattern": "SpaCy"},

    # Acronymes
    {"label": "ACRONYM", "pattern": "AI"},
    {"label": "ACRONYM", "pattern": "ML"},
    {"label": "ACRONYM", "pattern": "DL"},
    {"label": "ACRONYM", "pattern": "NLP"},
    {"label": "ACRONYM", "pattern": "CV"},
    {"label": "ACRONYM", "pattern": "GAN"},
    {"label": "ACRONYM", "pattern": "CNN"},
    {"label": "ACRONYM", "pattern": "RNN"},
]

# Ajouter les motifs au ruler
ruler.add_patterns(patterns)

# Sauvegarder le modèle personnalisé
nlp.to_disk("models/custom_ner_model")

print("Modèle personnalisé entraîné et sauvegardé avec succès !")