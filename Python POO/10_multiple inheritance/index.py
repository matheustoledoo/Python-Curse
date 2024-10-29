# Classe base Mamifero
class Mamifero:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        return f"{self.nome} está andando."


# Classe base Aquatico
class Aquatico:
    def __init__(self, nome):
        self.nome = nome

    def nadar(self):
        return f"{self.nome} está nadando."


# Classe Golfinho que herda de Mamifero e Aquatico
class Golfinho(Mamifero, Aquatico):
    def __init__(self, nome):
        # Chamamos o construtor de ambas as classes base
        Mamifero.__init__(self, nome)
        Aquatico.__init__(self, nome)

    # Método exclusivo de Golfinho
    def emitir_som(self):
        return f"{self.nome} faz um som de golfinho."

# Exemplo de uso
golfinho = Golfinho("Flipper")

# Acessando métodos das classes base
print(golfinho.andar())       # Saída: Flipper está andando.
print(golfinho.nadar())       # Saída: Flipper está nadando.
print(golfinho.emitir_som())  # Saída: Flipper faz um som de golfinho.
