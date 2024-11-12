from abc import ABC, abstractmethod


class Room(ABC):  # 1. Создание абстрактного класса Room
    def __init__(self, features, price):
        self._features = features      # список удобств номера (с одним подчеркиванием)
        self.__price = price           # цена номера (с двумя подчеркиваниями)

    @abstractmethod
    def get_price(self):
        """Возвращает цену номера. Должен быть реализован в подклассе."""
        pass

    @abstractmethod
    def get_features(self):
        """Возвращает список удобств номера. Должен быть реализован в подклассе."""
        pass


# 3. Создание классов дополнительных услуг WiFiService и BreakfastService
class WiFiService:
    def get_wifi_description(self):
        return "Высокоскоростной Wi-Fi доступен во всех зонах отеля."


class BreakfastService:
    def get_breakfast_description(self):
        return "Завтрак включен в стоимость проживания и подается с 7 до 10 утра."


# 2. Создание классов для номеров: StandardRoom, LuxuryRoom, и FamilyRoom
class StandardRoom(Room):
    def get_price(self):
        return self._Room__price  # Обращаемся к приватному атрибуту __price через имя класса

    def get_features(self):
        return self._features


class LuxuryRoom(Room, WiFiService, BreakfastService):
    def get_price(self):
        return self._Room__price  # Обращаемся к приватному атрибуту __price через имя класса

    def get_features(self):
        # Основные удобства номера
        features = self._features
        # Добавление описаний дополнительных услуг
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features


class FamilyRoom(Room, WiFiService):
    def get_price(self):
        return self._Room__price  # Обращаемся к приватному атрибуту __price через имя класса

    def get_features(self):
        # Основные удобства номера
        features = self._features
        # Добавление описания услуги Wi-Fi
        features.append(self.get_wifi_description())
        return features


# 4.3 Создание экземпляров для каждого типа номера
standard_room = StandardRoom(["Телевизор", "Мини-бар"], 100)
luxury_room = LuxuryRoom(["Телевизор", "Мини-бар"], 200)
family_room = FamilyRoom(["Телевизор", "Мини-бар", "Детская кроватка"], 150)

# Вывод информации о номерах
print("Standard Room:")
print("Price:", standard_room.get_price())
print("Features:", standard_room.get_features())

print("\nLuxury Room:")
print("Price:", luxury_room.get_price())
print("Features:", luxury_room.get_features())

print("\nFamily Room:")
print("Price:", family_room.get_price())
print("Features:", family_room.get_features())
