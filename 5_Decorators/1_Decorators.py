
# Decorators

#Eles permitem "envolver" uma função com outra função, adicionando funcionalidades de maneira concisa e reutilizável. 
#Os decorators são amplamente usados para adicionar funcionalidades como autenticação, logging, medição de tempo...

#Um decorator é uma função que recebe outra função como argumento, adiciona algum comportamento a essa função e retorna uma nova função com o comportamento adicional. 
#O símbolo @ é usado para aplicar um decorator a uma função de maneira prática.


# função que recebe outra função com um parametro e retorna essa função (a grande jogada é, voce pode modificar do jeito que voce quiser o decorator)
def myDecorator(func):
    def wrapFunction():
        print('*******')
        func()
        print('*******')
    return wrapFunction


@myDecorator
def hello():
    print('helooo')

@myDecorator
def bye():
    print('byeee')


hello()
bye()




#------------------------------------------------------------------------------------------

def log_args(funcao):
    #*args e **kwargs permitem que wrapper aceite qualquer número de argumentos posicionais e nomeados.
    def wrapper(*args, **kwargs):
        # Exibe uma mensagem com o nome da função e os argumentos passados
        print(f"Chamando {funcao.__name__} com argumentos {args} e {kwargs}")
        
        #  # Chama a função com os argumentos
        return funcao(*args, **kwargs)

    return wrapper


# Aplicação do decorator @log_args à função soma
@log_args
def soma(a, b):

    return a + b


resultado = soma(3, 5)  
print(f"Resultado: {resultado}") 


#-----------------------------------------------------------------------------------------------

from time import time

def performance(fn):
    def weapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result
    return weapper


@performance
def longTime():
    for i in range(100000):
        i*5

longTime()