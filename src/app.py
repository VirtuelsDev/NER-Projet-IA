import streamlit as st
import spacy

# Titre de l'application
st.title("Reconnaissance d'Entités Nommées (NER)")

# Charger le modèle spaCy personnalisé
nlp = spacy.load("models/custom_ner_model")

# Option pour saisir du texte manuellement
st.header("Saisir du texte")
user_input = st.text_area("Entrez votre texte ici")

# Option pour charger un fichier texte
st.header("Charger un fichier texte")
uploaded_file = st.file_uploader("Choisissez un fichier texte", type=["txt"])

# Bouton pour lancer l'analyse
if st.button("Analyser"):
    if user_input or uploaded_file:
        # Si un fichier est chargé, lire son contenu
        if uploaded_file:
            text = uploaded_file.read().decode("utf-8")
        else:
            text = user_input

        # Analyser le texte avec le modèle spaCy
        doc = nlp(text)

        # Afficher les entités détectées
        st.header("Entités détectées")
        for ent in doc.ents:
            st.write(f"**Entité** : {ent.text}, **Label** : {ent.label_}")

        # Afficher le texte annoté
        st.header("Texte annoté")
        st.write(doc.ents)
    else:
        st.warning("Veuillez saisir du texte ou charger un fichier.")