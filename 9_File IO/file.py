myFile = open('C:\\Users\\mathe\\Desktop\\test.txt') #abre o arquivo


print(myFile.read()) #lê o arquivo
myFile.seek(0) #move o cursor até essa linha
print(myFile.read()) 
print(myFile.readline()) #lê uma linha especifica 