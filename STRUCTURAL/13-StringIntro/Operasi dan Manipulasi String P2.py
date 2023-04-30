# Operator dalam bentuk methods

## Merubah case dari string

# Merubah semua ke upper case
salam = "bro!"
print("Normal = " + salam)

salam = salam.upper()
print("Upper = " + salam)

# Merubah semua ke lower case
alay = "aKU kECE AbieeZzzZZzZZZ"
print("normal = " + alay)

alay = alay.lower()
print("lower = " + alay)

## Pengecekan dengan menggunakan isX method

# contoh untuk pengecekan lower case
salam = "sist"
is_Lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(is_Lower))
is_upper = salam.isupper() #hasilnya bool
print(salam + " is upper = " + str(is_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek angka saja
# isspace() <-- untuk mengecek spasi, tab, newline \n
# istitle() <-- untuk mengecek semua kata dimulai dengan huruf besar
# referensi string methods https://www.w3schools.com/python/python_ref_string.asp

judul = "It Is Okay Not To Be Orkay" #tanda kutip akan membuat false pada istitle
cek_judul = judul.istitle() #hasil bool
print(judul + " is title = " + str(cek_judul))

## Ngecek Komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") #case sensitive
print("start = " + str(cek_start))

cek_end = "Sangjanim Oppa".endswith("Oppa") #case sensitive
print("end = " + str(cek_end))

## Penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu'] #list
gabung = ','.join(pisah)#string di awal sebagai penyeka tiap indeks list
print(pisah)
print(gabung)

gabung=' '.join(pisah)
print(gabung)

gabung=' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm')) #output berupa list

# alokasi karakter rjust(), ljust() center()
print(5*"=" + "data" + "="*5)

#right justify
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20, "-") #jika ingin penambahan justify yang bukan spasi, harus menambahkan satu karakter yang diinginkan
print("'"+tengah+"'")

#kebalikannya -> strip()
tengah = tengah.strip("-") #menghilangkan justify
print("'"+tengah+"'")

kanan = kanan.strip() #menghilangkan justify
print("'"+kanan+"'")





