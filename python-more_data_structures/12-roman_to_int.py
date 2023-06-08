#!/usr/bin/python3
def roman_to_int(chaine_romaine):
    if not isinstance(chaine_romaine, str) or chaine_romaine is None:
        return 0
    
    chiffres_romains = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    resultat = 0
    valeur_precedente = 0
    
    for caractere in reversed(chaine_romaine):
        valeur = chiffres_romains.get(caractere, 0)
        if valeur >= valeur_precedente:
            resultat += valeur
        else:
            resultat -= valeur
        valeur_precedente = valeur
    
    return resultat
