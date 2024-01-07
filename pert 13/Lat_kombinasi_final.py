print("----------------------------------------------------------------")
print("PROGRAM MANAJEMEN FILE DATA MAHASISWA")
print("----------------------------------------------------------------")
print("pilihan menu")
print("1. Melihat data\n2. Menambah data\n3. Menghapus data\n4. Keluar program")
pm = input("Masukan pilihan menu:")
namafile = "folderfileprogram\\datamhsw.txt"
#print(namafile)
while pm != '4':
    if pm=="1":
        print("----------------------------------------------------------------")
        print("Membaca isi file mahasiswa")
        f  =open(namafile)
        print("Isi File:")
        noBaris = 1
        for baris in f:
            print(noBaris,". ",baris, sep="",end="")
            noBaris+=1
        f.close()
    elif pm=="2":
        print("----------------------------------------------------------------")
        print("Menambah data ke file mahasiswa")
        f  =open(namafile,"a")
        sesuatu = input("Masukan data (nama uts uas):")
        f.write("\n"+sesuatu)
        f.close()
        print("Data telah disimpan.")
    elif pm=="3":
        print("----------------------------------------------------------------")
        print("Mendelete data mhsw tertentu dari file mahasiswa")
        target =  input("Masukan nama mahasiswa yang datanya ingin dihapus:")
        f  =open(namafile)
        listnya = []
        for baris in f:
            if baris.count(target)==0:
                listnya.append(baris)
        print(listnya)
        f.close()
        string=""
        for x in listnya:
            string += x
        print("-------------")
        print(string)
        f  =open(namafile,"w")
        print("--------------")
        f.write(string)
        print("Data",target,"sudah terhapus")
    else:
        print("Pilihan menu anda tidak valid!")

    pm = input("\nMasukan pilihan menu berikutnya:")
print("Anda keluar dari program, program selesai")