# Looping dari list

# For Loop 
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka: #for nama_variable in nama_list
    print(f"angka = {angka}")

print("\n")
peserta = ["ucup", "otong", "dadang", "diding"]

for nama in peserta:
    print(f"nama = {nama}")

print("\n")
#For Loop dan range
print("For Loop dan range ")

kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\nwhile loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# List comprehension
print("\nLIST Comprehension Loop")
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
