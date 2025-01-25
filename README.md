# Projet NER pour l'Intelligence Artificielle

## Description

Ce projet vise à développer un modèle de Reconnaissance d'Entités Nommées (NER) spécifique au domaine de l'intelligence artificielle (IA).

## Installation

1. Clonez ce dépôt :

```bash
   git clone https://github.com/votre-utilisateur/NER-Projet-IA.git
``` 

2. Installez les dépendances :

```bash
   pip install -r requirements.txt
```

3. Téléchargez le modèle de langue français de spaCy :

```bash
   python -m spacy download fr_core_news_sm
```

## Utilisation

1. Entraînez le modèle :

```bash
   python src/train_ner_model.py
```

2. Exécutez l'application Streamlit :

```bash
   streamlit run src/app.py
```