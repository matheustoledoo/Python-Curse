
#*args: captura todos os argumentos posicionais passados para wrapper em uma tupla. No nosso caso, args recebe (user1,), onde user1 é o primeiro argumento.
#**kwargs: captura todos os argumentos nomeados (keyword arguments) passados para wrapper em um dicionário. Neste caso, não há nenhum kwargs adicional, então ele fica vazio.

# authenticated recebe uma função fn e define uma função interna wrapper.
# wrapper utiliza *args e **kwargs para poder aceitar qualquer quantidade de argumentos.
# Lógica do wrapper:

# wrapper verifica se o usuário (args[0]) tem valid como True.
# Se for True, ele executa a função fn (neste caso, message_friends) com os mesmos argumentos.
# Se False, ele imprime "invalid user".

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": True,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn): #fn é a função que será decorada, neste caso, message_friends.
    def wrapper(*args, **kwargs): #wrapper é a função interna que será chamada no lugar de fn quando a função decorada (message_friends) for chamada.
                                  #O *args e **kwargs permitem que wrapper receba qualquer número de argumentos posicionais e argumentos com palavras-chave, respectivamente.
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)