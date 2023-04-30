# latihan sederhana

sisi = 20

#1. Using For
#dummy variable
print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for\n")
# 2. Menggunakan While

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir dari while\n")

# 3. Hanya ganjil saja

print("awal while")
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if (count%2) : #bernilai genap
        # print(f"nilai count  {count}")
        print("*"*count)
        count += 1
    else :
        count += 1
        continue
        
    # akan print jika genap
    # print("*"*count)
    # count += 1

    # akan break jika melebihi sisi
    if count > sisi:
        break


print("akhir dari while\n")


# segitiga dengan spasi

print("===============awal while================")
count = 1
spasi = int(sisi/2)
print(spasi)

while True:
    # akan kembali ke atas jika ganjil
    if (count%2) : #bernilai genap
        # print(f"nilai count  {count}")
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else :
        count += 1
        continue
    
    
    # akan print jika genap
    # print("*"*count)
    # count += 1

    # akan break jika melebihi sisi
    # if count > 10 :
    #     if (count%2) : #bernilai genap
    #     # print(f"nilai count  {count}")
    #         print(" "*spasi,"*"*count)
    #         spasi += 1
    #         count += 1
    #     else :
    #         count += 1
    #         continue


    if count > sisi:
        break
    
                
    


print("akhir dari while\n")