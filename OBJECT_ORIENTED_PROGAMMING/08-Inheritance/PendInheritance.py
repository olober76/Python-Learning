class Hero:
    
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
        

class Hero_intelligent(Hero):
    pass


class Hero_streghth(Hero):
    pass
        
lina = Hero('lina', 100)
techies = Hero_intelligent('techies',50)
axe = Hero_streghth('axe',100)


print(lina.name)
print(techies.name)
print(help(axe))
print(techies.__dict__)
print(axe.__dict__)