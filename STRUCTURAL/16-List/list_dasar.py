## --- LIST ----

# Kumpulan data numbers
data_angka = [1,5,2,3] #urutan indeks dimulai dari yang ke 0
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)

# Kumpulan data Boolean
data_boolean = [True, False, True, False]
print(data_boolean)

#Kumpulan data campuran
data_mixed = [1, "otong", 2, "cireng", "ucup", True, " hada", False]
print(data_mixed)

## cara alternatif membuat list
data_range = range(0,10,2) # range (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list denga  for loop, list comperhension
data_listFor = [i for i in range(0,10)]
print(data_listFor)

# Membuat list pake for pake if
data_ListForIf = [i for i in range(0,10) if i != 5]
print(data_ListForIf)

data_ListForIf = [i for i in range(0,10) if i%2 == 0]
print(data_ListForIf)

data_ListForIf = [i**2 for i in range(0,10) if i%2 != 0]
print(data_ListForIf)