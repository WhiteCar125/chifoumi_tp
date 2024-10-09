import random

def choix_ordi():
    c = random.choices('p','f','c')
    return c

def choix_joueur():
    choix = str(input("Choisissez p, f, ou,c"))