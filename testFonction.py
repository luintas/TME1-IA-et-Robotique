from tme1 import *

listeSpe = filetoMatSpe("./FichierPrefSpe.txt")
listeEtu = filetoMatEtu("./FichierPrefEtu.txt")

genere_liste_pref(listeEtu,listeSpe)
#Teste si la fonction de mariage et de divorce fonctionnent
a=Couple(listeEtu[0],listeSpe[0])
print(a)
print(listeEtu[0].listeAccepte)
print(listeSpe[0].listeAccepte)
a.divorce()
print(listeEtu[0].listeAccepte)
print(listeSpe[0].listeAccepte)