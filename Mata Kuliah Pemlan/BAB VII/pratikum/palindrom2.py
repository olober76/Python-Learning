
def palindrom_checker(word):
    checker = word[::-1]
    if word == checker:
        return "Palindrom"
    else:
        return "Bukan Palindrom"


while True:
    checker_Results = []
    many = int(input("Berapa Banyak Kata yang mau diperiksa? : "))
    for i in range(many):
        kata = input(f"Masukkan kata {i + 1} : ")
        checker_Results.append(palindrom_checker(kata))
    for i in range(many):
        print(checker_Results[i])

        