def check(original, edited):
    return original == edited

def reversed(word):
    return word[::-1]

n = int(input("Jumlah huruf yang ingin diperiksa : "))
for i in range(n):
    kata = input("Tuliskan sebuah kata : ")
    reversed_word = reversed(kata)
    if check(kata, reversed_word):
        print(f"palindrome.")
    else:
        print(f"is not palindrome.")
