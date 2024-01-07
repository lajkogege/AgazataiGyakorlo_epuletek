from osztaly import Osztaly
def fajlbeolvasas():
    fajl=open("epulet.txt", "r", encoding="utf-8")
    fajl.readline()
    fajbol_sorok_lista=fajl.readlines()
    fajl.close()

    osztaly_lista=[]
    for i in range(0,len(fajbol_sorok_lista),1):
        aktelem=fajbol_sorok_lista[i]
        sor_lista=aktelem.strip().split("$")
        osztalyom=Osztaly(str(sor_lista[0]), str(sor_lista[1]), str(sor_lista[2]),int(sor_lista[3]),int(sor_lista[4]),int(sor_lista[5]))
        osztaly_lista.append(osztalyom)
        return osztaly_lista

def magasabb_epulet(osztaly_lista):
    db=0 #169.1640000006767
    lab:float=555/3.280839895
    for i in range(0,len(osztaly_lista),1):
        if osztaly_lista[i].magasag > lab:
            db+=1
    return db

def legoregebb(osztaly_lista):
    max:int=0
    maxindex:int=0
    for i in range (0,len(osztaly_lista),1):
        if osztaly_lista[i].eve >max:
            max==i
    return max


