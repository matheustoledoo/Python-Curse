# Partes básicas de uma expressão regular
# Padrões básicos:
# Letras ou números sozinhos correspondem a si mesmos.
# Exemplos:
# O padrão a procura o caractere a.
# O padrão 123 procura a sequência 123.

# Metacaracteres: Estes são caracteres especiais que representam algo além de si mesmos:
# .: Qualquer caractere (exceto nova linha).
# \d: Qualquer número.
# \s: Qualquer espaço (inclui tab, espaço comum, etc.).
# \w: Qualquer caractere alfanumérico (letras, números e _).
# *: Zero ou mais repetições.
# +: Uma ou mais repetições.
# ?: Zero ou uma repetição.
# ^: Início da string.
# $: Fim da string.
# Escapando metacaracteres: Se você quiser usar um metacaractere como caractere literal, use a barra invertida \:

# Exemplo: Procurar o ponto final ., use \..

import re

def tutorial_regex():
    """
    Tutorial completo sobre a biblioteca re (expressões regulares) em Python.
    """
    print("--- Tutorial sobre a biblioteca 're' em Python ---")

    # Parte 1: re.match - Verifica se o início da string corresponde ao padrão
    print("\n1. Usando re.match")
    texto = "Python é incrível"
    resultado_match = re.match(r'Python', texto)
    if resultado_match:
        print("Match encontrado:", resultado_match.group())
    else:
        print("Nenhum match encontrado.")

    # Parte 2: re.search - Procura um padrão em qualquer lugar da string
    print("\n2. Usando re.search")
    resultado_search = re.search(r'incrível', texto)
    if resultado_search:
        print("Padrão encontrado:", resultado_search.group())
    else:
        print("Nenhum padrão encontrado.")

    # Parte 3: re.findall - Encontra todas as ocorrências do padrão
    print("\n3. Usando re.findall")
    texto_numeros = "Os números são 123, 456 e 789"
    resultado_findall = re.findall(r'\d+', texto_numeros)
    print("Todos os números encontrados:", resultado_findall)

    # Parte 4: re.finditer - Itera sobre todas as correspondências
    print("\n4. Usando re.finditer")
    for match in re.finditer(r'\d+', texto_numeros):
        print("Número encontrado:", match.group(), "na posição", match.span())

    # Parte 5: re.sub - Substitui correspondências do padrão
    print("\n5. Usando re.sub")
    texto_substituido = re.sub(r'\d+', 'X', texto_numeros)
    print("Texto após substituição:", texto_substituido)

    # Parte 6: re.split - Divide a string com base no padrão
    print("\n6. Usando re.split")
    texto_split = "nome1;nome2;nome3"
    resultado_split = re.split(r';', texto_split)
    print("Texto dividido:", resultado_split)

    # Parte 7: Usando modificadores (flags)
    print("\n7. Usando modificadores")
    texto_mod = "Python \u00c9 Incrível"
    resultado_ignorecase = re.search(r'python', texto_mod, re.IGNORECASE)
    if resultado_ignorecase:
        print("Match ignorando maiúsculas/minúsculas:", resultado_ignorecase.group())

    # Parte 8: Escapando metacaracteres
    print("\n8. Escapando metacaracteres")
    texto_escapado = "Use ponto final: . no final."
    resultado_escapado = re.search(r'\.', texto_escapado)
    if resultado_escapado:
        print("Ponto literal encontrado:", resultado_escapado.group())

    print("\n--- Fim do tutorial ---")

# Executar o tutorial
tutorial_regex()