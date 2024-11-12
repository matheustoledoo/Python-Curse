
import shopping.shoppinCart # para chamar um modulo que esta dentro de uma pasta(aqui por exemplo o shoppinCart esta dentro da pasta shopping)
from shopping.moreShopping import shop #aqui chamamos apenas o nome do modulo que queremos importar para nao ficar replicando codigo
from utility import mult, maxNumber # tambem dentor do modulo podemos importar suas funçoes para serem chamadas separadamente


print(mult(2, 9))
print(maxNumber([1,2,3]))
print(shopping.shoppinCart.buy('something'))
print(shop)

print(__name__) # esse name mostra o nome do arquivo que foi executado previnindo erros ou fazendo condiçoes... nesse caso ele retornara 'main'

if __name__ == '__main__':
    print('this is main file')