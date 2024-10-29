
# Encapsulation 

#encapsulamento de dados

class PlayerCharacter: 
    membership = True
    def __init__(self, name, age): 
       if(self.membership): 
        self.name = name    
        self.age = age  

    def speake(self):
       print(f'my name is {self.name}')



player1 = PlayerCharacter('matheus', 18) 

print(player1.name)
