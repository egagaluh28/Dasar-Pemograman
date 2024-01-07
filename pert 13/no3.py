#MUHAMMAD GALUH GUMELAR
#TRPL BP1

print("+++++++++++++++++++++++++++++++") #mencetak parameter
print("+ PROGRAM PENDATAAN MAHASISWA +") #mencetak parameter
print("+++++++++++++++++++++++++++++++") #mencetak parameter
print("[1]. Daftar mahasiswa\n[2]. Menambah data mahasiswa\n[3]. Keluar dari program")
menu = input("Pilih menu:")
catatan = "Daftar nama.txt"
while menu != '3':
    if menu=="1":
        print("----------------------------------------------------------------") #mencetak parameter
        print("[Lihat data siswa]")
        f  = open(catatan) #membuka file catatan
        print("Isi File:") #mencetak parameter isi
        Baris = 1        #baris di mulai dari 1
        for baris in f: 
            print(Baris,". ",baris, sep="",end="")
            Baris+=1
        f.close()
    elif menu=="2":
        print("----------------------------------------------------------------") #mencetak parameter
        print("[Menambah data siswa]")
        f  = open(catatan,"a") #membuka file catatan
        #pendataan mahasiswa
        nama = input("Nama :")         # memasukan nama
        nim = input("Nim :")           # memasukan nim
        asal = input("Asal SMK/SMA :") # memasukan asal sekolah
        #format text
        text = "Nama : {} | Nim : {} | Asal SMK/SMA : {} \n".format(nama,nim,asal)
        f.write(text)
        #menutup file
        f.close() 
        print("Data telah disimpan.")  #mencetak parameter
    else :
        print("Pilihan tidak tersedia, silahkan ulangi lagi") #mencetak parameter
    menu = input("\nPilihlah menu berikutnya\n[1]. Daftar mahasiswa\n[2]. Menambah data mahasiswa\n[3]. Keluar dari program \nPilih menu :")
print("Anda keluar dari program, program selesai")

f=open("buka")
tek = "aku"
f.write(tek)
