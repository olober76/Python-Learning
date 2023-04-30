# Tugas Nomer 1
import os 

class Resource:
    def __init__(self,nama,umur, balance):
        self.nama = nama
        self.umur = umur
        self.balance = balance
        
        
class CheckingUmur(Resource):
    def __init__(self, nama, umur, balance):
        super().__init__(nama, umur, balance)
    
    def age(self, age,balance):
        if age < 30 :
            self.balance += (5/100 * self.balance)
    
class CheckingStatus(Resource):
    def __init__(self, nama, umur, balance):
        super().__init__(nama, umur, balance)
        
    def karyawan(self):
        gajiKaryawan = self.balance + 100000

    def TenagaLepas(self):
        gajiTenagaLepas = self.balance + (1/100 * self.balance)
        
    
    def AnalisData(self):
        self.balance += (10/100 * self.balance) + 250000
       
        
    
    

     


while True:
    
    print('''
        Menu:
        1. Karyawan
        2. Tenaga Lepas
        3. Analisis data
        4. Keluar    
      
      ''')

    masukkan = int(input("Pilih menu: "))
    
    
    match masukkan:
        case 1:
            nama = input("Masukkan nama karyawan: ")
            Usia = int(input("Masukkan usia karyawan: "))
            balance = int(input("Masukkan pendapatan karyawan: "))
            status  = CheckingStatus(nama, Usia, balance)
            gaji = CheckingStatus.karyawan()
            print(f"Total Pendapatan karyawan: {gaji:.2f}")
            
            
        case 2:
            nama = input("Masukkan nama tenaga lepas: ")
            Usia = int(input("Masukkan usia karyawan: "))
            balance = int(input("Masukkan pendapatan karyawan: "))
            status  = CheckingStatus(nama, Usia, balance)
            gaji = CheckingStatus.TenagaLepas()
            print(f"Total Pendapatan karyawan: {gaji:.2f}")
            
            
        case 3:
            nama = input("Masukkan nama analis data: ")
            Usia = int(input("Masukkan usia karyawan: "))
            balance = int(input("Masukkan pendapatan karyawan: "))
            status  = CheckingStatus(nama, Usia, balance)
            gaji = CheckingStatus.AnalisData()
            print(f"Total Pendapatan karyawan: {gaji:.2f}")
            
            
        case 4:
            print("Terima kasih telah menggunakan program ini")
            break
            