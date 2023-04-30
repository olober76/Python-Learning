# Lambda Function

def f_kuadrat(angka):
    return angka**2


print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")


# Mencoba dengan lambda
# output = lambda argument: expression

kuadrat = lambda angka:angka**2
print(f"hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

# A. Fungsi lambda function

# 1. Sorting untuk list biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted list = {data_list}")

    #Sorting dia pakai panjang

def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"Sorted list by fungsi panjang_nama = {data_list}")
    
    #Sort pakai lambda

data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")


# 2. Filter

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima, data_angka)) #Cara ribet
data_angka_baru = list(filter(lambda x:x<5,data_angka)) #Memakai lambda
print(data_angka_baru)

    #Kasus genap

data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(data_genap)
    
    #Kasus ganjil

data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))
print(data_ganjil)
   
    #Kasus kelipatan 3

data_tri = list(filter(lambda x:(x%3==0), data_angka))
print(data_tri)


# B. Anonymous Function
    # currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5,2)
print(f" Fungsi biasa = {data_hasil}")

    #Dengan Currying menjadi

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Pangkat 2  = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"Pangkat 3  = {pangkat3(3)}")
print(f"Pangkat bebas  = {pangkat(4)(5)}")