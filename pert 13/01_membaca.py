f = open("files/file01.txt") #default mode membaa adalah "rt"
i = f.read()
print(i)

f.close()
f = open("files/file01.txt")
j = f.read()
print(j)
