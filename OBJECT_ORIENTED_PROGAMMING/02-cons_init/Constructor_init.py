class Hero: #Template
    
    def __init__(self,inputName, inputHealth, inputPower, inputArmor): #self berperan sebagai penopang variabel baru
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        # print("halo", x)
    


hero1 = Hero("sniper",100, 10, 4)
hero2 = Hero("Sven", 100 , 15, 1)
hero3 = Hero("Olober", 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)