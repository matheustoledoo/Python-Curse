import numpy as np

#Um array é como uma tabela de números. Ele pode ser 1D (vetor),
#2D (matriz) ou nD (multidimensional).

#Array 1D (vetor)
# Criando um array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Array 2D (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

arra = np.array([10, 20, 30, 40, 50])
print(arra[0])  # Primeiro elemento
print(arra[-1])  # Último elemento

ar = np.array([1, 2, 3])
print(ar + 10)  # Soma 10 a cada elemento
print(ar * 2)   # Multiplica cada elemento por 2