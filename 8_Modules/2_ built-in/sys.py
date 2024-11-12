
# built-in sao bibliotecas internas do python

import sys #essa biblioteca permite abrir, criar, executar, ler... coisas dentro do seu computador

def main():
    # Exibe argumentos da linha de comando
    print("Nome do arquivo:", sys.argv[0])
    print("Argumentos:", sys.argv[1:] if len(sys.argv) > 1 else "Nenhum argumento passado")
    
    # Exibe o sistema operacional e a versão do Python
    print("Sistema Operacional:", sys.platform)
    print("Versão do Python:", sys.version)
    
    # Exibe o caminho de pesquisa de módulos e modifica-o
    print("Caminhos de importação:")
    for path in sys.path:
        print("  ", path)
    sys.path.append("/novo/caminho/para/modulo")
    print("Novo caminho adicionado:", sys.path[-1])
    
    # Mostra o tamanho de um objeto em bytes
    objeto = [1, 2, 3, 4, 5]
    print(f"\nTamanho do objeto {objeto}:", sys.getsizeof(objeto), "bytes")
    
    # Redireciona a saída padrão para um arquivo
    original_stdout = sys.stdout
    with open("saida.txt", "w") as f:
        sys.stdout = f
        print("Este texto será salvo no arquivo saida.txt.")
    sys.stdout = original_stdout
    print("Texto padrão no console.")
    
    # Exibe o limite de recursão
    print("Limite de recursão atual:", sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
    print("Novo limite de recursão:", sys.getrecursionlimit())

if __name__ == "__main__":
    main()