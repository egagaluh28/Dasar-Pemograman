fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry', 'orange', 'cherry'] #variabel fruits yang menampung data dengan type list (str)
F = fruits.copy() #variabel F menampung data yang dimiliki oleh variable fruits (list)
deltaSebelumnya = 0 #variabel deltaSebelumnya yang menyimpan data type (int) dengan nilai yang berawal dari 0 dan akan terus bertambah didalam perulangan
 
while "cherry" in F: #looping F akan berjalan jika terdapat sebuah string ("cherry")
    x = F.index("cherry") #variabel x yang menyimpan Indeks dari string("cherry") yang terdapat pada variabel F
    print("indeks cherry:", x+deltaSebelumnya) #Mencetak index cherry + deltasebelumnya
    deltaSebelumnya = deltaSebelumnya+x+1 #deltasebelumnya ditimpa dengan deltasebelumnya + index cherry + 1
    F = F[x+1:] #F ditimpa dengan F[index yang ditentukan sampah akhir]
    print(F) #mencetak F
