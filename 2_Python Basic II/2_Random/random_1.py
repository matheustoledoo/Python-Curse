import random

name = ['matheus', 'fainer', 'adrian']
sorteio = (random.choice(name)) # sorteia um nome

print(sorteio)


random.shuffle(name) # embaralha os nomes
print(name)