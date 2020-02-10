class Choice:
    def __init__(self,nom,capacite,preference):
        self.nom=nom#Le nom de l'objet conformément au fichier txt
        self.capacite=capacite#Nombre de Choice pouvant etre accepté
        self.listeAccepte=[]#Liste des Choice que l'on accepte
        self.preference=preference#Liste des préferences trié
    def  __str__(self):
        return self.nom
    def free(self):
        """Choice->Boolean
            Permet de savoir si l'on peut toujours accepter des Choice
        """
        return (len(self.listeAccepte)<self.capacite)
    
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
        for i in reversed(range(0,len())):
            if self.preference.index(self.listeAccepte(i))>self.preference.index(accepte):
                self.listeAccepte.insert(i,accepte)
                return True
        self.listeAccepte.append(accepte)

    def setListePref(self,listePref):
        self.preference=listePref
