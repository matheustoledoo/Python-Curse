
# Public and Private

#Em Python, variáveis privadas são indicadas com o prefixo _ (uma barra) para indicar "protegido" ou com __ (duas barras) para indicar "privado"
#(ou seja, para uso apenas dentro da classe).

class Pessoa:
    #Variável pública
    nome_publico = "Nome público padrão"
    
    def __init__(self, nome, idade):
        #Variável pública
        self.nome = nome
        
        #Variável privada (proteção por convenção)
        self._idade = idade
        
        #Variável realmente privada (nome mangling)
        self.__segredo = "Informação secreta"

    #Método público para acessar o valor da variável privada _idade
    def mostrar_idade(self):
        return f"A idade é {self._idade}"
    
    #Método público para acessar a variável privada __segredo
    def mostrar_segredo(self):
        return f"Segredo: {self.__segredo}"


#Exemplo de uso
pessoa = Pessoa("João", 30)

#Acessando variáveis públicas
print(pessoa.nome)  #Saída: João
print(pessoa.nome_publico)  #Saída: Nome público padrão

#Acessando a variável privada com um método público
print(pessoa.mostrar_idade())  #Saída: A idade é 30

#Tentando acessar diretamente uma variável privada
print(pessoa._idade)  #Funciona, mas não é recomendado

#Tentando acessar diretamente uma variável privada com nome mangling
try:
    print(pessoa.__segredo)  #Erro! Acesso direto à variável realmente privada não permitido
except AttributeError as e:
    print(e)  #Saída: 'Pessoa' object has no attribute '__segredo'

#Acessando a variável privada com método público
print(pessoa.mostrar_segredo())  #Saída: Segredo: Informação secreta