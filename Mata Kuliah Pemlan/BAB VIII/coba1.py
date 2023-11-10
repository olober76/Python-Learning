import csv

class Character:
    def __init__(self, nama, hit_point, attack_power, defense_power, reaction_speed):
        self.nama = nama
        self.hit_point = hit_point
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.reaction_speed = reaction_speed

    def attack(self, enemy):
        damage = self.attack_power - enemy.defense_power
        if damage > 0:
            enemy.hit_point -= damage

    def parry(self, enemy):
        if self.reaction_speed > enemy.reaction_speed:
            return True
        else:
            return False

    def counter_attack(self, enemy):
        self.attack(enemy)

def load_data(nama_file):
    with open(nama_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        characters = []
        for row in reader:
            characters.append(Character(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
        return characters


def save_data(nama_file, characters):
    with open(nama_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for character in characters:
            writer.writerow([character.nama, character.hit_point, character.attack_power, character.defense_power, character.reaction_speed])

def main():
    characters = load_data('characters.csv')
    while True:
        print("1. Buat Karakter Baru")
        print("2. Hapus Karakter")
        print("3. Tampilkan Daftar Karakter")
        print("4. Mulai Pertandingan")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama karakter: ")
            hit_point = int(input("Masukkan hit point: "))
            attack_power = int(input("Masukkan attack power: "))
            defense_power = int(input("Masukkan defense power: "))
            reaction_speed = int(input("Masukkan reaction speed: "))
            new_character = Character(nama, hit_point, attack_power, defense_power, reaction_speed)
            characters.append(new_character)
            save_data('characters.csv', characters)
            
        elif pilihan == "2":
            nama = input("Masukkan nama karakter yang ingin dihapus: ")
            for character in characters:
                if character.nama == nama:
                    characters.remove(character)
                    save_data('characters.csv', characters)
                    break
                    
        elif pilihan == "3":
            for character in characters:
                print(f"Nama: {character.nama}, HP: {character.hit_point}, Attack Power: {character.attack_power}, Defense Power: {character.defense_power}, Reaction Speed: {character.reaction_speed}")
                
        elif pilihan == "4":
            nama1 = input("Masukkan nama karakter pertama: ")
            nama2 = input("Masukkan nama karakter kedua: ")
            char1 = None
            char2 = None
            for character in characters:
                if character.nama == nama1:
                    char1 = character
                elif character.nama == nama2:
                    char2 = character
            if char1 and char2:
                while char1.hit_point > 0 and char2.hit_point > 0:
                    char1.attack(char2)
                    if char2.parry(char1):
                        char2.counter_attack(char1)
                    print(f"{char1.nama} HP: {char1.hit_point}")
                    print(f"{char2.nama} HP: {char2.hit_point}")
                if char1.hit_point <= 0:
                    print(f"{char2.nama} menang!")
                else:
                    print(f"{char1.nama} menang!")
                save_data('characters.csv', characters)
                
        elif pilihan == "5":
            break

if __name__ == "__main__":
    main()