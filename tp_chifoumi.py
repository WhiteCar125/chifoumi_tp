import random
while True:
    def choix_ordi():
     c = random.choices(str('p f c'))
     return c

    def choix_joueur():
        choix = str(input("Choisissez p, f, ou, c\n>>"))
        return choix

    def verdict(choix_joueur,choix_ordi):
        if choix_joueur == choix_ordi:
            return 0

        if choix_joueur=='p' and choix_ordi == 'c' or choix_joueur=='f' and choix_ordi=='p' or choix_joueur=='c' and choix_ordi=='f':
            return 1

        else :
            return -1

    def partie():
        joueur = choix_joueur() 
        ordi = choix_ordi()
        print(ordi)
        return verdict(joueur,ordi)

    def jeu_pfc():
        s = 0
        verdict = partie()
        s = s + verdict
        print(s)

    jeu_pfc()

