import numpy as np

arr = np.array([1, 2, 3], dtype='float32')  # Array de floats
print(arr)
print(arr.dtype)  # Verifica que agora é float


# Alterando a Forma do Array (reshape)
# Transformar um array 1D (linha única) em uma matriz 2D (tabela):
arr = np.array([1, 2, 3, 4, 5, 6])
matriz = arr.reshape((2, 3))  # 2 linhas e 3 colunas
print(matriz)


#Arrays Especiais
zeros = np.zeros((3, 4))  # Matriz 3x4 cheia de zeros
print(zeros)

ones = np.ones((2, 2))  # Matriz 2x2 cheia de uns
print(ones)


# Criar uma sequência de números (arange)
arange = np.arange(0, 10, 2)  # De 0 a 10, pulando de 2 em 2
print(arange)

#Máscaras Booleanas
#O que é uma máscara booleana? É uma técnica para filtrar 
#elementos de um array com base em condições.

arr = np.array([1, 2, 6, 4, 9])
mask = arr > 5  # Cria uma máscara booleana
print(mask)  # Mostra a máscara
print(arr[mask])  # Aplica a máscara no array


# Operações Estatísticas
arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))  # Média dos valores
print(np.std(arr))   # Desvio padrão
print(np.sum(arr))   # Soma total
print(np.min(arr))   # Valor mínimo
print(np.max(arr))   # Valor máximo


#Eixos (axis) em Arrays Multidimensionais
#Quando trabalhamos com matrizes, podemos 
#realizar operações ao longo de linhas ou colunas.

matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Soma ao longo das colunas (axis=0)
print(np.sum(matriz, axis=0))

# Soma ao longo das linhas (axis=1)
print(np.sum(matriz, axis=1))
