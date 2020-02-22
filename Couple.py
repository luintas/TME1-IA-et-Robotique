class Couple:
    def __init__(self,Etudiant,Parcours,):
        if(Etudiant== None):
            print("Erreur Etudiant est None")
        if(Etudiant== None):
            print("Erreur Parcours est None")
        self.Etudiant=Etudiant
        self.Parcours=Parcours
        self.Etudiant.ajoutAccepte(Parcours)
        self.Parcours.ajoutAccepte(Etudiant)
    def __str__(self):
        return "("+str(self.Etudiant)+","+str(self.Parcours)+")"
    def divorce(self):
        #print(self.Etudiant,len(self.Etudiant.listeAccepte))
        self.Etudiant.listeAccepte.remove(self.Parcours)
        self.Etudiant.nombreAccepte-=1
        #print(self.Etudiant,len(self.Etudiant.listeAccepte))
        #print(self.Parcours,len(self.Parcours.listeAccepte))
        self.Parcours.listeAccepte.remove(self.Etudiant)
        self.Parcours.nombreAccepte-=1
        #print(self.Parcours,len(self.Parcours.listeAccepte))

class ListeCouple:
    def __init__(self,liste):
        self.listeCouple=liste

    def __str__(self):
        a=""
        for Couple in self.listeCouple:
            a=a+str(Couple)+" "
        return a
    def findCouple(self,Etudiant,Parcours):
        """
        Choice x Choice -> Couple
        Renvoie le couple constitué des deux Choice si il existe  
        """
        for couple in self.listeCouple:
            if(couple.Etudiant==Etudiant):
                if(couple.Parcours==Parcours):
                    return couple
            elif(couple.Etudiant==Parcours):
                if(couple.Parcours==Etudiant):
                    return couple
        return None
    def append(self,obj):
        if obj.__class__.__name__ == "Couple":
            return self.listeCouple.append(obj)
    def remove(self,obj):
        a=len(self.listeCouple)
        self.listeCouple.remove(obj)
        b=len(self.listeCouple)
        if a==b:
            print("Probleme")
            sleep(500)
        return 
