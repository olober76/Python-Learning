import csv
import os
#Write

with open('users.csv' , 'w', newline='') as file:
    fieldnames = ['acc_name', 'acc_pass', 'acc_acc']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'acc_name': 'olober', 'acc_pass': '1234', 'acc_acc' : 0})
    writer.writerow({'acc_name': 'Mortis', 'acc_pass': '4321', 'acc_acc' : 1})
    writer.writerow({'acc_name': 'Zakhaev', 'acc_pass': '4444', 'acc_acc' : 0})

def login():
    nama = str(input("\nMasukkan nama anda : "))
    sandi = str(input("Masukkan sandi anda : "))
    
    return nama,sandi

def sambutan(nama:str, sandi:str):
    with open('users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        match_found = False
        for row in csv_reader:
            if nama == row["acc_name"] and sandi == row["acc_pass"]:
                match_found = True
                if int(row["acc_acc"]) == 1:
                    print(f"Halo admin {nama}")
                else :
                    print(f"Halo user {nama}")
        if not match_found:
            print("LU SIAPA ANJIR")
                
            # line_count += 1
                
                    

def input_register():
    #Mengambil input user
    nama = str(input("Masukkan nama anda : "))
    newsandi = str(input("Masukkan sandi anda : "))
    accses = str(input("Apakah anda admin : "))
    
    return nama,newsandi, accses

def registrasi(nama: str, newsandi: str, accses :str):
    
    if accses == "iamgod":
        with open('users.csv', 'a', newline='') as file:
            fieldnames = ['acc_name', 'acc_pass', 'acc_acc']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'acc_name': nama, 'acc_pass': newsandi, 'acc_acc': 1})
        f = open("sambutan.txt", "w")
        f.write("PAGI BOSS")
        f.close()
        f = open("sambutan.txt", "r")
        print(f.read())
        f.close()

    else:
        with open('users.csv', 'a', newline='') as file:
            fieldnames = ['acc_name', 'acc_pass', 'acc_acc']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'acc_name': nama, 'acc_pass': newsandi, 'acc_acc': 0})
        f = open("sambutan.txt", "w")
        f.write("halo users")
        f.close()
        f = open("sambutan.txt", "r")
        print(f.read())
        f.close()
        

if os.path.exists("sambutan.txt"):
    os.remove("sambutan.txt")
f = open("sambutan.txt", "x")
f.close()



while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM ADMINISTRASI WARGA MEXICO':^40}")
    print(f"{'SILAHKAN MENGIKUTI INTRUKSI DI BAWAH INI':^40}")
    print(f"{'-'*40:^40}")
    
    
    opsi = input(""" \n
    PILIH
    1. LOGIN
    2. REGISTER
    3. Keluar
    
    JAWABANMU:  """)
    
    if opsi == "1":
        NAMA,SANDI = login()
        sambutan(NAMA,SANDI)
        
    elif opsi == "2":
        NAMA,SANDI,ACCSES = input_register()
        registrasi(NAMA,SANDI,ACCSES)
        
        
    elif opsi == "3":
        print(f"{'TERIMA KASIH':^40}")
        break
    
    isContinue = input("Apakah lanjut (y/n)? : ")
    if isContinue == "n" or isContinue == "N":
        print("Program selesai, terima kasih")
        break
    
    
