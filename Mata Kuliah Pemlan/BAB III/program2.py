while True:
    inputan = input("Masukkan input: ")
    print(inputan, type(inputan))
    
    angka = inputan.split()
      
    n = int(angka[0])
    m = int(angka[1])
    l = int(angka[2])
    
    print('n =', n, " Tinggi Karton")
    print('m =', m, " Lebar Karton")
    print('l =', l, " Tebal Karton")
    
    print('-' * 20)
    BoldPattern = "*" * m
    Midlepattern = "*" * l + "." * (m-l)
    for tinggi in range(n):
        if l >= n/2 :
            print("gabisa bos kalo Tebal karton lebih dari setengah tinggi dan lebarnya \n\n")
            break
        if tinggi < l or tinggi > (n-l-1):
            print(BoldPattern)
        else:
            print(Midlepattern)
    

