import random
import time

class Spell:
    def __init__(self, name, stat, mana_cost, type):
        self.name = name
        self.stat = stat
        self.mana_cost = mana_cost
        self.type = type

    def show_info(self):
        effect = "daño" if self.stat >= 0 else "Curacion"
        return f"{self.name} ({self.type}) | {effect}: {abs(self.stat)} | Costo Mana: {self.mana_cost}"

class Duelist:
    def __init__(self, name, health, max_health):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.is_defeated = False
    
    def take_damage(self, damage_value):
        self.health -= damage_value
        
        if damage_value < 0:
            self.health = min(self.health, self.max_health)
            print(f"{self.name} se cura {abs(damage_value)} puntos. Vida actual: {self.health}/{self.max_health}.")
            return False

        if self.health <= 0:
            self.health = 0
            self.is_defeated = True
            print(f"--- {self.name} ha sido Derrotado. ---")
            return True
        
        print(f"{self.name} recibe {damage_value} de daño. Vida actual: {self.health}/{self.max_health}.")
        return False

class Student(Duelist):
    def __init__(self, name, health, max_health, level, mana, spells):
        super().__init__(name, health, max_health)
        self.level = level
        self.mana = mana
        self.maxmana = 100 + (level * 10)
        self.spells = [s[0] if isinstance(s, tuple) else s for s in spells]
        self.health = self.max_health

    def level_up(self):
        old_level = self.level
        self.level += 1
        self.max_health += 10
        self.maxmana = 100 + (self.level * 10)
        self.health = self.max_health
        self.mana = self.maxmana
        print(f"============================================")
        print(f"¡{self.name} ha subido de nivel! De Nivel {old_level} a Nivel {self.level}!")
        print(f"Nueva Vida Maxima: {self.max_health}, Nuevo Mana Maximo: {self.maxmana}.")
        print(f"============================================")

    def learn_spell(self, new_spell):
        if isinstance(new_spell, tuple):
            new_spell = new_spell[0]
            
        self.spells.append(new_spell)
        print(f"Hechizo {new_spell.name} fue anadido a la lista de {self.name}.")

    
    def cast_spell(self, target):
        if not self.spells:
            print(f"{self.name} no tiene hechizos para lanzar.")
            return

        print(f"\n--- Hechizos de {self.name} (Mana: {self.mana}/{self.maxmana}) ---")
        
        temp_index = 0
        available_spells = []
        for spell in self.spells:
            temp_index += 1
            if self.mana >= spell.mana_cost:
                available_spells.append(spell)
                print(f"[{temp_index}] {spell.show_info()}")
            else:
                 print(f"[{temp_index}] {spell.show_info()} (Mana insuficiente)")


        if not available_spells:
            print(f"Mana insuficiente para lanzar cualquier hechizo. {self.name} debe recargar.")
            return

        while True:
            try:
                choice = input("Elija el numero del hechizo para lanzar: ")
                choice_index = int(choice) - 1
                
                chosen_spell = self.spells[choice_index] 
                
                if chosen_spell.mana_cost <= self.mana:
                    self.mana -= chosen_spell.mana_cost
                    
                    damage_dealt = int(chosen_spell.stat * self.level)
                    
                    target.take_damage(damage_dealt)
                    print(f"{self.name} lanza {chosen_spell.name} a {target.name}.")
                    break
                else:
                    print("Else: Mana insuficiente para ese hechizo.")
            except:
                print("Else: Entrada no valida o indice de hechizo incorrecto.")
                break

    def recharge_mana(self):
        self.mana = self.maxmana
        print(f"El estudiante {self.name} recargo todo su mana. Mana: {self.mana}/{self.maxmana}.")
    
    def show_state(self):
        status = "Derrotado" if self.is_defeated else "Activo"
        print("=========== STATS ===========")
        print(f"Nombre: {self.name}")
        print(f"Nivel: {self.level} | Estado: {status}")
        print(f"Vida: {self.health}/{self.max_health} | Mana: {self.mana}/{self.maxmana}")
        print("Hechizos Aprendidos:")
        for spell in self.spells:
            print(f" - {spell.show_info()}")
        print("=============================")

