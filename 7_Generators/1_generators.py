
# Generators

def makeList(num):
    result = []
    for i in range(num): # range é um generator, ele não aloca espaço na memoria quando é processado, diferente de quando criado uma lista direta
        result.append(i*2)
    return result

# print(makeList(100000))


#-----------------------------------------------------------------------------------------------------------------------------------------

#essa é a estrutura basica de um generator, onde se recebe uma variavel 'num' e retorna ele no loop com o i, após isso usar o yeld i
def generatorFunction(num):
    for i in range(num):
        yield i # Usa yield para "produzir" o valor atual de i e pausa a execução
                # Isso faz com que a função retorne um valor e possa ser retomada na próxima chamada de next()


g = generatorFunction(100)
# next(g)
# next(g)
# print(next(g))

# for item in generatorFunction(10000):
#     print(item)

#-----------------------------------------------------------------------------------------------------------------------------------------

 # Essa função simula o comportamento de um loop for usando um iterador manualmente
def specialFor(iterable):
   
    iterator = iter(iterable)  # Converte o iterable em um iterador usando a função iter()

    # Loop infinito que tentará obter o próximo valor do iterador até que ele esteja esgotado
    while True:
        try:
            # Tenta obter o próximo valor do iterador usando a função next()
            next(iterator)
        except StopIteration:
            # Quando StopIteration é levantado, significa que o iterador chegou ao fim
            # O loop é interrompido usando break
            break



class MyGen():
    current = 0 
    # Método inicializador da classe que define o início (first) e o final (last) do intervalo
    def __init__(self, first, last):
        self.first = first  # Armazena o valor inicial do intervalo
        self.last = last    # Armazena o valor final do intervalo

    # Define o método __iter__, que torna o objeto iterável
    def __iter__(self):
        return self  # Retorna a própria instância para ser usada como iterador
    
    # Define o método __next__, que permite obter o próximo valor do iterador
    def __next__(self):
        # Verifica se o valor atual está dentro do intervalo
        if MyGen.current < self.last:
            num = MyGen.current  # Salva o valor atual em uma variável
            MyGen.current += 1   # Incrementa o valor atual para o próximo número
            return num           # Retorna o número salvo (num)
        # Se o valor atual atingir o limite (last), lança StopIteration para terminar a iteração
        raise StopIteration

# Cria uma instância de MyGen com intervalo de 0 a 100
gen = MyGen(0, 100)

# Usa um loop for para iterar sobre o generator
# Cada iteração chama automaticamente __next__ até que StopIteration seja levantado
for i in gen:
    print(i)  # Imprime cada valor gerado no intervalo de 0 a 99



#-----------------------------------------------------------------------------------------------------------------------