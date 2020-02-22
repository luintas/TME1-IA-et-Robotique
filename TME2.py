from random import sample
from Choice import *
from tme1 import *
def Create_n_Etu(n):
    """
        int -> list[Choice]
        Crée une liste de n étudiant avec une liste de préférence vide
    """
    listeEtu=[]
    for i in range(n):
        listeEtu.append(Choice("Etu"+str(i+1),1,None))
    return listeEtu
def Create_Random_pref_Etu(listeEtu,listeSpe):
    """
        Crée des listes aléatoires de Préférences pour tout les Etu dans listeSpe passé en parametre
    """
    for Etu in listeEtu:
        Etu.setListePref(sample(listeSpe,len(listeSpe)))

def Create_Capacite_deter(ValTotal,nbElement):
    #TODO Trouver un moyen de faire une generation aléatoire de la distribution de la capacité
    """
        int x int -> list[int]
        Renvoie une liste contenant des valeurs de capacités pour chaque element avec pour valeur totale ValTotal
    """
    listeCapacite=[]
    for i in range(nbElement):
        listeCapacite.append(ValTotal//nbElement)
    if(ValTotal % nbElement != 0):
        for i in range(nbElement):
            listeCapacite[i]+=1
    return listeCapacite

def Create_Random_pref_Spe(listeEtu,listeSpe,n):
    """
        list[Choice] x list[Choice] x int ->list[Choice]\n
        Renvoie la liste de Choice apres avoir initialisé la liste de préférence de maniere aléatoire\n
        et la liste de capacité de maniere uniforme et de maniere à ce que sa somme ait pour valeur n
    """
    capacite=Create_Capacite_deter(n,len(listeSpe))
    i=0
    for Spe in listeSpe:
        Spe.capacite=capacite[i]
        Spe.setListePref(sample(listeEtu,len(listeEtu)))
        i+=1