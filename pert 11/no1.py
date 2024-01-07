# MUHAMMAD GALUH GUMELAR
# J0403221017

def kalimat(nama ):
    nama=int(input("nama:"))# definisi fungsi yang bernama kalimat dengan parameter variabel
    kata = "{} {} {}"                     # Mendefinisikan variabel kata dengan string yang terdiri dari 3 format dan dipisahkan dengna sepasi 
    return  kata.format(nama) #Mengembalikan nilai variabel kata dengan 3 format yang di dalamnya diisi oleh variabel word

print(kalimat("nama"))
    

