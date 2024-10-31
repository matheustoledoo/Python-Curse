# Set

#set é uma coleção não ordenada de objetos unicos

mySet = {1,2,3,4,5,5} #ou seja, tudo deve ser unico e nao pode ser repetido, como aqui apenas um dos dois 5 ira aparecer
yourSet = {4,5,6,7,8,9,10}

print(mySet.difference(yourSet)) #ele vai tirar os iguais e deixar os diferentes do mySet
print(mySet.discard(5)) #ele vai discartar o numero
print(mySet.difference_update(yourSet)) #muda o elemento mantendo a diferença
print(mySet.intersection(yourSet)) #faz uma interseção entre os dois(pegar os iguais e mantes)
print(mySet.isdisjoint(yourSet)) #ve se eles se sobrepoem(se tem iguais)
print(mySet.issubset(yourSet)) #ve se tem elementos iguais um no outro
print(mySet.union(yourSet)) #une os 2

list = [1,2,3,3,5]
print(set(list)) #assim fazemos para nao deixar o valor se repetir

