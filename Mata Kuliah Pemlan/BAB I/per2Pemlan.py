#Pertemuan kedua PEMLAN
# LIST

listname = ["jason", "kukuh", "eldon" ]
blacklist = []

print(listname)
print(blacklist)

len(listname) #untuk melihat panjang list

listname[2] = "ocir"

print(len(listname))
print(listname)


listname2 = ["Kukuh", 213, True ]

print(listname2)

listname2.append('tutor') #menambahkan index list beserta isinya
print(listname2)

daftargebetan = ["bunga", "mawar", "bulan"]

listname2.extend(daftargebetan) #menambahkan  satu list ke list yang lainnya tanpa harus menghilangkan list yang lainnya
print(listname2)
print(len(listname2))
print(len(daftargebetan)) #list yang ditambahkan  akan tetap

listname2.remove("bulan") #menghapust list dengan menulis parameter nilai di dalam index secara langsung
print(listname2)

listname2.pop(0) #menghapust list dengan menulis indexnya saja
print(listname2)

listname2.pop() #menghapus list tanpa menuliskan angka indeks, maka index yang terbesar akan dihapus
print(listname2)


while listname2[0] == 213 :  #looping statement
    print("kamu ganteng")
    listname2[0] = False 
    

kegiatan = 0
while kegiatan < 6: #looping statement
    print("makan bang")
    # if kegiatan == 4: #conditional statement
    #     break #untuk menghentikan perulangan
    kegiatan += 1
    # if kegiatan == 3: #conditional statement
    #     continue #untuk meng skip perulangan
else:
    print("ganok loop an mas e") # while statement  bisa diadakan  else

angka = 2

# for variablename in range(start, stop, step) start = angka mulai , stop = angka berakhir, step, kelipatan inkremen
for angka in range(1, 6):
    print(listname2)
    print(angka)



