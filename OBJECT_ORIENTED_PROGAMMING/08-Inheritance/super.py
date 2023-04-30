class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("{} dengan Health: {}".format(self.name,self.health))
        
class Hero_Intelligent(Hero):
    def __init__(self, name):
        # self.name = name
        # self.health = 100
        # Hero.__init__(self,name,100)
        super().__init__(name, 100)
        super().showInfo()

class Hero_Strength(Hero):
    def __init__(self, name):
        # self.name = name
        # self.health = 200
        # Hero.__init__(self,name,200)
        super().__init__(name, 200)
        super().showInfo()
        
lina = Hero_Intelligent('lina')
axe = Hero_Strength('axe')

# print(lina.name , " " , lina.health)
# print(axe.name , " " , axe.health)