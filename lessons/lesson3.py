# Инкапсуляция

# Когда имя атрибута или метода начинается с одного подчеркивания (например, _balance),
# это обозначает, что он защищен
# или может начитаться с двух подчеркиваний (__balance), что обозначает, что он приват


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Защищенный атрибут
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Баланс {self.owner} пополнен на {amount}. Текущий баланс: {self._balance}"
        return "Сумма должна быть положительной."

    def get_balance(self):
        return f"Баланс: {self._balance}"

# Использование защищенного атрибута
account = BankAccount("Иван", 1000)
print(account.get_balance())    # Баланс: 1000
print(account._balance)      # Мы можем получить доступ к _balance, но это не рекомендуется.
# Прямой доступ к __balance вызовет ошибку, так как он скрыт
print(account.__balance)      # Ошибка AttributeError: 'BankAccount' object has no attribute '__balance'
# Доступ к приватному атрибуту через преобразованное имя
print(account._BankAccount__balance)  # 1000

# Подсказка: Просмотр всех атрибутов и методов объекта
print(dir(account))


# Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
# реализации. Это можно сделать, создавая абстрактные классы, которые определяют
# интерфейс (методы) для классов-наследников. В Python абстрактные классы обычно
# создаются с помощью модуля abc.

from abc import ABC, abstractmethod

class Animal(ABC):  # Абстрактный класс
    @abstractmethod
    def make_sound(self):
        pass  # Определяет интерфейс для звука

    @abstractmethod
    def move(self):
        pass  # Определяет интерфейс для движения

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

    def move(self):
        return "Собака бегает на четырех лапах."

class Bird(Animal):
    def make_sound(self):
        return "Чирик-чирик!"

    def move(self):
        return "Птица летит."

# Пример использования абстракции
dog = Dog()
bird = Bird()

print(dog.make_sound())  # Гав-гав!
print(dog.move())        # Собака бегает на четырех лапах.
print(bird.make_sound()) # Чирик-чирик!
print(bird.move())       # Птица летит.


# Множественное наследование

# Множественное наследование позволяет классу наследовать поведение и свойства сразу от нескольких классов.
# Однако это может привести к путанице, особенно если в классах есть методы с одинаковыми именами.
# Python решает такие проблемы с помощью механизма порядка разрешения методов (Method Resolution Order, MRO),
# который определяет, какой метод или атрибут будет вызван в случае конфликтов.


class Animal:
    def make_sound(self):
        return "Издает звук"

class Flyable:
    def move(self):
        return "Летит"

class Swimmable:
    def move(self):
        return "Плавает"

class Duck(Animal, Flyable, Swimmable):  # Множественное наследование
    def make_sound(self):
        return "Кря-кря!"

# Пример использования множественного наследования
duck = Duck()
print(duck.make_sound())  # Кря-кря!
print(duck.move())

# Для просмотра порядка разрешения методов можно использовать атрибут __mro__ или функцию mro().
# Порядок разрешения методов (MRO)
print(Duck.__mro__)  # Массив классов в порядке их проверки для поиска методов