# Operator Assignment
# Operasi yng dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 #adalah assignment
print("Nilai a =", a)

a += 1 #ini artinya a = a + 1
print("Nilai a+=1, nilai a menjadi  =", a)

a -= 2 #ini artinya a = a - 2
print("Nilai a-=2, nilai a menjadi  =", a)

a *= 5 #ini artinya a = a * 5
print("Nilai a*=5, nilai a menjadi  =", a)

a /= 2 #ini artinya a = a / 2
print("Nilai a/=2, nilai a menjadi  =", a)

b = 10
print("\nnilai b =", b)

#Modulus dan floor division
b %= 3
print("Nilai b%=3, nilai b menjadi  =", b)

b = 10
print("\nnilai b =", b)

print("Nilai b//=3, nilai b menjadi  =", b)

# Pangkat atau eksponen
a = 5
print("Nilai a =", a)
a **= 3
print("Nilai a**=3, nilai a menjadi  =", a)

#Operasi Bitwise
#OR
c =  True
print("\nnilai c =", c)
c |= False
print("Nilai c |= false, nilai c menjadi  =", c)

c =  False
c |= False
print("Nilai c |= false, nilai c menjadi  =", c)

#AND
c =  True
print("\nnilai c =", c)
c &= False
print("Nilai c &= false, nilai c menjadi  =", c)

c =  True
c &= True
print("Nilai c &= True, nilai c menjadi  =", c)

#XOR
c =  True
print("\nnilai c =", c)
c ^= False
print("Nilai c ^= false, nilai c menjadi  =", c)

c =  True
c ^= True
print("Nilai c ^= True, nilai c menjadi  =", c)

# Shifting
d = 0b0100
print("\nnilai d = ", format(d, '04b'))
d>>=2
print("Nilai d >>= 2, nilai d menjadi  =", format(d, '04b'))

d<<=1
print("Nilai d <<= 1, nilai d menjadi  =", format(d, '04b'))

