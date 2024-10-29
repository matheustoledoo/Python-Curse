
# Inheritance (herança)

class Pessoa: # classe pai
    # Variável pública
    nome_publico = "Nome público padrão"
    
    def __init__(self, nome, idade):
        # Variável pública
        self.nome = nome
        
        # Variável protegida (apenas convenção)
        self._idade = idade

    # Método público para acessar o valor da variável protegida _idade
    def mostrar_idade(self):
        return f"A idade é {self._idade}"
    


# Classe Estudante que herda da classe Pessoa
class Estudante(Pessoa): 
    def __init__(self, nome, idade, curso):
        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome, idade)
        
        # Variável pública específica da classe Estudante
        self.curso = curso
        
        # Variável protegida específica da classe Estudante
        self._media = None
    
    # Método para acessar a idade (variável protegida) da classe pai
    def detalhes_estudante(self):
        return f"Estudante: {self.nome}, Idade: {self._idade}, Curso: {self.curso}"



# Exemplo de uso
estudante = Estudante("Maria", 22, "Engenharia")

# Acessando variáveis públicas
print(estudante.nome)  # Saída: Maria
print(estudante.curso)  # Saída: Engenharia

# Acessando variáveis protegidas da classe pai
print(estudante._idade)  # Funciona, mas não recomendado

# Acessando método que exibe variáveis protegidas
print(estudante.detalhes_estudante())  # Saída: Estudante: Maria, Idade: 22, Curso: Engenharia


# Outro exemplo

class User():
   def signIn(self):
       print('logged')

class Wizard(User):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def atack():
        print('atack')

class Archer(User):
      def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

      def atack():
        print('atack')


wizard1 = Wizard('patolino', 'fire')
print(isinstance(wizard1, Wizard)) # para ver se um é instancia