
# for

#ele percorre todo o array, objeto, dicionary, tudo item por item

for i in 'zero to mastery':
  print(i)

for i in {1,2,3,4,5}:
  for x in ['a', 'b', 'c']:
    print(i, x)



# iterables

#iteravel significa que é um objeto ou uma coleção(array) que pode ser iterado novamente e ite´ravel pode ser uma lista,dicionario,touple,set e string
#iterado significa que podemos ir um por um como no exemplo acima e aqui abaixo

user = {
  'name': 'Matheus',
  'age': 18,
  'canSwim': True,
}

for i in user: #apenas o user sozinho ele mostra os valores de nomeação
  print(i) # aqui percorremos todos os itens dentro do objeto user

for i in user.items(): #com o .items ele mostra todos os itens dentro sendo o nome e o que esta dentro
  print(i)

for i in user.values(): #com o .values ele mostra todos os valores apenas
  print(i)


# Exercice

list = [1,2,3,4,5,6,7,8,9,10]
count = 0

for i in list:
  print(i)
  i + 1


# exercice

list = []

def increment2(li):
  for item in li:
    list.append(item*2)
  return print(list)

increment2([1,2,3])