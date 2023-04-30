# Deep Copy list
data_0 =  [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1, 10]
data_2D_copy =  data_2D.copy()

print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

# Mengambil data dari nested list

data = data_2D[0]
print(f"data = {data}")

data = data_2D[0][0]
print(f"data = {data}")

data = data_2D[0][1]
print(f"data = {data}")

# Addres semuanya
print(f"address asli data_2D = {hex(id(data_2D))}")
print(f"address copy data_2D = {hex(id(data_2D_copy))}\n")

print("addres dari member ke-1")
print(f"address asli data_2D = {hex(id(data_2D[0]))}")
print(f"address copy data_2D = {hex(id(data_2D_copy[0]))}\n")


data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

# kita gunakan deep copy

from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli data_2D = {hex(id(data_2D))}")
print(f"address deep data_2D = {hex(id(data_2D_deepcopy))}\n")

print("addres dari member ke-1")
print(f"address asli data_2D = {hex(id(data_2D[0]))}")
print(f"address deep data_2D = {hex(id(data_2D_deepcopy[0]))}\n")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep= {data_2D_deepcopy}\n")