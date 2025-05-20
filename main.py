# Zadanie 1
# 0! = 1, dlatego return 0; był nieprawidłowy.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Zadanie 2
# "3" złe, używamy liczb (metody spodziewają się inta, nie ma implementacji castowania string na int),
# więc dodałem kod, aby próbowało castować (jeżeli się nie uda to error)
def get_grades():
    return [5, 4, "3", 2, 1]

def calculate_average(grades):
    converted_grades = []

    for grade in grades:
        if isinstance(grade, int):
            converted_grades.append(grade)
        elif isinstance(grade, str):
            try:
                converted_grades.append(int(grade))
            except ValueError:
                raise ValueError(f"Zły typ oceny - Nie można przekonwertować '{grade}' na liczbę!")

    return sum(converted_grades) / len(converted_grades)

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

show_result()

# Zadanie 3

# W take_damage, ponieważ w attack jest np. take_damage(damage), gdzie damage nie jest jasno określony,
# warto się upewnić typu `amount` w take_damage
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Invalid damage type: {type(amount)}. Must be int or float.")

        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = self.strength * 1.5
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    initial_w_hp = w.hp
    initial_m_hp = m.hp
    initial_m_mana = m.mana

    print("Start:", w.hp, m.hp)
    w.attack(m)
    assert m.hp < initial_m_hp, "Po ataku hp powinno się zmniejszyć (lub ew. pozostać niezmieniona)"
    m.attack(w)
    assert w.hp < initial_w_hp, "Po ataku hp powinno się zmniejszyć (lub ew. pozostać niezmieniona)"
    assert m.mana < initial_m_mana, "Po ataku mana powinna się zmniejszyć (lub ew. pozostać niezmieniona)!"
    m.attack(w)
    m.attack(w)
    m.attack(w)

    assert m.mana >= 0, "Mana nie powinna być ujemna!"

    print("End:", w.hp, m.hp)

simulate_battle()