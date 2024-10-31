

# Exercício 1: Encapsulamento com Variáveis Privadas
# Explicação
# Neste exercício, você criará uma classe Banco com atributos privados. A classe deve permitir que um cliente consulte e deposite dinheiro em sua conta, mas o saldo não pode ser alterado diretamente de fora da classe.

# Crie uma classe Banco com um atributo privado _saldo.
# Implemente um método depositar(valor) que permita depositar um valor na conta.
# Crie um método consultar_saldo() que retorne o saldo atual.

class Banco:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  # Atributo privado para o saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado.")
        else:
            print("Valor de depósito inválido.")

    def consultar_saldo(self):
        return f"Saldo atual: {self._saldo}"

# Exemplo de uso
conta = Banco(100)  # Saldo inicial de 100
print(conta.consultar_saldo())  # Saída: Saldo atual: 100
conta.depositar(50)  # Depósito de 50
print(conta.consultar_saldo())  # Saída: Saldo atual: 150


# Exercício 2: Herança e Polimorfismo
# Explicação
# Este exercício envolve uma classe Veiculo base com um método descrever(). Você criará subclasses Carro e Moto, cada uma com sua implementação de descrever(), demonstrando o polimorfismo.

# Crie uma classe Veiculo com um método descrever().
# Crie duas subclasses Carro e Moto, ambas herdam de Veiculo e implementam o método descrever() de maneira única.
# Escreva uma função mostrar_veiculo() que aceite qualquer objeto Veiculo e chame descrever().

class Veiculo:
    def descrever(self):
        pass  # Método a ser implementado pelas subclasses

class Carro(Veiculo):
    def descrever(self):
        return "Este é um carro. Tem quatro rodas e é ideal para estradas."

class Moto(Veiculo):
    def descrever(self):
        return "Esta é uma moto. Tem duas rodas e é ágil no trânsito."

def mostrar_veiculo(veiculo):
    print(veiculo.descrever())

# Exemplo de uso
carro = Carro()
moto = Moto()

mostrar_veiculo(carro)  # Saída: Este é um carro. Tem quatro rodas e é ideal para estradas.
mostrar_veiculo(moto)   # Saída: Esta é uma moto. Tem duas rodas e é ágil no trânsito.


# Exercício 3: Herança Múltipla
# Explicação
# Neste exercício, você criará uma classe DispositivoMovel e DispositivoConectavel, e uma classe Smartphone que herda de ambas.

# Crie uma classe DispositivoMovel com o método ligar().
# Crie uma classe DispositivoConectavel com o método conectar().
# Crie uma classe Smartphone que herda de ambas e possui um método status().
# O método status() do Smartphone deve chamar ligar() e conectar().

class DispositivoMovel:
    def ligar(self):
        return "Dispositivo móvel ligado."

class DispositivoConectavel:
    def conectar(self):
        return "Dispositivo conectado à internet."

class Smartphone(DispositivoMovel, DispositivoConectavel):
    def status(self):
        return f"{self.ligar()} {self.conectar()}"


# Exemplo de uso
smartphone = Smartphone()
print(smartphone.status())  # Saída: Dispositivo móvel ligado. Dispositivo conectado à internet.


# Exercício 4: Herança e Encapsulamento com Variáveis Privadas
# Explicação
# Você criará uma classe Funcionario com atributos privados e uma subclasse Gerente que possui acesso a esses atributos através de métodos da classe base.

# Crie a classe Funcionario com atributos privados _nome e _salario.
# Adicione métodos públicos para definir e consultar o salário.
# Crie uma classe Gerente que herda de Funcionario e tem um método relatorio(), que exibe o nome e o salário.

class Funcionario():
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def defSalario(self, encremento):
        self._salario += encremento

    def consultSalario(self):
        return f'{self._salario}'
    
class Gerente(Funcionario):
    def relatorio(self):
        return f'nome: {self._nome}, salario: {self._salario}'
    
# Exemplo de uso
funcionario = Funcionario("Carlos", 3000)
gerente = Gerente("Alice", 5000)

print(gerente.relatorio())  # Saída: Gerente: Alice, Salário: 5000
gerente.defSalario(5500)
print(gerente.relatorio())  # Saída: Gerente: Alice, Salário: 5500


# Exercício 5: Polimorfismo com Herança Múltipla e Sobrescrita de Métodos
# Explicação
# Crie uma classe base InstrumentoMusical com o método tocar(), depois classes Guitarra e Bateria que implementam tocar(). Em seguida, crie uma classe Banda que aceita qualquer instrumento e chama seu método tocar(), demonstrando polimorfismo.

# Crie a classe base InstrumentoMusical com o método tocar().
# Implemente Guitarra e Bateria que sobrescrevem tocar() com sua própria versão.
# Crie a classe Banda que aceita diferentes InstrumentoMusical e chama tocar().

class InstrumentoMusical():
    def tocar(self):
        pass

class Guitarra(InstrumentoMusical):
    def tocar(self):
        return 'tocando guitarra'
    
class Bateria(InstrumentoMusical):
    def tocar(self):
        return 'tocando bateria'
    
class Banda:
    def __init__(self):
        self.instrumentos = []

    def adicionar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def apresentar(self):
        for instrumento in self.instrumentos:
            print(instrumento.tocar())

# Exemplo de uso
guitarra = Guitarra()
bateria = Bateria()

banda = Banda()
banda.adicionar_instrumento(guitarra)
banda.adicionar_instrumento(bateria)

banda.apresentar()