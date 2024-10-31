# lambda
#uma função lambda é uma função anônima, ou seja, uma função sem nome. como uma arrow function

#sintaxe: lambda argumentos: expressão


# Função lambda para somar dois números
soma = lambda x, y: x + y

# Chamando a função lambda
print(soma(3, 5))  # Saída: 8


multiple = lambda a, b: a * b

print(multiple(20,10))


numeros = [1, 2, 3, 4, 5]

# Usando lambda com map para elevar ao quadrado cada número
quadrados = map(lambda x: x ** 2, numeros)

print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]


myList = [1,2,3,4,5]

som = list(map(lambda item: item*2, myList))

print(som)



# exercice

lista = [5,4,3]

ex = list(map(lambda item: item**2, lista))

print(ex)


# exercice 2

a = [(0,2), (4,3), (7,3), (10,-1)]

a.sort(key=lambda x: x[1])
print(a)