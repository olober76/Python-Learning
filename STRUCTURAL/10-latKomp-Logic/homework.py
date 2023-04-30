#Soal nomor 1 ---------0++++++++5--------8++++++11------ 
#Soal nomor 2 +++++++++0--------5++++++++8------11++++++

inputUser = float(input("Masukkan Angka : "))

#Soal Nomor 1
# --------0+++++++5--------
inputKomp1 = 0 < inputUser < 5
print("bilangan berada di range 0 < x < 5 = ", inputKomp1 )

# --------8+++++++11--------
inputKomp2 = 8 < inputUser < 11
print("bilangan berada di range 8 < x < 11 = ", inputKomp2 )

# ---------0++++++++5--------8++++++11------ 
isCorrect = inputKomp1 or inputKomp2
print("Apakah input memenuhi komparasi 0 < x < 5, atau 8 < x < 11 = ", isCorrect)

print("\n", 10*"=", "\n")


#Soal Nomor 2
# ++++++++0---------5++++++++
inputKomp3 = (inputUser < 0) or (5 < inputUser < 8)
print("bilangan berada di range x < 0 atau 5 < x < 8 = ", inputKomp3 )

# ++++++++++8---------11++++++++++
inputKomp4 = (5 < inputUser < 8) or (inputUser > 11)
print("bilangan berada di range 5 < x < 8 atau x > 11", inputKomp4 )

# ++++++++++0---------5++++++++++8---------11++++++++++ 
isCorrect = inputKomp3 or inputKomp4
print("Apakah input memenuhi komparasi x < 0 atau 5 < x < 8 atau x > 11 = ", isCorrect)


