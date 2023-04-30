# Getter and Setter
class Hero:
   
    #private class variable
    
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth : {}".format(self.__name,self.__health)
        # self.__info = "name {} : \n\thealth : {}".format(self.name,self.__health)

    #Getter
    @property
    def info(self):
        return "name {} : \n\thealth : {}".format(self.name,self.__health)
    
    # @property
    # def info2(self):
    #     return self.__info
    
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    # Setter
    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None
    

sniper = Hero('sniper', 100, 10)
print(sniper.info) # agar variable info tidak bisa di edit
sniper.name = 'dadang'
print(sniper.info) # agar variable info tidak bisa di edit
print(sniper.__dict__)

print("getter dan setter untuk __armor :")
print(sniper.armor)

sniper.armor = 50
print(sniper.__dict__)

print("delete armor")
del sniper.armor

print(sniper.__dict__)



