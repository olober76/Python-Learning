# Latihan konversi satuan temperature

# Celcius (4/5 C untuk ke R), (9/5C+32 untuk ke F), (C+273 untuk ke K)
# Reamur (5/4 R untuk ke C), (9/4 R + 32 untuk ke F), (5/4K + 273 untuk ke K)
# Fahrenheit (5/9(F-32) untuk ke C), (4/9(F-32) untuk ke R)
# Kelvin (K-273 untuk ke C), (4/5(K-273) untuk ke R)

# Program konversi celcius ke satauan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

#celcius
celcius = float(input('Masukkan suhu dalam Celcius : '))
print("Suhu adalah ", celcius, " Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah ", reamur, " reamur")


# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, " fahrenheit")


#Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, " kelvin")


#Rumus fahrenheit ke kelvin
fahrenheit2 = float(input('\nMasukkan Suhu Fahrenheit : '))
kelvin = ((5/9)*(fahrenheit2 - 32) + 273)
print("Suhu dalam kelvin adalah ", kelvin, " kelvin")


#Rumus kelvin ke fahrenheit
kelvin2 = float(input('Masukkan Suhu kelvin : '))
fahrenheit = ((9/5)*(kelvin2 - 273) + 32)
print("Suhu dalam fahrenheit adalah ", fahrenheit, " fahrenheit")
