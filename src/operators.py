"""
operators.py.

Description :
Ce module défini les fonctions logiques de l'application

Auteur : Équipe 26
Date : 2026-02-14
"""

def add(a,b):
    """
    Additionne deux nombres.

    Paramètres :
        a (float) : premier nombre
        b (float) : deuxième nombre

    Retour :
        float : somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Soustrait deux nombres.

    Paramètres :
        a (float) : premier nombre
        b (float) : deuxième nombre

    Retour :
        float : soustraction de a et b
    """
    return a - b

def multiply(a,b):
    """
    Multiplie deux nombres.

    Paramètres :
        a (float) : premier nombre
        b (float) : deuxième nombre

    Retour :
        float : multiplication de a et b
    """
    return a ** b

def divide(a,b):
    """
    Divise deux nombres.

    Paramètres :
        a (float) : premier nombre
        b (float) : deuxième nombre

    Retour :
        int : division de a par b
    """
    return a // b
