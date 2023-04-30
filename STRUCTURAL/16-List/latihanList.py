# Database sederhana
#Program list buku
# Referensi https://www.youtube.com/watch?v=cS-VYthhO9A&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY

list_buku = []
while True:
    print("\nMasukkan data Buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama Penulis\t: ")
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    
    print("-"*50)
    print("No.\t| Judul\t\t\t| Penulis")
    print("-"*50)
    for index,buku in enumerate(list_buku):
        print(f"{index + 1}\t|{buku[0]}\t\t| {buku[1]}")
    
    print("\n\n","-"*50)
    isLanjut = input("Apakah masih berlanjut? (Y/N)\t: ")
    match isLanjut:
        case "n":
            print("Program Selesai")
            break
        case "N":
            print("Program Selesai")
            break
        case "Y":
            print("\n")
        case "y":
            print("\n")
        case default:
            print("Tidak ada dalam program")
            print("-"*50)
            print("No.\t| Judul\t\t\t| Penulis")
            print("-"*50)
            for index,buku in enumerate(list_buku):
                print(f"{index + 1}\t|{buku[0]}\t\t| {buku[1]}")
            break
            
