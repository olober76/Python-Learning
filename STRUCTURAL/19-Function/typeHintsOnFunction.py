#Type Hints untuk fungsi

#Bentuk standar fungsi yang udah kita pelajari


# def fungsi(parameter):
#     hasil = parameter**2
#     print(hasil)


# fungsi(1)
# fungsi("Ucup")
# fungsi(True)


import string
#Penggunaan type hints


def sepuluh_pangkat(argument:int) -> int:
    #Fungsi dengan hints
    output = 10**argument
    return output


HASIL = sepuluh_pangkat(2)
print(HASIL)


def display(argument:string):
    print(argument)

display("Ucup")

import os

hasil = os.system("cls")
print(hasil)