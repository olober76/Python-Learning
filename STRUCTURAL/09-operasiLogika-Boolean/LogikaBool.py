# Operasi Logika atau Boolean

# not, or, and, xor

# NOT
print('=====NOT=====')
a = False
c = not a
print('data a = ', a)
print('---------NOT')
print('data c = ', c)


# OR (Jika salah satu true, maka hasilnya adalah true)
print('=====NOT=====')
a = False
b = False
c = a or b
print(a,' OR ',b ,'= ', c)
a = False
b = True
c = a or b
print(a,' OR ',b ,' = ', c)
a = True
b = False
c = a or b
print(a,' OR ',b ,' = ', c)
a = True
b = True
c = a or b
print(a,' OR ',b ,'  = ', c)


# AND (Jika salah satu falsese, maka hasilnya adalah false)
print('=====AND=====')
a = False
b = False
c = a and b
print(a,' AND ',b ,'= ', c)
a = False
b = True
c = a and b
print(a,' AND ',b ,' = ', c)
a = True
b = False
c = a and b
print(a,' AND ',b ,' = ', c)
a = True
b = True
c = a and b
print(a,' AND ',b ,'  = ', c)


# XOR (Akan true jika salah satu true, sisanya false)
print('==========')
a = False
b = False
c = a ^ b
print(a,' XOR ',b ,'= ', c)
a = False
b = True
c = a ^ b
print(a,' XOR ',b ,' = ', c)
a = True
b = False
c = a ^ b
print(a,' XOR ',b ,' = ', c)
a = True
b = True
c = a ^ b
print(a,' XOR ',b ,'  = ', c)



