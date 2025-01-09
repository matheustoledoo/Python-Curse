
from translate import Translator
import sys

translator = Translator(to_lang='pt') #traduz para portugues o txt que esta em ingles

try:
    with open('C:\\Users\\mathe\\Desktop\\PY\\9_File IO\\exercice\\translateThis.txt', mode='r+') as myFile:
        text = myFile.read() #pega o texto que esta no arquivo
        translation = translator.translate(text) #por meio da documentação da biblioteca se faz a tradução assim
        print(translation)
        with open('C:\\Users\\mathe\\Desktop\\PY\\9_File IO\\exercice\\traducion.txt', mode='r+') as myFile2:
            myFile2.write(translation)


except FileNotFoundError as err:
    print('check you file')
    print(err)