
# Zip
#A função zip() em Python é usada para combinar elementos de várias sequências (como listas, tuplas, etc.) 

#sintaxe: zip(*iteráveis)

# Listas de dados
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 22]

# Usando zip() para combinar as listas
resultado = zip(nomes, idades)

# Convertendo o resultado para uma lista de tuplas para visualização
print(list(resultado))  # Saída: [('Ana', 25), ('Bruno', 30), ('Carlos', 22)]



# Listas de dados
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 22]
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba"]

# Usando zip() para combinar as três listas
resultado = zip(nomes, idades, cidades)

# Convertendo o resultado para uma lista de tuplas para visualização
print(list(resultado))
# Saída: [('Ana', 25, 'São Paulo'), ('Bruno', 30, 'Rio de Janeiro'), ('Carlos', 22, 'Curitiba')]
