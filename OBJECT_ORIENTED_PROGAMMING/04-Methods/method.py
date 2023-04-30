# Methods

class Hero:
    #Class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # Void function, method tanpa return
    def siapa(self):
        print(f"namaku adalah = {self.name}")
    
    # Method dengan argumen tanpa return
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 20, 5)
hero2 = Hero('mirana', 90, 5, 10)\

# print(hero1.__dict__)
# print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)

print(hero1.__dict__)
print(hero1.getHealth())