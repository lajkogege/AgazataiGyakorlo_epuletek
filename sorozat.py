import random
def fej_iras():
    lista=[]
    for i in range (0,7,1):
        veletlen_szam:int=random.randint(0,1)
        lista.append(veletlen_szam)

    for i in range(0,len(lista),1):
        if lista[i] ==0:
            if i == len(lista)-1:
                print("ÍRÁS")
            else:
                print("ÍRÁS",end="-")
        elif lista[i] ==1:
            if i == len(lista)-1:
                print("FEJ")
            else:
                print("FEJ",end="-")
    return lista

def fejek_szama(lista):
    db_fej:int=0
    for i in range(0,len(lista),1):
        if lista[i] == 1:
            db_fej+=1
    return db_fej

def konzol_kiir(db_fej):
    print(f"\tA fejek száma: {db_fej}")

def file_kiir(db_fej):
    fajlnev:str="fejek.txt"
    print(f"\tA fejek száma:{db_fej}")
    f=open(fajlnev, "w", encoding="utf-8")
    f.write(f"\A fejek száma:{db_fej}")
    f.close()
