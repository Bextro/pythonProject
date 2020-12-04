class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speed = 1.5

    def change_speed(self, new_speed):
        self.speed = new_speed

    def bark(self):
        print("bark bark!")

    def run(self, place):
        print(self.name, 'runs with speed ', self.speed, 'in', place)

    def bite(self, victim_name):
        print(self.name, 'bites', victim_name)

    # print all attributes of a dog

    def att(self):
        print(self.name,'are',self.age,'years old and it can run up to',self.speed,'km/h')

reks = Dog('Reks', 2)
reks.att()
