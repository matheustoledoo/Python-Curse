
from collections import Counter, defaultdict, OrderedDict

li = [1,1,2,3,4,5,6,7,7,7]
sentence = 'blah blah blah thinking about python'

print(Counter(li)) #ele mostra em um dicionario quntas vezes aquele palavra ou numero apareceu e retorna o que tem mais apariçoes em primeiro
print(Counter(sentence)) #aqui ele faz a mesma coisa so que com caracteres


dictionary = defaultdict(lambda: 'does not exist',  {'a': 1, 'b': 2}) #o defaultdict cria um cenario padrao caso o usuario tente acessar uma informação o dicionario q n existe como no pirnt abaixo

print(dictionary['c'])


d = OrderedDict() #o OrderedDict verifica se o dicionario esta igual ao outro
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['a'] = 1
d['b'] = 2

print(d == d2)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import datetime #biblioteca para data

print(datetime.date.today())


import array

arr = array('i', [1,2,3]) # ele cria um array apenas com int 'i'