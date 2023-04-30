# Copy dictionary

teman_teman = {
    "cup" : "ucup surucup",
    "tng" : "otong surotong",
    "dng" : "dudung surudung",
    "sep" : "asep markasep",
    "cuy" : "ucuy surucuy",
}

friends = teman_teman # metode biasa

print(f"teman teman: {teman_teman}\n")
print(f"Friends : {friends}\n")

teman_teman["cup"] = "ucup si kerend"
print(f"teman teman: {teman_teman}\n")
print(f"Friends : {friends}\n")

# sama seperti list, jika data pada teman_teman diubah, maka perubahan itu juga di ikuti oleh friends

print(f"\n\n MENGGUNAKAN COPY\n")
friends = teman_teman.copy() # menggunakan copy
print(f"teman teman: {teman_teman}\n")
print(f"Friends : {friends}\n")

teman_teman["cup"] = "ucup si jelek"
print(f"teman teman: {teman_teman}\n")
print(f"Friends : {friends}\n") # data copy tidak akan berubah


# Pop dictionary
print("\n\nPOP Dictionary\n")
dataAsep = friends.pop("sep")
print(f"data asep: {dataAsep}\n")
print(f"Friends : {friends}\n") # data asep diambil atau ditransfer ke variabel yang menggunakan pop

#Pop Item dictionary
print("\n\nPOPITEM Dictionary\n")
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}\n")
print(f"Friends : {friends}\n") 

