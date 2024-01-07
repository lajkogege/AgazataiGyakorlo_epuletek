import beveztes

beveztes.elso_feldata()

import sorozat
print("II/A,B,C:")
listam=sorozat.fej_iras()
print("II/D,E")
sorozat.konzol_kiir(listam)
print("II/F:")
sorozat.file_kiir(listam)

import epuletek
print("III/A,B:")
osztaly_listam=epuletek.fajlbeolvasas()
print(f"\tAz épületek száma: {len(osztaly_listam)}")
db=epuletek.magasabb_epulet(osztaly_listam)
print("III/C:")
print(f"\tAz 555 lábnál magsasabb épületek száma: {db}")
print("III/D:")
max=epuletek.legoregebb(osztaly_listam)
print(f"\tA egöregebb épület országa: {osztaly_listam[max].orszaga}")