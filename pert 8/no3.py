def luas_jajargenjar(a,t):
    luas = a * t
    return luas

print (33*"=")
print ("PROGRAM MENCARI LUAS JAJAR GENJAR")
print (33*"=")
print ("\n")

alas=int(input("masukan nilai alas:"))
tinggi=int(input("masukan nilai tinggi:"))
print("luas jajargenjar", luas_jajargenjar(alas,tinggi))