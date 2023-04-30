# Operasi dan manipulasi string

#1. menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah  = "D"
nama_akhir   = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'"  + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string
# 3.1 mengecek apakah ada komponen char atau string di string
d = "ucup"
status = d in nama_lengkap
print( d + " ada di string " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print( D + " ada di string " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print( d + " tidak ada di string " + nama_lengkap + " = " + str(status))


# 3.2 mengulang string
print("wk"*10)
print(10*"wk")

# 3.3 indexxing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1]) 
print("index ke-(-2) : " + nama_lengkap[-2]) 
print("index ke-[0:3] : " + nama_lengkap[0:4]) # index yang terakhir tidak di ikutsertakan ibarat 0 <= x < 4
print("index ke-[3:7] : " + nama_lengkap[3:8]) 
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2]) 

# 3.4 item paling kecil
print("Paling kecil : " + "(" + min(nama_lengkap) + ")" )
# 3.5 item paling besar
print("Paling besar : " + "(" + max(nama_lengkap) + ")" )

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))