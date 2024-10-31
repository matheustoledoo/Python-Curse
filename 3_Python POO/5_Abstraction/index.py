
# Encapsulation

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is{self.name}')


player1 = PlayerCharacter('andrei', 19)

player1.speak()
player1.name = '!!!'
player1.speak = 'boo'