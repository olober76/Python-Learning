#Tuples dan set

#list
data_list = [1,2,3,4,5] # menggunakan kurung siku
print(data_list)

#Tuples
data_tuples = (20,11,7,8,9,10) #menggunakan kurunng lengkung
print(data_tuples)
print(data_tuples[1])
# data tuples tidak memenuhi operasi assignmen
# data tuples harus satu jenis
# dengan kata lain tidak bisa mengubah isi data dari tuples
# tidak bisa menggunakan syntax misal
# data_tuples[1] = "ucup"
#data_tuples.append(1)

#Set (himpunan)
data_sets= {10,4,3,2,4,7,6,5} #kumpulan data yang tidak memiliki indeks
# data yang sama akan dikeluarkan satu kali, misal data bernilai 4
#data akan diurutkan mulai dari terkecil
#data bisa di append atau di cal(dijumlahkan) 
print(data_sets)
# sehingga kita tidak bisa memanggil salah satu datanya, harus dipanggil semuanya#
# misal kita tidak bisa menggunakan syntax seperti
# print(data_sets[0])