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
