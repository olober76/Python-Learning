# Latihan Encapsulasi

class Hero:

    #Private class variable
    __jummlah = 0

    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jummlah += 1
        
    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {:.2f}".format(self.__name,self.__level,round(self.__health,2),self.__healthMax,self.__attPower,self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            
            
            self.__healthMax = self.__healthStandar * self.__level
            self.__health = self.__healthMax
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
                
        
    def attack(self,musuh):
        self.gainExp = 50
        musuh.__health -= (self.__attPower / (3/4 * musuh.__armor))
    
    
    
slardar = Hero('slardar',100,40,10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)
print(axe.info)


slardar.attack(axe)
print(slardar.info)
print(axe.info)
slardar.attack(axe)


slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)
print(axe.info)

