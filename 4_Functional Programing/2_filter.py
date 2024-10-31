
# Filter
#A função filter() em Python é usada para filtrar elementos de um iterável (como uma lista ou tupla) com base em uma condição. 

#sintaxe: filter(funcao, iteravel)


# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função que verifica se um número é par
def eh_par(num):
    return num % 2 == 0

# Usando filter() para aplicar a condição de paridade
resultado = filter(eh_par, numeros)

# Convertendo o resultado para uma lista para visualização
print(list(resultado))  # Saída: [2, 4, 6, 8, 10]



# Lista de palavras
palavras = ["gato", "elefante", "cachorro", "peixe", "leão"]

def quatroLetras(palavra):
    if len(palavra)> 4:
        return palavra
 
# Usando filter() para manter palavras com mais de 4 letras
print(list(filter(quatroLetras, palavras)))


