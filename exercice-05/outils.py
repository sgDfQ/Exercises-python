def convertir_note(texte):
    try:
        return float(texte.replace(',', '.'))
    except (ValueError, AttributeError):
        return None

def mention(note):
    if note is None:
        return None
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"

def moyenne(valeurs):
    if not valeurs:
        return None
    return sum(valeurs) / len(valeurs)