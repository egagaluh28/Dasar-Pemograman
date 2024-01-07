my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]              # Variabel my_friends menampung list yang berisi nama-nama orang dengan type list(str)
print("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3])) # Memasukan list my_friends index ke-3 kedalam string lalu mencetaknya
print("Semua teman: ada {} orang".format(len(my_friends)))           # program akan mencetak dari list my_friends kedalam string
for friend in my_friends:                                            # Looping akan dilakukan dengan list my_friends dan masukan setiap valuenya kedalam variabel friend
    print(friend)                                                    # mencetak