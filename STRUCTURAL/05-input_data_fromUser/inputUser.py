# how to comment selected lines :  Ctrl+K+C
# how to uncomment selected lines : Ctrl+K+U


# Data yang dimasukkan pasti string
data = input("Masukkan data : ")
print ("data = ", data, "type =  ", type(data))

print("\n")

#Jika ingin mengambil inputan tipe data int, maka
angka = float(input("Masukkan angka : "))
angka = int(input("Masukkan angka : "))
print ("data = ", angka, "type =  ", type(angka))

print("\n")

# Bagaiman dengan boolean
# Input dari boolean harus diubah menjadi int terlebih dahulu untuk bisa mendeteksi nilai False Bool
data_bool = bool(int(input("masukkan nilai boolean : ")))
print ("data = ", data_bool, "type =  ", type(data_bool))