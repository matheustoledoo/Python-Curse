# Classe base, ou "classe pai", Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass  # Não faz nada aqui, mas serve como uma "promessa" de que cada animal "sabe falar"



# Classe Cachorro que herda de Animal
class Cachorro(Animal):
    # Implementação específica de como um cachorro "fala"
    def falar(self):
        return f"{self.nome} diz: Au Au!"  # O cachorro late



# Classe Gato que herda de Animal
class Gato(Animal):
    # Implementação específica de como um gato "fala"
    def falar(self):
        return f"{self.nome} diz: Miau!"  # O gato mia



# Função que aceita qualquer tipo de animal
def ouvir_animal(animal):
    print(animal.falar())  # Chama o método falar() do objeto animal



# Exemplo de uso:
cachorro = Cachorro("Rex")  # Criamos um cachorro chamado Rex
gato = Gato("Mimi")         # Criamos um gato chamado Mimi



# Vamos ouvir os animais "falando"
ouvir_animal(cachorro)  # Saída: Rex diz: Au Au!
ouvir_animal(gato)      # Saída: Mimi diz: Miau!
