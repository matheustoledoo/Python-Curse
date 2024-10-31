

class PlayerCharacter: #aqui criamos a classe
    membership = True # Class Object Atribute
    def __init__(self, name, age): #aqui criamos o construtor (sempre usar o self para declarar algo)
       if(self.membership): 
        self.name = name    
        self.age = age   #chamamos as definições do construtor


    def shout(self):
        print(f'my name is {self.name}') #f antes da string para poder usar o {} (lembre de sempre usar o self)

    @classmethod #o @classmethod serve para que a função abaixo possa ser utilizada sem ter que instanciar
    def addingThings(cls, num1, num2): #cls é o self do @classmethod
       return num1 + num2
    
    @staticmethod #o @staticmethod é a mesma coisa que o @classmethod so que nao precisa utilizar o cls
    def addingThings(num1, num2): #cls é o self do @classmethod
       return num1 + num2



player1 = PlayerCharacter('matheus', 18) #instanciação

print(player1.addingThings(1, 2))
