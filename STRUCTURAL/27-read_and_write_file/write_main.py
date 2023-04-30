

# 1. mode write

# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt",'w', encoding="utf-8") as file:
    file.write("Duta Kukuh Pribadi")



with open("data_1.txt",'w', encoding="utf-8") as file:
    file.write("Olober SYKES")

# 2. mode append

with open("data_2.txt",'w', encoding="utf-8") as file:
    file.write("Olober Sykes\n")

# with open("data_2.txt",'a', encoding="utf-8") as file:
#     file.write("Olober Sykes\n")


with open("data_2.txt",'a', encoding="utf-8") as file:
    file.write("Duta Kukuh Pribadi\n")

with open("data_2.txt",'a', encoding="utf-8") as file:
    file.write("nambah lagi dengan append\n")


# 3. mode r+
with open("data_3.txt" , 'w', encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("baris satu\n")
    file.write("baris kedua \n")
    file.write("baris ketiga \n")
    
with open("data_3.txt", 'r+', encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("baris ketiga\n")
    
    