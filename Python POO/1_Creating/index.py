
# OOP

class PlayerCharacter: #aqui criamos a classe
    membership = True # Class Object Atribute
    def __init__(self, name, age): #aqui criamos o construtor (sempre usar o self para declarar algo)
       if(self.membership): 
        self.name = name    
        self.age = age   #chamamos as definições do construtor


    def shout(self):
        print(f'my name is {self.name}') #f antes da string para poder usar o {} (lembre de sempre usar o self)

player1 = PlayerCharacter('matheus', 18) #instanciação

print(player1.name)
print(player1.membership)