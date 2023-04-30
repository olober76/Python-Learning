# Operaasi dalam Dictionary

data_dict = {
    "cup" : "ucup surucup",
    "tng" : "otong surotong",
    "dng" : "dudung surudung",
    }

#panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")


# deteksi key exist atau tidak
# KEY = "cup"
KEY = "kis"
CHECKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKEY}")


# mengakses value {read} dengan get
print(data_dict["cup"]) # cara biasa
print(data_dict.get("cup")) # menggunakan get
print(data_dict.get("kis")) # jika key tidak sesuai, outputnya akan "None" 
#print(data_dict["kis"]) akan error jika menggunakan cara ini 
print(data_dict.get("kis", "key tidak ditemukan")) # jika key tidak sesuai, makan error akan memunculkan argumen kedua


# updating data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep" # adding more data in dictionary
print(data_dict)

data_dict.update({"cup":"ucup surucup"}) # edit data di dictionary menggunakan update
print(data_dict)
data_dict.update({"kup":"duta kupri"}) # adding more data in dictionary by using .update()
print(data_dict)


# deleting data in dictionary
del data_dict["kup"]
print(data_dict)