#bisa pake mode append (a) atau write (w)

f = open("dirfiletulis\\"+"f01.txt",  "w")
f.write("ABCDEFGHIJ")
f.write("KLMNOP\n")
f.write("QRSTU")
f.close()