#**kwargs

def fungsi(nama, tinggi, berat):
    #fungsi biasa
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("ucup", 183, 79)

def fungsi(**kwargs):
    #fungsi kwargs
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup", tinggi=183, berat=79) #data yang masuk menjadi dictionary


# Studi kasus
# *args untuk angka sedangkan **kwargs untuk keyword
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali" :
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")


    return output


hasil = math(1,2,3,4,5,6,option="tambah")
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,5,6,option="kali")
print(f"hasil kali {hasil}")