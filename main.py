class Avengers:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def __str__(self):
        return f'{self.name} is {self.age} years old, is {self.gender}, has {self.super_power} as superpower, and uses {self.weapon} as a weapon'



captain_america = Avengers('Captain America',23,'Male','Super Strength', 'Shield')

iron_man = Avengers('Iron Man',23,'Male','Technology', 'Iron-Man Suite')

black_widow = Avengers('Black Widow',23,'Female','Superhuman', 'Fighting-Skills')

thor = Avengers('Thor',23,'Male','Super Energy', 'Mjolnir')

hawk_eye = Avengers('Hawk Eye',23,'Male','Fighting Skills', 'Bow and Arrow')

print(hawk_eye)




