import re

# Exemple de motifs regex pour détecter des dates et des acronymes
regex_patterns = {
    "DATE": r"\d{2}/\d{2}/\d{4}",  # Dates au format JJ/MM/AAAA
    "ACRONYM": r"[A-Z]{2,}",       # Acronymes en majuscules
}

def detect_entities(text, pattern_type):
    """
    Détecte des entités dans un texte en utilisant un motif regex.
    """
    pattern = regex_patterns.get(pattern_type)
    if pattern:
        return re.findall(pattern, text)
    return []