
# Fundamental Data types

#--------------------------------------------------------------------------------------------------------------------------------

# int and float

print(type(2 + 2)) # int
print(type(2 - 2)) # int
print(type(0.001)) # Float
print(type(2/4)) # (0,5) Float

print(type(10.66)) # Float

print(2 ** 3) # aqui fazemos a potenciação (2^3)
print(5 // 4) # aqui ele arredonda o numero para nao ser menos de 0 ou 0. alguma coisa
print(6 % 4) # resto da divisao

# math functions

print(round(3.1)) # aproxima do numero mais proximo ou seja 3
print(abs(-20)) # Return the absolute value of the argument. (ou seja o positivo)
print(bin(5)) ## mostra o numero binario nesse caso (101)


#--------------------------------------------------------------------------------------------------------------------------------

# string

print(type("hello")) # str

# formatted strings

name = 'matheus'

print(f"hi {name}, how are u?")

# string index

selfish = '12345678'

print(selfish[0]) # retornara a posição 0 (1)
print(selfish[0:7]) # retornara a posição 0 ao 7


#--------------------------------------------------------------------------------------------------------------------------------

print(len('heloooo')) # esse len é o lenght

quote = 'helloooo there'

print(quote.upper()) # deixa tudo em capslock
print(quote.lower()) # deixa tudo minusculo
print(quote.find('there')) # verifica se tem essa frase ou letra ou numero na variavel
print(quote.replace('there', 'someone')) # troca um pelo outro
print(quote.capitalize()) # deixa apenas a primeira letra da frase em cpslock


birth_year = input("what year were you born?")

age = 2024 - int(birth_year) # transformamos a string em int pelo int()

print(age)


# exercice

username = input("what is your name?")
password = input("what is your password?")

passwordLenght = len(password)
secret = '*' * passwordLenght

print('{usename} and {secret}')


# matrix

# aqui criamos arrays e sub-arrays
matrix = [ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matrix[0][1]) # ai quando for chamado é preciso abrir 2 vezes, a primeira para indicar qual dos arrays vc quer e o outro para posiçaõ( nesse exemplo de chamada ele vai retornar 2)


#--------------------------------------------------------------------------------------------------------------------------------


# listas

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']

print(li2[0]) # mostra apenas o da posição 0
print(li2[0:3]) # 0 ao 3
print(li2[0::2]) # somente o 0 e o 2

#append()	Adds an element at the end of the list
basket = [1,2,3,4,5]
basket.append(6)
print(basket)

#pop()	Removes the element at the specified position
basket.pop(0) # remove na posição 0

#remove()	Removes the first item with the specified value
basket.remove(2) # aqui ele removera os 2

#clear()	Removes all the elements from the list
#basket.clear()

#index()	Returns the index of the first element with the specified value
basket.index(4) # ele vai mostrar em qual posição do array esta o 4

#in (verifica se tem esse favor dentro do array)
print(4 in basket) # vai retornar true

#count()	Returns the number of elements with the specified value
basket.count(5) # retorna quantos valores tem iguais ao pedido no array

#reverse()	Reverses the order of the list
basket.reverse()

#sort()	Sorts the list
#copy()	Returns a copy of the list

print(list(range(1,100))) # aqui criamos uma lista que vai de 1 a 100 (uma dica, sempre que vc quer tornar algo int ou str ou list coloque ele e () )


#--------------------------------------------------------------------------------------------------------------------------------


# Dictionary (like a object in JS)

dictionary = {
    'a': 1,
    'b': [1,2,3],
    'c': True,
    'x': 'hello'
}

print(dictionary)
print(dictionary['a']) # returns '1'
print(dictionary.get('d', 'hello')) # aqui por que nao tem o 'd' ali na lista ele utiliza o 'hello' como valor padrao mas caso entrar no objeto ele é pricipal e fazemso isso com o .get

print('x' in dictionary) # ver se tem x no dicionario
print('x' in dictionary.keys()) # ver se tem x no dicionario
print('hello' in dictionary.values()) # ver se tem o valor 'hello'
print(dictionary.clear()) # limpa os dados
print(dictionary.pop('a')) # deleta um valor
print(dictionary.popitem()) # deleta um item
print(dictionary.update({'x': 11})) # altera um valor
dictionary2 = dictionary.copy() # copia o objeto


myList = [{
    'a': 1,
    'b': [1,2,3],
    'c': True
},
{
    'a': 1,
    'b': [1,2,3],
    'c': True
}
]

