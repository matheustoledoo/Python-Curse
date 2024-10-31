# List

myList = [i for i in 'hello']  # com isso evitamos criar um codigo amais apenas para colocar um for dentro do array e colocar um .append
myList2 = [num for num in range(0, 100)]
myList3 = [num for num in range(0, 100) if num % 2 == 0]  # conseguimos colocar um if tambem

print(myList3)

# Set

simpleDict = {
    'a': 1,
    'b': 2
}

myDict = {key: value**2 for key, value in simpleDict.items() if value%2==0} 
myDict2 = {num: num*2 for num in [1,2,3]}

print(myDict)


# Dictionary

myList = (i for i in 'hello')  # com isso evitamos criar um codigo amais apenas para colocar um for dentro do array e colocar um .append
myList2 = (num for num in range(0, 100))
myList3 = (num for num in range(0, 100) if num % 2 == 0)  # conseguimos colocar um if tambem


# Exercice

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)