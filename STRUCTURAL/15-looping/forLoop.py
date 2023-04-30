# Looping statement tipe for looping

#contoh tanpa menggunakan looping
# angka = 1
# print(angka)
# angka = angka + 1
# print(angka)
# angka = angka + 1
# print(angka)

 #Looping dengan list
angka2 = [0,1,2,3,4]
print(angka2)

for i in angka2: #perulangan akan dimulai dari angka 0
    print(f"i sekarang => {i}")

print("akhir dari program 1\n")

angka3 = [0,2,4,8,10]
for x in angka3: #perulangan akan mengikuti nilai dari indeks awal list sampai indeks terakhir
    print(f"x sekarang => {x}")

print("akhir dari program 2\n")

#Looping dengan range
angka4 = range(5)
for i in angka4: # selalu dimulai dari angka 0 misal jika range(5), maka looping akan start dari 0-4
    print(f"i sekrang i-> {i}")

print("akhir dari program 3\n")

angka4 = range(1,10)
for i in angka4: #mengikuti dari nilai awalan range hingga niali akhir (n-1) dari range
    print(f"i sekrang i-> {i}")
    #dalam looping juga bisa diisi dengan yang lain, seperti print dan sebagainya
    print(f"Duta Ganteng")

print("akhir dari program 4\n")

#Menggunakan string
data_str = "Saya ganteng abis"
for huruf in data_str: # tiap karakter akan di keluarkan di tiap linenya
    print(huruf)

print("akhir dari program 5\n")










