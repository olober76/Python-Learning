#Global and local scope


nama_global = "otong" # Variable global


#Akses variable global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan  {nama_global}")



fungsi()


#Akses variable global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")


# Percabangan
if True:
    print(f"if menampilkan {nama_global}")


## Variable local scope

def fungsi2():
    nama_local = "Ucup"


fungsi2()
# print(nama_local) # tidak akan bisa diakses karena variable local


## Contoh penggunaan
def say_otong():
    print(f"Hello {nama}")

 
nama = "otong"
say_otong() # variabel akan dipanggil karena belum digunakan fungsi itu sendiri seblum di deklarasikan

## contoh 2:

# angka = 0

# def ubah_angka(nilai_baru):
#     angka = nilai_baru

# print(f"sebelum = {angka}")
# ubah_angka(10)
# print(f"sesudah = {angka}") # variable angka tidak akan berubah karena angka adalah variable local


# Solusi

angka = 0
name = "ucup"

def ubah(nilai_baru, nama_baru):
    global angka #fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum = {angka, name}")
ubah(10, "otong")
print(f"sesudah = {angka, name}")  

# Contoh 3
angka = 0
for i in range(0,5):
    angka += i 
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)