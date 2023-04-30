# tipe data adalah macam macam dataa 
# yang bisa dimasukkan ke dalam program python
# a = 10, a adalah variable nilai 10

# tipe data: integer
data_integer = 5
# tips : syntax type("data yang dipanggil") bisa digunakan untuk mengetahui tipe data dari suatu variable yang dipanggil
print("data : ", data_integer)
print( "bertipe :", type(data_integer))

# tipe data: float
# NB : variable float dan double tidak dibedakan dan dijadikan menjadi satu
data_float = 1.5
print("data : ", data_float)
print( "bertipe :", type(data_float))

# tipe data: string (kumpulan karakter)
data_string = "ucup 10"
print("data : ", data_string)
print( "bertipe :", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print( "bertipe :", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print( "bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print( "bertipe :", type(data_c_double))
