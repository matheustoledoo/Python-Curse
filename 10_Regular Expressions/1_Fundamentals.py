# Importa o módulo 're' para trabalhar com expressões regulares
import re

# Define a string onde vamos buscar o padrão
text = 'search inside of this text please'

# Utiliza re.search para encontrar a primeira ocorrência do padrão 'this' na string 'text'
# Retorna um objeto de correspondência se o padrão for encontrado, caso contrário, retorna None
match_a = re.search('this', text)

# Compila o padrão 'this' em um objeto de padrão para reutilização e maior eficiência
pattern = re.compile('this')

# Usa o objeto compilado para buscar a primeira ocorrência do padrão na string
match_b = pattern.search(text)

# Usa o objeto compilado para encontrar todas as ocorrências do padrão na string
# Retorna uma lista com todas as correspondências encontradas
all_matches = pattern.findall(text)

# Imprime o objeto de correspondência gerado por re.search
# Exemplo de saída: <re.Match object; span=(17, 21), match='this'>
print(match_a)

# Usa o método .group() para obter o texto correspondente ao padrão encontrado no objeto match_a
# Exemplo de saída: 'this'
print(match_a.group())

# Imprime os resultados das outras buscas
# match_b deve ser igual a match_a porque ambos buscam a mesma coisa
print(match_b)

# all_matches contém uma lista de todas as correspondências; nesse caso, ['this']
print(all_matches)