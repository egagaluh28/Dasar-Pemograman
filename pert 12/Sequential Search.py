#Muhammad Galuh Gumelar
#J0403221017

def seksearch(D,x):                                           #Membuat fungsi seksearch dengan parameter "D" dan "x"
    print("Data masuk:",D)                                    #Mencetak nilai D dan "data masuk"
    print("data yang dicari:",x)                              #Mencetak "data yang dicari" dan nilai x
    print("-------------------------------------------")      #Mencetak parameter
    n = len(D)                                                #Menghitung banyaknya data yang ada dalam data  
    posisi = -1                                               #Variabel posisi yang menyatakan nilai
    for i in range(n):                                        #Pengulangan yang terjadi sebanyak n, dimulai dari indeks 0
        print((i+1),"mengecek data di indeks-",i,":",D[i])    #Mencetak pengulangan dan mencetak indeks, serta nilainya
        if D[i]==x:                                           #apabila nilai sama dengan yang dicari saat pengulangan
            posisi = i                                        #Maka variabel akan berubah posisi dengan indeks yang dicari
            break                                             #Ketika sudah menemukan data maka fungsi dipaksa berhenti
    if posisi==-1:                                            #apabila nilai yang dicari tidak ada dalam indeks
        print(x,"tidak ada pada data")                        #Maka nilai yang dicari akan dicetak serta keterangan tidak ada dalam data
        return None                                           #Mengembalikan nilai fungsi yang ada
    else:                                                     #apabila nilai yg dicari ada dalam salah satu indeks data
        print(x,"terletak pada indeks",posisi)                #Maka nilai yang dicari akan dicetak dan posisi indeks dari yang dicari
        return posisi                                         #Mengembalikan nilai fungsi yang ada pada sebelumnya

A = [17,83,37,6,10,82,5,11,1]
rslt = seksearch(A,6)