
# Map
#A função map() percorre cada item do iterável e aplica a função especificada.

#sintaxe: map(funcao, iteravel)
#funcao: A função que será aplicada a cada item do iterável.
#iteravel: A sequência (lista, tupla, etc.) onde cada item será transformado pela função.



# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função que dobra um número
def dobrar(num):
    return num * 2

# Usando map() para aplicar a função em cada item da lista
print(list(map(dobrar, numeros)))




# Listas de números
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]

# Função que soma dois números
def somar(x, y):
    return x + y

# Usando map() com dois iteráveis
resultado = map(somar, numeros1, numeros2)

print(list(resultado))  # Saída: [5, 7, 9]

