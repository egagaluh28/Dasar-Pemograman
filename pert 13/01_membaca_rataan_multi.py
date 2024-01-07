import os
Path = "data"
filelist = os.listdir(Path) #["data01.txt","data02.txt","data07.txt"]
#print(filelist)
jmlh = 0
banyakdata = 0
for namafile in filelist:
    print("Membaca data pada:",namafile)
    y  = 'data\\' + namafile
    f = open(y,"r")
    subbanyakdata = 0
    subjmlh = 0
    for nilai in f:
        nilai = int(nilai)
        subbanyakdata +=1
        subjmlh +=  nilai
    print(">>",namafile,"Jumlah data:",subbanyakdata,", Nilai total:",subjmlh)
    print("--------------------------------")
    jmlh += subjmlh
    banyakdata += subbanyakdata

print(">>Jumlah data semuanya:",banyakdata,", Nilai total semua:",jmlh)
print("Rataan:",jmlh/banyakdata)