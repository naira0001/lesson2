from main import Hero

class Warrior(Hero):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength  # Новый атрибут силы
        self.energy = 100  # Новый атрибут энергии, которая уменьшается при использовании способности

    def battle_scream(self):
        if self.energy >= 10:  # Проверка наличия достаточной энергии
            self.strength += 20
            self.energy -= 10  # Уменьшаем энергию
            return f"{self.name} использует боевой крик, увеличивая силу на 20! " \
                   f"Текущая сила: {self.strength}, энергия: {self.energy}."
        else:
            return f"{self.name} недостаточно энергии для боевого крика!"

    def action(self):
        # Сначала вызываем базовый метод action
        base_action = super().action()
        # Затем вызываем уникальный метод battle_scream
        unique_action = self.battle_scream()
        return base_action + unique_action

# Пример использования

warrior = Warrior("Конан", health=100, strength=100)
print(warrior.introduce())       # Вызов метода из класса Hero
print(warrior.action())          # Вызов нового метода action
print(warrior.rest())            # Вызов метода отдыха из класса Hero

