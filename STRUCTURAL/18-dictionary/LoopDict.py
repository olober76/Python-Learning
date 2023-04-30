# Looping operation in dictionary

teman_teman = {
    "cup" : "ucup surucup",
    "tng" : "otong surotong",
    "dng" : "dudung surudung",
    "sep" : "asep markasep",
    "cuy" : "ucuy surucuy",
}

# looping first try (yang keluar adalah keynya )
for teman in teman_teman:
    print(teman) # hanya menampilkan key


# operator untuk mengambil item /iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key)) # mengambil value


values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value) # mengambil value

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item) # mengambil item (key dan value akan dipanggil)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}") #editable