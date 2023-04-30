# class A:
#     def method_A(self):
#         print("ini adalah method A")
        
# class B:
#     def method_B(self):
#         print("ini adalah method B")
        
# class C(A,B):
#     pass


# objek = C()

# objek.method_A()
# objek.method_B()

class Team:
    def setTeam(self,team):
        self.team = team
    
    def showTeam(self):
        print(self.team)
        
class Tipe_Hero:
    def setTipe(self,tipe):
        self.tipe = tipe
        
    def showTipe(self):
        print(self.tipe)

class Hero(Team,Tipe_Hero):
    def __init__(self,name, health) -> None:
        self.name = name
        self.health = health
        
Ucup = Hero('ucup', 100)
Ucup.setTeam("merah")        
Ucup.setTipe("Cundang")

Ucup.showTeam()
Ucup.showTipe()