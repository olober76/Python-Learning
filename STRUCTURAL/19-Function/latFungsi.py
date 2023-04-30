#Latihan Fungsi

import os

#menghitung luas dan keliling persegi panjang

# #membuat header program
# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# #mengambil input dari user
# LEBAR = int(input("Masukkan nilai Lebar : "))
# PANJANG = int(input("Masukkan nilai Panjang : "))

# #Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# #tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    #Fungsi header
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    #Mengambil input user
    lebar = int(input("Masukkan nilai Lebar : "))
    panjang = int(input("Masukkan nilai Panjang : "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    #Fungsi luas
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    #Fungsi keliling
    return 2*(panjang+lebar)

def display(massage,value):
    #Fungsi display
    print(f"Hasil perhitungan {massage} = {value}")

#PROGRAM UTAMANYA
while True:
    
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(PANJANG,LEBAR)

    opsi = input("""
    PILIH
    1. Display luas
    2. Display keliling
    3 Display luas dan keliling
    
    JAWABANMU : """)

    if opsi == "1":
        display("luas", LUAS)
    
    elif opsi == "2":
        display("keliling", KELILING)
    
    elif opsi == "3":
        display("luas", LUAS)
        display("keliling", KELILING)

    else:
        print("Tidak ada dalam program \n\n")


    isContinue = input("Apakah lanjut (y/n)? : ")
    if isContinue == "n":
        break
    elif isContinue == "N":
        break

print("Program selesai, terima kasih")