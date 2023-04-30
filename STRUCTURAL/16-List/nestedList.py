# Nested List 

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, data_list_biasa,6,7]
print(f"list 2D = {list_2D}")

#Contoh penggunaan

peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Dedeh", 50, "wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")


# dengan reference
list_copy = list_peserta.copy();
print(f"peserta = {list_copy}\n")
peserta_0[0] = "Michael"

print(f"peserta = {list_copy}\n")
print(f"peserta = {list_peserta}") #tidak akan berubah karena reference dari peserta_0 dan sebagainya masih sama dengan yang sebelumnya


