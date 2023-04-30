# Format String

# contoh generic
nama = "marlene"
str = "hello " + nama

print(str)

# using formatting (string)
nama = "marlene"
format_str = f"hello {nama}"

print(format_str)

# using formatting (boolean)
boolean = True 
format_str = f"boolean = {boolean}"
print(format_str)

# using formatting (angka)
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# using formatting (bilangan bulat)
angka = 15
format_str = f"bilangan bulat = {angka:d}" #harus bertipe integer
print(format_str)

# using formatting (bilangan dengan ordo ribuan)
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# using formatting (bilangan desimal)
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" #untuk membatasi output berapa angka dibelakang koma
print(format_str)

# using formatting (leading zero)
angka = 2005.54321
format_str = f"desimal = {angka:08.2f}" #nge geser angka kekiri dengan 0 atau spasi
print(format_str)

# using formatting (tanda + atau - )
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus) 

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

#tambahan
#melakukan aritmetika didalam formating placeholder
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# Format angka lain like binary, hex, octal
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)