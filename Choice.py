class Choice(object):
    """
        Les Spe et les Etudiants seront représentés par Cette classe Afin de permettre une application unique de Gale-Shapley
    """
    def __init__(self,nom,capacite,preference):
        self.nom=nom#Le nom de l'objet conformément au fichier txt
        self.capacite=capacite#Nombre de Choice pouvant etre accepté
        self.listeAccepte=[]#Liste des Choice que l'on accepte
        self.preference=preference#Liste des préferences trié
        self.nombreAccepte=0
    def  __str__(self):
        return self.nom
    def free(self):
        """Choice->Boolean
            Permet de savoir si l'on peut toujours accepter des Choice
        """
        return (self.nombreAccepte<self.capacite)
    
    def prefere(self,Demande):
        """Choice-->Boolean
        Permet de savoir si l'appelant préfere demande à l'un des Choice dans sa liste D'accepté
        """
        IndiceDemande=self.preference.index(Demande)
        dernierAccepte=self.listeAccepte[-1]
        if self.preference.index(dernierAccepte) > IndiceDemande :#L'indice de celui qui demande doit etre plus petit en effet l'etudiant ou le Parcours le plus demandé à pour indice 0
            return(True,dernierAccepte)
        return (False,None)
    def ajoutAccepte(self,accepte):
        """
            Permet que la liste des candidats accepté reste trié après chaque insertion
        """
        self.nombreAccepte+=1
        for i in range(0,len(self.listeAccepte)):#On parcourt la liste des candidats accepté pour se placer juste avant celui qui à un indice de préférence moins elevé que le notre
            if self.preference.index(self.listeAccepte[i])>self.preference.index(accepte):
                self.listeAccepte.insert(i,accepte)
                return True
        self.listeAccepte.append(accepte)
    def CheckValid(self):
        for i in range(0,len()-1):
            if self.preference.index(self.listeAccepte[i])>self.preference.index(self.listeAccepte(i+1)):
                print("WTF")
                sleep(2)
    def setListePref(self,listePref):
        self.preference=listePref
