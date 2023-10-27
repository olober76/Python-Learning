#Polymorphm

class Hero:
    def __init__(self, name="Hero", hp=1000, energy=100):
        self.name = name
        self.__hp = hp #PRIVATE VARIABLE
        self.energy = energy
        
    def attack(self):
        print("using weapon")
        
    def get__hp(self):
        return print(self.__hp)
        
    def set__hp(self, hp):
        self.__hp = hp
        
class Tank(Hero):
    def attack(self):
        print("using axe")

class Assasins(Hero):
    def attack(self):
        print("using bow")

    def ulti(self):
        pass

class Support(Hero):
    def attack(self):
        print("using staff")
        

tidehunter = Tank(name="tidehunter", hp=3000, energy=500)
tidehunter.attack()

clinkz = Assasins(name="clinkz", hp=1000, energy=700)
clinkz.attack()

# tidehunter.__hp = 1
# print(f"{tidehunter.name} HP is {tidehunter.hp}")

tidehunter.get__hp() #encasulapsi
tidehunter.set__hp(4000)
tidehunter.get__hp()
