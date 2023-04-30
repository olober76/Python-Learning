class Hero: #Template
    # Class variabel
    jumlah = 0
    def __init__(self,inputName, inputHealth, inputPower, inputArmor): #self berperan sebagai penopang variabel baru
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama " + inputName)
    


hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Sven", 100 , 15, 1)
print(Hero.jumlah)
hero3 = Hero("Olober", 1000, 100, 0)
print(Hero.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__) # hero tidak memiliki atribut