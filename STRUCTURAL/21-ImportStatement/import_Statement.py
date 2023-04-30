# Import statement
# Fungsinya untuk mengambil program dari file external .py


# 1. Untuk menyambung program dari external
import program_print
import program_jaka

# 2. import dengan data
import variable
import kupri

# data ada di namespace variable
print(variable.data)
print(kupri.data)


# 3. import dengan fungsi 
import matematika
hasil = matematika.tambah(4,5)

print(hasil)