from collections import Counter
import os

def remov_duplicates(input):
    input = input.split(" ")
    
    for i in range(0, len(input)):
        input[i] = "".join(input[i])
    UniqW = Counter(input)
    s = " ".join(UniqW.keys())
    print (f"""
        
           ========
           REMOVE DUPLICATE
           ========
           
           {s}
           
           """)
    
    
if __name__ == "__main__":
    while True:
        os.system("cls" if os.name == "nt" else "clear") 
        masuk = input ('Masukkan kata yang ingin di proses : \n\n')
        remov_duplicates(masuk)