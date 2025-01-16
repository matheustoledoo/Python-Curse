import requests  # Biblioteca para fazer requisições HTTP
import hashlib  # Biblioteca para gerar hashes
import sys  # Biblioteca para acessar argumentos da linha de comando

def request_api_data(query_char):
    # Define a URL da API adicionando os primeiros 5 caracteres do hash
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    
    # Faz uma requisição GET para a API
    res = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    
    # Retorna a resposta da API
    return res

def get_password_leaks_count(hashes, hash_to_check):
    # Divide o conteúdo retornado pela API em linhas e separa cada linha em hash e contagem
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    # Percorre os hashes retornados pela API
    for h, count in hashes:
        # Verifica se o hash fornecido corresponde ao hash restante (tail)
        if h == hash_to_check:
            return count  # Retorna a quantidade de vazamentos encontrados
    
    # Retorna 0 caso o hash não seja encontrado
    return 0

def pwned_api_check(password):
    # Converte a senha em um hash SHA-1
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Divide o hash em dois: os primeiros 5 caracteres e o restante
    first5_char, tail = sha1password[:5], sha1password[5:]
    
    # Envia os primeiros 5 caracteres para a API
    response = request_api_data(first5_char)
    
    # Verifica a quantidade de vazamentos para o hash restante
    return get_password_leaks_count(response, tail)

def main(args):
    # Percorre cada senha passada como argumento
    for password in args:
        # Verifica se a senha foi comprometida
        count = pwned_api_check(password)
        
        # Exibe uma mensagem apropriada com base no resultado
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    
    # Retorna uma mensagem indicando que o processo foi concluído
    return 'done!'

# Ponto de entrada do script
if __name__ == 'main':
    # Executa a função main com os argumentos da linha de comando (exceto o nome do script)
    sys.exit(main(sys.argv[1:]))