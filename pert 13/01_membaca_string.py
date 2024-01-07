f = open("files/file04.txt")
isi = f.read()
print("Isi file:\n",isi,"\nPanjang isi:",len(isi)," karakter\n",sep="") 

pil = "y"
while pil == "y":
    kata = input("kata yang ingin dicari:")
    n = isi.count(kata)
    print("terdapat",n,"buah kata:",kata)
    pil = input("lagi? (y/n):")


