#contiune, pass, break

#Pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi

angka = 0
while angka < 5:
     angka += 1
     if angka == 3:
        #print("whadaap!")
        pass # tidak akan di eksekusi dan akan di anggap sebagai dummy command
     print(angka)

# continue
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice")
        continue # print whassup akan langusn dilewati dan loop meloncat ke state selanjutnya
    print("whassup!")

print("pinishh")


# Break

data_int = int(input("hitung sampai = "))

#contoh pertama
angka = 0

while angka < 5:
    angka += 1 
    print(f"count -> {angka}")

    if angka == 3: 
        print("nice")
        break #loop urutan ke selanjutnya akan tidak dilanjutkan dan keluar dari looping
    print("whassuo")

print("finish")



# contoh kedua
angka = 0

while True:
    angka += 1 
    print(f"count -> {angka}")

    if angka == data_int: 
        print("nice")
        break #loop urutan ke selanjutnya akan tidak dilanjutkan dan keluar dari looping
    print("whassuo")

print("finish")



