#Fungsi dengan argument (input)

#def <nama_fungsi>(argument/parameter/input):
    #badan fungsi

# argument bisa berisi string, bboolean, number ,dsb
def hello_world(nama):
    #badan fungsi hello world menerima input dengan variable nama
    print(f"Selamat datang dunia wahai {nama}")


hello_world("kukuh")
hello_world("fawwaz")

def tambah(angka_1,angka_2):
    #fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(6969,69)

def say_hi(list_peserta):
    list_peserta[1]= "duta"
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")


anggota_boyband = ["fawwaz", "kukuh", "felix"]


say_hi(anggota_boyband)
print(anggota_boyband[1])