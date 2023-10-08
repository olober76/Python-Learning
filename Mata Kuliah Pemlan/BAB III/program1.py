# Tugas nomer 1 

while True :
    tahun = int(input("Masukkan tahun yang ingin digunakan : "))
    
    if tahun < 0 :
        print("yang benar saja kao bang")
    elif tahun == 0 :
        print("\n\n\n===============TERIMA KASIH===============\n\n\n")
        break
    
    if tahun%4==0 :
        if tahun%100 == 0 :
            if tahun%400 == 0:
                print(f"tahun {tahun} merupakan tahun kabisat\n")
            else:
                print(f"tahun {tahun} bukan  tahun kabisat\n")
        else:
            print(f"tahun {tahun} merupakan tahun kabisat\n")
    else:
        print(f"tahun {tahun} bukan  tahun kabisat\n")
        