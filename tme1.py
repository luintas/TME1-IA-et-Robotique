from Couple import *
from Choice import *
from time import *
"""Definition des classes utilisées"""
#NOTE on garde la liste des objet plutot que la liste en String car elle prend moins de place en mémoire et permert un acces plus rapide



#Fonction permettant la génération des classes à partir des fichiers fournis
def filetoMatSpe(File):
    """ File -> list[Choice]
        Genere une liste contenant tout les choices contenus dans le fichier de préference des Spéciàlités
        NOTE: Les Choice ne contiennent pas de réference vers les objets dans la liste de préference mais une liste de String contenant les indices de leur noms
    """
    f=open(File,"r")
    lines = f.read().splitlines()
    capacite=lines[1].split()
    #print(capacite)
    listSpe=[]
    for indicelignecourante in range(2,len(lines),1):
        tmpPref=lines[indicelignecourante].split()[1:]
        listSpe.append(Choice(lines[indicelignecourante].split()[0],int(capacite[indicelignecourante-2]),tmpPref))
    return listSpe


def filetoMatEtu(File):
    """ File -> list[Choice]
        Genere une liste contenant tout les choices contenus dans le fichier de préférence des Etudiants
        NOTE: Les Choice ne contiennent pas de réference vers les objets dans la liste de préference mais une liste de String contenant les indices de leur noms
    """
    f=open(File,"r")
    lines = f.read().splitlines()
    listEtu=[]
    for indicelignecourante in range(1,len(lines),1):
        tmpPref=lines[indicelignecourante].split()[1:]
        listEtu.append(Choice(lines[indicelignecourante].split()[0],1,tmpPref))

    if(len(listEtu)!= int(lines[0])):
        print("Probleme lors de la génération de la liste d'etudiant")
    return listEtu
def dicoSpecialite(listeSpe):
    """
    list[Choice]->Dictionnaire \n
    Renvoie un dictionnaire prenant pour indice le nom d'un Choice et en valeur la reference à cet objet à partir de la liste passée en argument
    """
    dico={}
    for Spe in listeSpe:
        dico[str(Spe.nom[0:3])]=Spe
    return dico
#TODO Créer la fonction qui permettra d'ajouter les objets pour remplacer les Strings et donc faire fonctionner les fonctions de recherche et de mariage
def genere_liste_pref(listeEtu,listeSpe):
    for Spe in listeSpe:
        listePref=[]
        for Pref in Spe.preference:
            listePref.append(listeEtu[int(Pref)])
        Spe.setListePref(listePref)
    dicoSpe=dicoSpecialite(listeSpe)
    for Etu in listeEtu:
        listePref=[]
        for Pref in Etu.preference:
            listePref.append(dicoSpe[Pref[0:3]])
        Etu.setListePref(listePref)


def createMat():
    Spe=filetoMatSpe("./FichierPrefSpe.txt")
    tabSpe=[]
    for i in range(1,len()):
        tabSpe.add(Choice(Spe.capacite[i-1],Spe.matrice[i]))
    Etu=filetoMat("./FichierPrefEtu.txt")
    tabEtu=[]
    for i in range(1,len()):
        tabEtu.add(1,Etu.matrice[i])


#Fonctions demandées dans la suite du projet
def GaleShapley(tabEtudiant,tabParcours):
    listeCouple=ListeCouple([])
    tabLibre=tabEtudiant
    tailletabLibre=len(tabLibre)
    while(tailletabLibre>0):
        tmpLibre=tabLibre.pop()
        tailletabLibre-=1
        for Volonte in tmpLibre.preference:#TODO Voir pourquoi des gens partent sans avoir trouvé d'affectation
            if(not tmpLibre.free()):#Permet de savoir si l'on est toujours libre si on ne l'est pas on ne cherche plus d'Etudiant/de Master
                break
            if Volonte.free() :
                listeCouple.append(Couple(tmpLibre,Volonte))
            else:
                (reponse,rejete)=Volonte.prefere(tmpLibre)
                if reponse :
                    tmpDivorce=listeCouple.findCouple(Volonte,rejete)
                    if tmpDivorce == None:
                        print("ERROR",sys.stderror)
                    tmpDivorce.divorce()
                    listeCouple.remove(tmpDivorce)
                    tabLibre.append(rejete)
                    tailletabLibre+=1
                    listeCouple.append(Couple(tmpLibre,Volonte))
        #for Spe in tabParcours:
        #    Spe.CheckValid()
                    
    return listeCouple



