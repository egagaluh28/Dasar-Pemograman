f = open("files/file03.txt","r")
jumlah = 0
for data in f:
    x = int(data)
    jumlah += x
    #print(jumlah)

print("Nilai penjumlahan datanya:", jumlah)