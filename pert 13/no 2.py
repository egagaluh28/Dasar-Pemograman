#MUHAMMAD GALUH GUMELAR
#TRPL BP1
import random                               # import file random

list=[0,1,2,3,4,5,6,7,8,9]                  # list urutan angka
for x in range (100) :                      # akan mencetak ke bawah sebanyak 100x
    for y in range (10) :                   # akan mencetak kesamping sebanyak 10x
        print(random.choice(list), end=" ") # akan mencetak data random yang di ambil dari list
    print("\n")                             # mencetak garis baru