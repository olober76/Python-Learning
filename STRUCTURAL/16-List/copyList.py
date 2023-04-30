## TEKNIK MENDUPLIKAT LIST

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a #alamat a dan alamat b akan sama
print(f"b = {b}")

# Merubah member dari a

# Merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address b = {hex(id(b))}")
print(f"address a = {hex(id(a))}")

# Menduplikat list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy() # alamat c tidak akan sama dengan alamat a / full duplicate

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

