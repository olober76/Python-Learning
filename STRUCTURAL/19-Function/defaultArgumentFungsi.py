# Default argument dengan fungsi

# Def fungsi(argument):
# Def fungsi(argument = nilai defaultnya):


def say_hello(nama = "Ganteng"):
    print(f"Hallo {nama}")


say_hello("ucup")
say_hello()

#Contoh 2
def sapa_dia(nama , pesan = "apa kabar?"):
    #Fungsi dengan satu input biasa, dan satu default argument
    print(f"hai {nama}, {pesan}")


sapa_dia("Dudung", "hai ganteng")
sapa_dia("Otong")

# Contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil)

#Contoh 4

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))