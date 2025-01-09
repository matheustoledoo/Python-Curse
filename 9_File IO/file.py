#myFile = open('C:\\Users\\mathe\\Desktop\\test.txt') #abre o arquivo

#ou

try:
    with open('C:\\Users\\mathe\\Desktop\\test.txt', mode='r+') as myFile: #com esse mode='r+' possibilita para tanto escrever como ler o arquivo 
        text = myFile.write('hey its me a')                                #mas tbm tem o 'r' so para ler 'w' so para escrever 'a' para escrever adicionando e nao apagar o que ja tiver escrito
        print(myFile.read()) #lê o arquivo
except FileNotFoundError as err:
    print('file does not exist')
    raise err



# myFile.seek(0) #move o cursor até essa linha
# print(myFile.readlines()) #lê uma linha especifica 


