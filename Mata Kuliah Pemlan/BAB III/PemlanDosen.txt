import random

mylist = [None] * 100
counter = 0
while counter < 100: #isi list dan namnaya
    if counter < 10:
        mylist[counter] = f"BKB{counter + 1}"
    elif counter >= 10 and counter < 20:
        mylist[counter] = f"Armlet{counter + 1}"
    elif counter >= 20 and counter < 30:
        mylist[counter] = f"Skadi{counter + 1}"
    elif counter >= 30 and counter < 40:
        mylist[counter] = f"urn{counter + 1}"
    elif counter >= 40 and counter < 50:
        mylist[counter] = f"Crimson{counter + 1}"
    elif counter >= 50 and counter < 60:
        if counter == 56:
            mylist[55] = "SILVER EDGE*"
            gachaSSS1 = mylist[55]
        mylist[counter] = f"shadow{counter + 1}"
    elif counter >= 60 and counter < 70:
        if counter == 69:
            mylist[68] = "BLACK KING BAR*"
            gachaSSS2 = mylist[68]
        mylist[counter] = f"hood{counter + 1}"
    elif counter >= 70 and counter < 80:
        mylist[counter] = f"tarrasque{counter + 1}"
    elif counter >= 80 and counter < 90:
        mylist[counter] = f"ethereal{counter + 1}"
    elif counter >= 90 and counter < 100:
        mylist[counter] = f"dagger{counter + 1}"
            
    counter += 1

print(f"{mylist} \n\n {10 * '======='}")

def gacha():
    pity = 0
    
    while True:
            
        nilai_random = random.randint(0,99)
        if mylist[nilai_random] == gachaSSS1 or mylist[nilai_random] == gachaSSS2:
            print(f"\n {10 * '======='}\n SELAMAT KAMU MENDAPATKAN ITEM RARE || {mylist[nilai_random]} || DENGAN PITY {pity}\n {10 * '======='}")
            break
        else:
            print(f"\n selamat cuman dapat {mylist[nilai_random]}")
        pity += 1
        
gacha()
    
