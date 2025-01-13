from PIL import Image, ImageFilter # chamando a biblioteca

img = Image.open('c:/Users/mathe/Desktop/PY/12_Scripting/1_Image/Pokedex/pikachu.jpg') # abre a imagem que esta na pasta

filter = img.filter(ImageFilter.BLUR) #aqui fazemos com que a imagem fique borrada(uma das opçoes do ImageFilter)
filterConvert = img.convert('L') #deixa preto e branco
rotacao = filterConvert.rotate(90) #rotaciona a imagem em 90 graus
resize = filterConvert.resize((300, 300)) #ele muda a renderização da imagem

filter.save("ImagemBorrada.png", 'png') #cria essa imagem borrada e salva como png
filterConvert.save("gray.png", 'png')
filterConvert.show() #o show ele abre a imagem para voce
rotacao.show()


print(img) #fala se a imagem existe