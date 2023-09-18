# FUNGSI DAN DATA

def function_name():     # isi kerangka fungsi tanpa parameter
    print("what to do") 

function_name() #cara memanggil fungsi


def utang(nominal):  #mominal == parameter
    print("pinjem dulu " + nominal) # argumen
        
utang("seratus")


#ARBITRARY ARGUMENTS *

def mahasiswa(*nama):
    print("yang datang kelas pertama " + nama[0]) #indeks dari awal, nama di sini adalah tuple
    #tuple bersifat statis
    
    print("yang datang kelas pertama " + nama[len(nama) - 1]) #indeks dari akhir
    
mahasiswa("Ravi", "Jason", "Gavin")



#Parameter 2 
def function_name(par1, par2):
    print("we go from " + par1 + " to " + par2)

function_name(" malang ", " osaka")

#Key value syntax 
def function_name(par1, par2):
    print("we go from " + par1 + " to " + par2)

function_name(par1= " malang ", par2= " osaka")


#list as argumen 
def mahasiswa(nama):
    for x in nama:
        print(x)
        

listmhs = ["Ravi", "Jason", "Gavin"]
mahasiswa(listmhs)


#return value
def utang(nominal):  #mominal == parameter
    print("pinjem dulu " + nominal) # argumen
        
utang("seratus")
 
 
#rekurkrsi

#n! = n* (n - 1)

def factorial(n):
    if (n==1):
        return n
    else:
        return n*(factorial(n-1))


factorial(5)

print(factorial(100))

   