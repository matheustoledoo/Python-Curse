
# Reduce
#A função reduce() em Python é usada para aplicar uma função cumulativa a uma sequência de elementos, reduzindo a sequência a um único valor

#sintaxe:
#from functools import reduce
#reduce(funcao, iteravel, valor_inicial)

#funcao: Uma função que recebe dois argumentos e retorna um único valor. A função é chamada repetidamente, acumulando o resultado.
#iteravel: Um iterável (como uma lista ou tupla) cujos elementos serão reduzidos a um único valor.
#valor_inicial (opcional): Um valor inicial para começar a acumulação. Se não for fornecido, reduce() começa com o primeiro elemento do iterável.



from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função que soma dois números
def somar(x, y):
    return x + y

# Usando reduce() para somar os elementos da lista
resultado = reduce(somar, numeros)

print(resultado)  # Saída: 15




# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função que soma dois números
def somar(x, y):
    return x + y

# Usando reduce() com um valor inicial de 10
resultado = reduce(somar, numeros, 10)

print(resultado)  # Saída: 25 (10 + 1 + 2 + 3 + 4 + 5)
