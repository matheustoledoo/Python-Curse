import sys
import PyPDF2

# Capturar os argumentos fornecidos na linha de comando (exceto o script)
inputs = sys.argv[1:]

# Função para combinar arquivos PDF
def pdf_combiner(pdf_list):
    # Usar PdfMerger no lugar de PdfFileMerger
    merger = PyPDF2.PdfMerger()
    
    # Adicionar cada PDF na lista
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"Erro: Arquivo '{pdf}' não encontrado. Verifique o caminho.")
        except Exception as e:
            print(f"Erro ao processar o arquivo '{pdf}': {e}")
    
    # Salvar o PDF combinado
    with open('super.pdf', 'wb') as output_file:
        merger.write(output_file)

# Validar se há arquivos fornecidos como entrada
if inputs:
    pdf_combiner(inputs)
    print("PDFs combinados com sucesso! O arquivo gerado é 'super.pdf'.")
else:
    print("Erro: Nenhum arquivo PDF foi fornecido como entrada.")
