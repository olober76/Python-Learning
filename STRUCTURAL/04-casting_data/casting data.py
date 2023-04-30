#casting
# Merubah dari satu tipe data ke tipe data lain

##INTEGER
print("===========INTEGER===========");
data_int = 9;
print("data = ",data_int, "type = ", type(data_int))

# Operator casting 
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #selain  nilai int = 0 , nilai pada bool akan selalu true

print("data = ",data_float, "type = ", type(data_float))
print("data = ",data_str, "type = ", type(data_str))
print("data = ",data_bool, "type = ", type(data_bool))

print("\n");


##FLOAT
print("===========FLOAT===========");
data_float = 9.7;
print("data = ",data_float, "type = ", type(data_float))

# Operator casting 
data_int = int(data_float) #akan dibulatkan ke bawah berapapun nilainya di belakang koma
data_str = str(data_float)
data_bool = bool(data_float) #selain  nilai float = 0 , nilai pada bool akan selalu true

print("data = ",data_int, "type = ", type(data_int))
print("data = ",data_str, "type = ", type(data_str))
print("data = ",data_bool, "type = ", type(data_bool))

print("\n");

##BOOLEAN
print("===========BOOLEAN===========");
data_bool = False;
print("data = ",data_bool, "type = ", type(data_bool))

# Operator casting 
data_int = int(data_bool) #akan dibulatkan ke bawah berapapun nilainya di belakang koma
data_str = str(data_bool)
data_float = float(data_bool) 

print("data = ",data_int, "type = ", type(data_int))
print("data = ",data_str, "type = ", type(data_str))
print("data = ",data_float, "type = ", type(data_float))

print("\n");


##STRING
print("===========STRING===========");
data_str = "60";
print("data = ",data_str, "type = ", type(data_str))

# Operator casting 
data_int = int(data_str); #harus angka pada string
data_float = float(data_str); #harus angka pada string
data_bool = bool(data_str) ; # nilai bool bisa false jika nilai pada variable string tidak ada / ""

print("data = ",data_int, "type = ", type(data_int))
print("data = ",data_float, "type = ", type(data_float))
print("data = ",data_bool, "type = ", type(data_bool))

print("\n");