class Teacher:
    def __init__(self, name, subject, spells):
        self.name = name
        self.subject = subject
        self.dominated_spells = [s[0] if isinstance(s, tuple) else s for s in spells]
    
    def teach_spell(self, student):
        print(f"\n--- Clase de {self.subject} con el Profesor {self.name} ---")
        print(f"Hechizos disponibles para ensenar:")
        
        temp_index = 0
        for spell in self.dominated_spells:
            temp_index += 1
            print(f"[{temp_index}] {spell.show_info()}")
        
        try:
            o = input("Elija el numero del hechizo para ensenar: ")
            choice_index = int(o) - 1
            
            spell_to_teach = self.dominated_spells[choice_index]
            
            student.learn_spell(spell_to_teach)
            print(f"El profesor {self.name} le enseno el hechizo {spell_to_teach.name} al estudiante {student.name}.")
        except:
            print("Else: Opcion no valida o indice incorrecto.")
            
class Academy:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Estudiante {student.name} matriculado en {self.name}.")

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Profesor {teacher.name} contratado.")

    def select_student(self, prompt):
        print(f"\n--- Seleccionar Estudiante ({prompt}) ---")
        
        temp_index = 0
        for student in self.students:
            temp_index += 1
            status = "Derrotado" if student.is_defeated else "Activo"
            print(f"[{temp_index}] {student.name} (Nivel {student.level}, Estado: {status})")

        try:
            choice = input("Elija el numero del estudiante: ")
            return self.students[int(choice) - 1]
        except:
            print("Else: Seleccion no valida.")
            return None

    def organize_duel(self, student1, student2):
        print(f"\n INICIANDO DUELO: {student1.name} vs {student2.name} ")
        
        student1.health = student1.max_health
        student2.health = student2.max_health
        student1.is_defeated = False
        student2.is_defeated = False
        student1.recharge_mana()
        student2.recharge_mana()
        
        current_duelist = student1
        opponent = student2
        winner = None

        while not student1.is_defeated and not student2.is_defeated:
            time.sleep(0.5)
            print(f"\n--- Turno de {current_duelist.name} (Vida: {current_duelist.health}/{current_duelist.max_health}, Mana: {current_duelist.mana}/{current_duelist.maxmana}) ---")
            
            action = input("Elige accion [Lanzar (L) / Recargar (R)]: ").upper()
            
            if action == 'R':
                current_duelist.recharge_mana()
            elif action == 'L':
                current_duelist.cast_spell(opponent)
            else:
                print("Else: Accion no valida, turno perdido.")
            
            if opponent.is_defeated:
                winner = current_duelist
            
            current_duelist, opponent = opponent, current_duelist
            
        if winner is None:
            if not student1.is_defeated:
                winner = student1
            elif not student2.is_defeated:
                winner = student2
        
        if winner:
            print(f"\n DUELO TERMINADO ¡El ganador es: {winner.name}!")
            winner.level_up()
        else:
            print("\n DUELO TERMINADO. Empate o error.")

Fireball = Spell("FIREBALL", 15, 10, "dmgdealing")
Freeze = Spell("FREEZE", 20, 15, "dmgdealing")
Heal = Spell("HEAL", -12, 8, "healing")

basic_spells_list = [
    Fireball, Freeze, Heal
]

Hurting = Spell("HURTING", 10, 10, "dmgdealing")
Etouch = Spell("EldritchTouch", 18, 20, "healing")

dark_spells_list = [
    Hurting, Etouch
]

student_lyra = Student("Lyra", 50, 50, 1, 100, spells=[Fireball])
student_kane = Student("Kane", 60, 60, 2, 120, spells=[Freeze, Heal])

dark_teacher = Teacher("Uldar", "Dark Magic", dark_spells_list)
light_teacher = Teacher("Elara", "Basic Magic", basic_spells_list)

MagikZkul_academy = Academy("Magik Skul")
MagikZkul_academy.add_student(student_lyra)
MagikZkul_academy.add_student(student_kane)
MagikZkul_academy.assign_teacher(dark_teacher)
MagikZkul_academy.assign_teacher(light_teacher)

def run_tests(academy):
    print("\n========== TEST ==========")

    student_lyra.show_state()

    print("\n--- Simulacion de Clase ---")
    academy.teachers[0].teach_spell(student_lyra) 

    print("\n--- Simulacion de Duelo ---")
    academy.organize_duel(student_lyra, student_kane) 

    print("\n--- Estado despues del Duelo ---")
    student_lyra.show_state()
    student_kane.show_state()

run_tests(MagikZkul_academy)