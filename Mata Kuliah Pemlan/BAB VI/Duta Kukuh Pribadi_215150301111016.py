#DUTA KUKUH PRIBADI
#215150301111016

class mobil:
    def __init__(self, name="mobil", rpm=1000, shift=4, cc=1000, torsi=200, maxspeed=120):
        self.name = name
        self.rpm = rpm
        self.shift = shift
        self.cc = cc
        self.torsi = torsi
        self.maxspeed = maxspeed
        
        print(f""" Mobil {self.name} ini memiliki spesifikasi
                RPM         = {self.rpm} 
                Shift       = {self.shift}
                CC          = {self.cc}
                Torsi       = {self.torsi}
                Maxspeed    = {self.maxspeed}
                \n
                """)
    
    def tuneUp(self, blok):
        print(f"\n==============TUNE UP================")
        print(f"Mobil {blok.name} sebelum di tune Up Mempunyai speed {blok.maxspeed} ")
        blok.maxspeed+= (blok.maxspeed - 110)
        print(f"Mobil {blok.name} setelah di tune Up Mempunyai speed {blok.maxspeed}")
        
    def gantiBlok(self, machine):
        print(f"\n==============GANTI BLOK MESIN================")
        print(f"Mobil {machine.name} memiliki CC {machine.cc} dan torsi {machine.torsi} dengan speed {machine.maxspeed}")
        
        choice = input("""Pilih jenis blok mesin
                       1. Diesel
                       2. Bensin
                       """)
        if choice == "1" :
            machine.cc += (machine.cc/2)
            machine.torsi += (machine.torsi * 2)
            machine.maxspeed -= (40)
            print(f"""Jika Mobil {machine.name} diganti menjadi mesin diesel, maka dia memiliki 
                CC    = {machine.cc} 
                torsi = {machine.torsi} 
                speed = {machine.maxspeed}""")
        if choice == "2" :
            machine.cc += (machine.cc/2)
            machine.torsi -= (machine.torsi - 300)
            machine.maxspeed += 100
            print(f"""Jika Mobil {machine.name} diganti menjadi mesin bensin, maka dia memiliki 
                CC    = {machine.cc} 
                torsi = {machine.torsi} 
                speed = {machine.maxspeed}""")
        
    def upperShift(self, gigi):
        print(f"\n==============UPGRADE GIGI================")
        gigi.shift += 1
        print(f"gigi mobil {gigi.name} bertambah menjadi {gigi.shift} ")
    
    def tipeMobil(self, tipe):
        print(f"\n==============JENIS MOBIL================")
        if tipe.torsi >= 600 and tipe.maxspeed < 200:
            print(f"Mobil {tipe.name} adalah jenis mobil Diesel")
    
        if tipe.torsi <= 600 and tipe.maxspeed > 200:
            print(f"Mobil {tipe.name} adalah jenis mobil Bensin")
    
        

Mobil1= mobil(name="Galant", maxspeed=180,shift=5,cc=1800 )
Mobil2= mobil(name="Land Cruiser", torsi=400,shift=5,cc=1800 )

Mobil1.gantiBlok(machine=Mobil1)
Mobil2.gantiBlok(machine=Mobil2)

Mobil2.tuneUp(blok=Mobil2)

Mobil1.upperShift(gigi=Mobil1)

Mobil1.tipeMobil(tipe=Mobil1)
Mobil2.tipeMobil(tipe=Mobil2)
    
    
        
        
        
        