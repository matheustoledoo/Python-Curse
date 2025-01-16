# Importar a biblioteca PyPDF2
import PyPDF2

# Abrir o arquivo PDF para leitura
with open('c:/Users/mathe/Desktop/PY/12_Scripting/3_PDFs/dummy.pdf', 'rb') as file:
    # Criar o leitor de PDF
    reader = PyPDF2.PdfReader(file)
    # Obter a primeira página
    page = reader.pages[0]
    # Rotacionar a página 90 graus no sentido anti-horário
    page.rotate(-90)

    # Criar o escritor de PDF
    writer = PyPDF2.PdfWriter()
    # Adicionar a página rotacionada ao escritor
    writer.add_page(page)

    # Salvar o novo PDF
    with open('c:/Users/mathe/Desktop/PY/12_Scripting/3_PDFs/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
