import os

import csv
from tabulate import tabulate

class Character:
    def __init__(self, nama, hit_point, attack_power, defense_power, reaction_speed):
        self.nama = nama
        self.hit_point = hit_point
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.reaction_speed = reaction_speed
        self.recap = []

    def copy(self):
        return Character(self.nama, self.hit_point, self.attack_power, self.defense_power, self.reaction_speed)
    
    def attack(self, enemy):
        damage = self.attack_power - enemy.defense_power
        if damage > 0:
            enemy.hit_point -= damage
            self.recap.append([self.nama, 'attack', enemy.nama, damage])
            enemy.recap.append([enemy.nama, 'defend', self.nama, damage])

    def parry(self, enemy):
        if self.reaction_speed > enemy.reaction_speed:
            return True
        else:
            return False

    def counter_attack(self, enemy):
        self.attack(enemy)
        if enemy.parry(self):
            self.recap.append([self.nama, 'counter attack', enemy.nama])
            enemy.recap.append([enemy.nama, 'parry', self.nama])

def load_data(nama_file):
    characters = []
    try:
        with open(nama_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            print(f"Header: {header}")  # Print the header row
            for row in reader:
                characters.append(Character(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
    except StopIteration:
        print("WAJIB MENAMBAHKAN KARAKTER BARU \n")
    except FileNotFoundError:
        print("The file does not exist.")
    return characters


def save_data(nama_file, characters):
    with open(nama_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if os.path.getsize(nama_file) == 0:
            writer.writerow(["Nama", "Hit Point", "Attack Power", "Defense Power", "Reaction Speed"])
        for character in characters:
            writer.writerow([character.nama, character.hit_point, character.attack_power, character.defense_power, character.reaction_speed])

def save_recap(nama_file, recaps):
    with open(nama_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for recap in recaps:
            writer.writerow(recap)

def display_recap(recaps):
    for i, recap in enumerate(recaps):
        print(f"Recap Pertandingan {i+1}:")
        print(tabulate(recap, headers=["Character", "Action", "Enemy", "Damage"]))

def main():
    characters = []
    while True:
        print("1. Buat Karakter Baru")
        print("2. Hapus Karakter")
        print("3. Tampilkan Daftar Karakter")
        print("4. Mulai Pertandingan")
        print("5. Rekap Pertandingan")
        print("6. Keluar")
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
            characters = load_data('characters.csv')  # Load data here
            for character in characters:
                print(f"Nama: {character.nama}, HP: {character.hit_point}, Attack Power: {character.attack_power}, Defense Power: {character.defense_power}, Reaction Speed: {character.reaction_speed}")
                
        elif pilihan == "4":
            nama1 = input("Masukkan nama karakter pertama: ")
            nama2 = input("Masukkan nama karakter kedua: ")
            char1 = None
            char2 = None
            for character in characters:
                if character.nama == nama1:
                    char1 = character.copy()
                elif character.nama == nama2:
                    char2 = character.copy()
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
                    
        elif pilihan == "5":
            save_recap('recap.csv', [char.recap for char in characters])
            display_recap([char.recap for char in characters])
               
        elif pilihan == "6":
            break

if __name__ == "__main__":
    main()
