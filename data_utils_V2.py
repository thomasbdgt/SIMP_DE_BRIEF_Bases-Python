# Variables :
pi = 3.14159
e = 2.71828

# Functions :
def carre(x):
    return  x ** 2

def cube(x):
    return x ** 3

def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)

def valeur_absolue(x):
    if x < 0:
        x = -x
        return x
    else:
        return x

def maximum(liste):
    return max(liste)

def minimum(liste):
    return min(liste)

def moyenne(liste):
    return sum(liste) / len(liste)

def ecart_type(liste):
    moy = moyenne(liste)
    variance = sum((x - moy) ** 2 for x in liste) / len(liste)
    return variance ** 0.5

def mediane(liste):
    liste_triee = sorted(liste)
    n = len(liste_triee)
    if n % 2 == 0:
        return (liste_triee[n // 2 - 1] + liste_triee[n // 2]) / 2
    else:
        return liste_triee[n // 2]

def somme_cumulee(liste):
    cumul = 0
    liste_cumulee = []
    for i in range(len(liste)):
        cumul += liste[i]
        liste_cumulee.append(cumul)
    return liste_cumulee

def compter_occurences(liste):
    dico_comptage = {}
    for i in liste:
        comptage = liste.count(i)
        dico_comptage[i] = comptage
    return dico_comptage


def inverser_dict(dictionnaire):
    dico_inverse = {}
    for i in dictionnaire:
        dico_inverse[dictionnaire[i]] = i
    return dico_inverse

def filtrer_pairs(liste):
    liste_pairs = []
    for i in liste:
        if i % 2 == 0:
            liste_pairs.append(i)
    return liste_pairs

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def trouver_doublons(liste):
    liste_doublons = []
    for i in liste:
        if liste.count(i) > 1:
            if i in liste_doublons:
                pass
            else:
                liste_doublons.append(i)
    return liste_doublons

def calculer_moyenne_ponderee(valeurs, poids):
    somme = 0
    coeff = 0
    longueur = max(len(valeurs), len(poids))

    for i in range(longueur):
        somme += valeurs[i] * poids[i]
    for j in poids:
        coeff += j
    return somme / coeff

def analyser_texte(texte = str):
    dico_analyse = {}

    longueur = len(texte.split())
    len_avec_space = len(texte)
    len_sans_space = len(texte) - texte.count(" ")
    mot_long = ""
    len_mot = 0
    longueur_mot = []

    for i in texte.split():
        longueur_mot.append(len(i))
        if len(i) > len_mot:
            len_mot = len(i)
            mot_long = str(i)

    dico_analyse["Nombre total de mots "] = longueur
    dico_analyse["Nb de caractères (espaces inclus) "] = len_avec_space
    dico_analyse["Nb de caractères (espaces exclus) "] = len_sans_space
    dico_analyse["Mot le plus long "] = mot_long
    dico_analyse["Longueur du mot le plus long "] = len_mot
    dico_analyse["Longueur moyenne des mots "] = moyenne(longueur_mot)

    return dico_analyse

