

def sayHello(name='Nome default', age='Ano Default'):
    print(name, age)

sayHello('matheus', 18)

#keyword arguments
sayHello(name='bibi', age='17')



# Return

def sum(num1, num2):
    return num1 + num2

print(sum(1,2))


# DocStrings

def test(a):
    '''
    Info: this function test and prints # aqui fizemos um comentario sobre o que a função faz quando apssa o mouse em cima dela
    '''
    print(a)

test('hello')


# *args and **kwargs (key word args)

def superFunc(*args, **kwargs): # adicionando o *args voce pode colocar quantos argumentos quiser na função sendo numeros e o **kwargs str
    print(args)
    return sum(args)

