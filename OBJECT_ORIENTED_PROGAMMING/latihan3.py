from modulHeroL3 import Hero_intelligent,Hero_Strength

lina = Hero_intelligent('lina')
slardar = Hero_Strength('slardar')

lina.showInfo()
slardar.showInfo()

lina.gainExp = 200
slardar.gainExp = 250
lina.showInfo()
slardar.showInfo()

