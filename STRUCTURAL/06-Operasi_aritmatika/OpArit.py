# Operaso Aritmatika

a = 10;
b = 3;

#Opearsi tambah +
hasil = a + b;
print(a, '+', b, '=', hasil);

#Opearsi minus -
hasil = a - b;
print(a, '-', b, '=', hasil);

#Opearsi perkalian *
hasil = a * b;
print(a, '*', b, '=', hasil);

#Opearsi pembagian /
hasil = a / b; #hasilnya bisa langsung menjadi float tanpa harus dicasting datanya
print(a, '/', b, '=', hasil);

#Opearsi eksponen (pangkat) **
hasil = a ** b;
print(a, '**', b, '=', hasil);

#Opearsi modulus % (sisa pembagian)
hasil = a % b;
print(a, '%', b, '=', hasil);

#Opearsi floor division //
hasil = a // b; # hasil pembagiaan akan dibulatkan ke bawah
print(a, '//', b, '=', hasil);

print("\n");

#Prioritas operasi, operational presedence\
x = 3;
y = 2;
z = 4;

hasil = x ** y * z + x / y - y % z // x
# Urutan prioritas jenis operasi
#([ Jenis operasi apapun] )
#eksponen
#Perkalian meliputi * / % //
#Pertambahan + -
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x , '=', hasil);