import random
import time

# CLAN WARS

class Warrior:
    def __init__(self, name, health, damage, defense, type):
        self.name = name
        self.max_health = health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.type = type

    def attack(self, enemy):
        dmg_dealt = max(1, self.damage - enemy.defense) 
        return dmg_dealt

    def receive_damage(self, damage_value):
        self.health -= damage_value
        if self.health < 0:
            self.health = 0
        return self.health

    def heal(self):
        heal_amount = self.max_health * 0.30
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} ({self.type}) se ha curado {round(heal_amount)} puntos. Vida actual: {round(self.health)}/{self.max_health}")

    def show_state(self):
        status = "Vivo" if self.health > 0 else "Muerto"
        print("--- STATS ---")
        print(f"Nombre: {self.name}")
        print(f"Tipo: {self.type}")
        print(f"Vida: {round(self.health)}/{self.max_health} ({status})")
        print(f"Ataque: {self.damage}")
        print(f"Defensa: {self.defense}")
        print("-----------------------")

class Clan:
    def __init__(self, name, warrior_list, strategy):
        self.name = name
        self.warrior_list = warrior_list 
        self.strategy = strategy
    
    def add_warrior(self, warrior):
        self.warrior_list.append(warrior)
    
    def select_warrior(self, warrior_name):
        for warrior in self.warrior_list:
            if warrior.name.lower() == warrior_name.lower():
                warrior.show_state()
                return warrior
        print(f"Guerrero '{warrior_name}' no encontrado en {self.name}.")
        return None

    def get_available_warriors(self):
        return [w for w in self.warrior_list if w.health > 0]

    def select_random_warrior(self):
        available_warriors = self.get_available_warriors()
        if available_warriors:
            return random.choice(available_warriors)
        return None

    def is_alive(self):
        return len(self.get_available_warriors()) > 0
    
    def attack_clan(self, enemy_clan, battle_controller):
        print(f"{self.name} inicia el asalto contra {enemy_clan.name}!")
        battle_controller.start(self, enemy_clan)

    def show_status(self):
        alive_count = len(self.get_available_warriors())
        total_count = len(self.warrior_list)
        print(f"========================================")
        print(f"Clan: {self.name}")
        print(f"Estrategia: {self.strategy}")
        print(f"Guerreros disponibles: {alive_count} / {total_count}")
        print(f"----------------------------------------")
        for warrior in self.warrior_list:
             status = "Vivo" if warrior.health > 0 else "Derrotado"
             print(f" - {warrior.name} ({warrior.type}): {round(warrior.health)}/{warrior.max_health} ({status})")
        print(f"========================================")

class Battle:
    def __init__(self):
        self.turn = 0
        self.clan1 = None
        self.clan2 = None

    def start(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2
        self.turn = 0

        while self.clan1.is_alive() and self.clan2.is_alive():
            self.turn += 1
            print(f"\n--- TURNO {self.turn} ---")
            self.battle_turn(self.clan1, self.clan2)
            if not self.clan2.is_alive():
                break

            self.battle_turn(self.clan2, self.clan1)
            time.sleep(1) 
        
        self.verify_winner()

    def battle_turn(self, attacking_clan, defending_clan):
        attacker = attacking_clan.select_random_warrior()
        defender = defending_clan.select_random_warrior()

        if not attacker or not defender:
            return 

        damage = attacker.attack(defender)
        defender.receive_damage(damage)

        print(f"{attacker.name} ({attacking_clan.name}) ataca a {defender.name} ({defending_clan.name})! Daño: {damage}")
        
        if random.random() < 0.20:
            attacker.heal()

        if defender.health <= 0:
            print(f"{defender.name} ha sido derrotado!")
        else:
            print(f" Vida restante de {defender.name}: {round(defender.health)}")


    def verify_winner(self):
        print("\n========================================")
        if not self.clan1.is_alive() and not self.clan2.is_alive():
            print("DRAW! Ambos clanes han sido derrotados!")
        elif not self.clan2.is_alive():
            print(f"¡{self.clan1.name} ha ganado la guerra!")
        elif not self.clan1.is_alive():
            print(f"¡{self.clan2.name} ha ganado la guerra!")
        else:
            print("Batalla terminada por error o empate.")
        print("========================================")

#OBJECTS

battle = Battle()

BlueWarrior = Warrior("Urg", 70, 30, 10, "Guerrero")
BlueMage = Warrior("Za'war", 50, 60, 5, "Mago")
BlueTank = Warrior("Vazlo", 100, 10, 20, "Tanque")
BlueArcher = Warrior("Niak", 60, 30, 8, "Arquero")

BlueWarriors = [BlueWarrior, BlueMage, BlueTank, BlueArcher]

RedWarrior = Warrior("Gru", 70, 30, 10, "Guerrero")
RedMage = Warrior("Raw'az", 50, 60, 5, "Mago")
RedTank = Warrior("Olzav", 00, 10, 20, "Tanque")
RedArcher = Warrior("Kain", 60, 30, 8, "Arquero")

RedWarriors = [RedWarrior, RedMage, RedTank, RedArcher]

blueclan = Clan("Clan Azul", BlueWarriors, "Siege")
redclan = Clan("Clan Rojo", RedWarriors, "Assault")

#GAME

print("--- SELECCIÓN DE CLAN ---")
MainClan = None
EnemyClan = None

while MainClan is None:
    choose = input("Elige tu estrategia: \n[ASSAULT] (Jugar como Clan Rojo)\n[SIEGE] (Jugar como Clan Azul)\n\nElección: ").lower()
        
    if choose == "siege":
        MainClan = blueclan
        EnemyClan = redclan
        break
    elif choose == "assault":
        MainClan = redclan
        EnemyClan = blueclan
        break
    else:
        print("Opción no válida. Por favor, elige 'ASSAULT' o 'SIEGE'.")

print(f"\nHas elegido: {MainClan.name} con la estrategia de {MainClan.strategy}.")

def game(MainClan, EnemyClan):
    while MainClan.is_alive() and EnemyClan.is_alive():
        print("\n---------------- CLAN WARS MENU ----------------")
        print(f"Clan Activo: {MainClan.name}")
        print("1. Ver STATUS de tu Clan.")
        print("2. Ver GUERREROS de tu Clan.")
        print("3. Ver STATUS del Clan enemigo.")
        print("4. Atacar CLAN ENEMIGO.")
        print("5. Salir.")
        print("------------------------------------------------")
        
        option = input("Elija una acción: ")
        if option == '1':
            MainClan.show_status()
        elif option == '2':
            print(f"\n--- Guerreros de {MainClan.name} ---")
            for w in MainClan.warrior_list:
                w.show_state()
        elif option == '3':
            EnemyClan.show_status()
        elif option == '4':
            MainClan.attack_clan(EnemyClan, battle)
            return 
        elif option == '5':
            print("Juego terminado.")
            return
        else:
            print("Opción no válida.")

game(MainClan, EnemyClan)