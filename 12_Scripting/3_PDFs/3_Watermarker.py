import PyPDF2

# Ler o arquivo da marca d'água e o arquivo template
waterMark = PyPDF2.PdfReader('c:/Users/mathe/Desktop/PY/12_Scripting/3_PDFs/wtr.pdf')
template = PyPDF2.PdfReader('c:/Users/mathe/Desktop/PY/12_Scripting/3_PDFs/dummy.pdf')
output = PyPDF2.PdfWriter()

# Iterar sobre as páginas do template
for i in range(len(template.pages)):  # Use len() em vez de getNumPages()
    page = template.pages[i]
    page.merge_page(waterMark.pages[0])  # Usar merge_page em vez de mergePage()
    output.add_page(page)

# Escrever a saída em um novo arquivo PDF
with open('watermarkedOutput.pdf', 'wb') as file:
    output.write(file)

print("Marca d'água aplicada com sucesso!")
