# Pengenalan string

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''
   1. Dengan menggunakan single quote '...'
   2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')# tanda double quote akan dianggap sebagai karakter di dalamnya
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

#2. Menggunakan back slash (\)

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day,isn\'t it?')

# Backslash
print("C\\User\\Ucup") #membuat backslash menjadi salah satu dari karakter dalam string

# tab
print("Ucup\t\t\t\totong,  semakin jauh")

#backspace
print("ucup \botong, jadi deketan")

# newLine
print("baris pertama. \nbaris kedua.") #LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.")#CRLF -> Line feed carriage return -> dipakai oleh windows

# 3. string literal atau raw

# hati - hati
print('C:\new folder')# akan salah pathnya
print()

# menggunakan raw string
print(r'C:\new folder')
print(r'C:\new \t\n\b\\\rfolder')# karakter khusus akan dijadikan string semua

# Multiline literal string
print("""
Nama  : Ucup
Kelas : 3 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama    : Ucup
Kelas   : 3SD \new normal
Website : Www.ucup.com/NewID
""")
