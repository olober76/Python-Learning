while True:
    angka = int(input("Masukkan angka : "))
    
    if angka <= 0 :
        print("\n\nOnly Bilangan Bulat BOSSSS\n\n")
        
    
    if angka%2 == 0 and angka != 0 : 
        print(f"{angka} \n")
    elif angka%2 != 0 and angka != 0:
        print("Bukan bilangan genap! \n")