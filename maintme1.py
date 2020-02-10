from tme1 import *
from sys import *



#Initialisation des variables nécéssaires
def init():
    listeSpe = filetoMatSpe("./FichierPrefSpe.txt")
    listeEtu = filetoMatEtu("./FichierPrefEtu.txt")
    genere_liste_pref(listeEtu,listeSpe)
    return (listeSpe,listeEtu)

(listeSpe,listeEtu)=init()
lc=GaleShapley(listeEtu,listeSpe)
for Spe in listeSpe:
    print(Spe,"  ",str(Spe.capacite)+"=="+str(len(Spe.listeAccepte)))
for Spe in listeEtu:
    print(Spe,"  ",str(Spe.capacite)+"=="+str(len(Spe.listeAccepte)))
"""print(lc)
lc=GaleShapley(listeSpe,listeEtu)
print("\n\n")
print(lc)"""