'''
f = open("files/file01.txt") #default mode membaa adalah "rt"
i = f.readline()
print(i,end="")
j = f.readline()
print(j,end="")
k = f.readline()
print(k,end="")
f.close()
'''

#cara lain untuk mendapatkan baris perbaris
f = open("files/file01.txt") #default mode membaa adalah "rt"
for x in f:
    print(x,end="")