# Static and Classic Method

class Hero:
    #private class variabel
    __jumlah = 0;
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objeck tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # Method static (decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowRanger = Hero('drowranger')
print(Hero.getJumlah3())
print(sniper.getJumlah3())
# print(Hero.__jumlah)
