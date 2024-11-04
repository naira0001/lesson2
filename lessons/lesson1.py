# OOP - Объектно-ориентированное программирование

# types_python = 1, 'str', 1.2, True, {}, [], ()
#
# print(type('str'))

# def a(b):
#     print(b)
#
# a(123)

# CamelCase - snike_case

class Car:


    def drive(self):
        print('Машина едет', self.model)

    def __init__(self, model, volume, age):
        self.model = model
        self.volume = volume
        self.age = age

    def start(self):
        print("Машина завелась в", self.age)



# Экземпляр
audi = Car(model="A8", age="2000", volume="2.8")
mazda = Car(model="RX-8", volume="3.0", age="2001")

audi.drive()
mazda.drive()

print(mazda)
a=