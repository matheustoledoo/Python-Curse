
# Exercice: check for duplicates in list:

list = ['a', 'b', 'c', 'c', 'd', 'd']

duplicates = []

for i in list:
    if list.count(i) > 1:  # count fala quantos itens iguais tem e se dor maior que um ele adiciona
        if i not in duplicates: # para nao duplicar
         duplicates.append(i) # append adiciona na lista

print(duplicates)
