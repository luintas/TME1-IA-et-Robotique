import TME2
from tme1 import *
import matplotlib.pyplot as py
def init(n):
    listeEtu=TME2.Create_n_Etu(n)
    listeSpe = filetoMatSpe("./FichierPrefSpe.txt")
    TME2.Create_Random_pref_Etu(listeEtu,listeSpe)
    TME2.Create_Random_pref_Spe(listeEtu,listeSpe,n)
    return listeEtu,listeSpe
tabtaille=[]
tabtemps=[]
for i in range(200,2000,200):
    tabtaille.append(i)
    temps=0
    for j in range(10):
        listeEtu,listeSpe=init(i)
        a=time()
        lc=GaleShapley(listeEtu,listeSpe)
        b=time()
        temps+=b-a
    print(temps/10)
    tabtemps.append(temps/10)
tabtailleSpe=[]
tabtempsSpe=[]
for i in range(200,2000,200):
    tabtailleSpe.append(i)
    temps=0
    for j in range(10):
        listeEtu,listeSpe=init(i)
        a=time()
        lc=GaleShapley(listeEtu,listeSpe)
        b=time()
        temps+=b-a
    print(temps/10)
    tabtempsSpe.append(temps/10)
py.plot(tabtaille,tabtemps)
py.plot(tabtailleSpe,tabtempsSpe)
py.show()