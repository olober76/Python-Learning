# Date and Time (latihan)
# Sumber referensi library https://docs.python.org/3/library/datetime.html

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2002,7,20)
print(tanggal)
print(f"Ulang tahun saya = {tanggal:%A}")

print("\n" + 5*"=" + "DATE TIME DENGAN INPUT USER" + 5*"=" + "\n")

print("Silahkan masukkan tanggal, \nbulan, dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t: ")) 
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_hari.days % 365) % 30


print(umur_hari.days)
print(f"Umur anda adlah : {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari")