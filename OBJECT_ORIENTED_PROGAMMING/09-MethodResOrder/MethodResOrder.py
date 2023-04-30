class A:
    def show(self):
        print("ini A")
        
class B:
    
    def show(self):
        print("ini B")
    

class C(B,A):
    pass
    # def show(self):
    #     print("ini C")
    
    

objek = C()
objek.show()
# help(objek)