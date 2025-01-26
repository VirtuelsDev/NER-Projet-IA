import streamlit as st
import spacy
import base64

# Fonction pour encoder l'image en base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Fonction pour le Header avec image de fond locale
def header():
    # Encoder l'image locale en base64
    image_path = "./data/screenshots/image.png"  # Chemin de votre image locale
    base64_image = get_base64_of_image(image_path)

    # CSS pour le header avec image de fond
    st.markdown(
        f"""
        <style>
        .header {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
            background-position: center;
            color: blue;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        </style>
        <div class="header">
            Ner-Projet-AI
        </div>
        """,
        unsafe_allow_html=True,
    )

# Fonction pour la page d'accueil
def home():
    st.title("Bienvenue dans l'application de Reconnaissance d'Entités Nommées (NER)")
    st.write("""
    Cette application permet de détecter des entités nommées dans un texte en utilisant un modèle spaCy personnalisé.
    Vous pouvez soit saisir du texte directement, soit charger un fichier texte pour l'analyse.
    """)

# Fonction pour la page d'analyse de texte
def analyze_text():
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

# Fonction pour la page d'information
def about():
    st.title("À propos")
    st.write("""
    Cette application a été développée pour démontrer l'utilisation de la reconnaissance d'entités nommées (NER) avec spaCy.
    Elle permet aux utilisateurs de saisir du texte ou de charger un fichier texte pour détecter les entités nommées.
    """)
    st.write("**Développeur** : Benewende Pierre BONKOUNGOU")
    st.write("**Contact** : benepeter.b@gmail.com")

# Fonction principale pour la navigation
def main():
    # Initialisation de la session state pour la page active
    if "page" not in st.session_state:
        st.session_state.page = "Accueil"

    # Header avec image de fond locale
    header()

    # Barre de navigation (boutons alignés à gauche)
    st.sidebar.title("Navigation")
    if st.sidebar.button("Accueil"):
        st.session_state.page = "Accueil"
    if st.sidebar.button("Analyse de Texte"):
        st.session_state.page = "Analyse de Texte"
    if st.sidebar.button("À propos"):
        st.session_state.page = "À propos"

    # Affichage de la page sélectionnée
    if st.session_state.page == "Accueil":
        home()
    elif st.session_state.page == "Analyse de Texte":
        analyze_text()
    elif st.session_state.page == "À propos":
        about()

# Lancer l'application
if __name__ == "__main__":
    main()