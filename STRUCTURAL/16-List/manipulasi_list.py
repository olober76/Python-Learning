## Operasi

# index dimulai dari 0
data = ["ucup", "otong", "DUdung"]
# index  0(-3),  1(-2),    2(-1)

# Mengambil data dari list ini
data_0 = data[0]
print(f"data pertama atau indeks ke 0 = {data_0}")
# jika tidak mengerti ukuran dari indeks dari list, maka cukup memanggil indeks ke -1 untuk indeks terakhir
data_last = data[-1]
print(f"data terakhir adalah = {data_last}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil jumalh ingpo indeks dalam list
panjang_data = len(data)
print(f"panjang data  = {panjang_data}")

#menambahkan item pada list sesuai posisi\
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep") # nama_list.insert(posisi_indeks,data_input)
print(f"data sesudah ditambah = \n{data}")

#menambah data di akhir list
data.append("jajang")
print(f"data ditambah lagi = \n{data}")

#menambah list dengan list
new_data = ["Ujang", "Usep", "Dadang"]
data.extend(new_data)
print(f"data gabungan menjadi = \n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah menjadi = \n {data}")

# meremove data
data.remove("Ujang") #nama data yang dihapus harus sesuai (case sensitive)
print(f"data remove = \n {data}")

#remove data paling belakang
data_last = data.pop()
print(f"data akhir = {data}")

print(data_last)