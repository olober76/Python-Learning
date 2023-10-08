#Inheritance #OBJECT ORIENTED PROGAMMING

#Dalam pemrogaman, kita alangkah baiknya menggambar dulu diagram yang diperlukan untuk membuat kerangkaa berpikir

class Hero:
    def __init__(self, name="hero", hp = 500 , atk=100,  armor=50, energy=200 ): # constructor
        ''' 
            self merujuk apada diri atau object 
            yang dimaksud
        '''
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.energy = energy
        print(f"{self.name} summoned !")
        print(f"{self.energy} energized !\n")
    
    def attack(self, target):
        print(f"{target.name} HP is {target.hp} before getting rekted out")
        target.hp -= (self.atk-target.armor)
        print(f"{self.name} menyerang {target.name} sebesar {self.atk}")
        print(f"{target.name} HP is {target.hp} after gettomg rekted out")
    
    def skill(self, target):
        self.energy -= 20
        print(f"{target.name} HP is {target.hp} before getting rekted out")
        target.hp -= self.atk*2
        print(f"{self.name} menyerang {target.name} sebesar {self.atk*2} dengan keluaran energy sebesar {self.energy}")
        print(f"{target.name} HP is {target.hp} after gettomg rekted out")
    
    def heal(self, healing=100):
        self.hp += healing
        print(f"si {self.name} dapat heal sebesar {healing}")
        print(f"si {self.name} HP sekarang adalah {self.hp}")
        
class Tank(Hero):
    def __init__(self, name="TANK !", hp = 1000 , atk=70,  armor=100, energy=200 ): # constructor
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.energy = energy
        print(f"Tanker {self.name} summoned !")
        
    def defend(self):
        self.armor += 100
        print(f"{self.name} using DEFEND!!!, his armor is {self.armor}")
    
class Assassin(Hero):
    pass

class Support(Hero):
    pass


tanker1=Tank()
tanker1.defend()
Assassin1=Assassin()
Support1 = Support()

        
        
hero1= Hero()
hero2= Hero(name= 'kunka', hp=1000) # menambah atribut sendiri


hero1.attack(target=hero2)
hero1.skill(hero2)

hero2.heal()

#ndaimen@ub.ac.id - tugass

'''
    TUGAS
    MEMBUAT CONTOH CLASSS, YANG MENERAPKAN INHERITANCE , 
    BERIKAN DESKRIPSI PAKAI COMMENT 1 PARAGRAF AJA TENTANG APA YANG KALIAN BIKIN
    format nama  = nim_nama.ipynb

'''