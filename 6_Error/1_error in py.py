
# Error Handling

while True:
    try:
        age = int(input('what is yout age: '))
        print(age)
    except ValueError: #esse seria o catch
        print('please enter a number')
    except ZeroDivisionError: #a idade nao pode ser zero, entao chamaos essa função interna do python
        print('please enter age higher than 0')
    else:
        print('thanks')
        break
    finally: # o finally vai acontecer, nao importa se der erro ou nao
        print('done')


#---------------------------------------------------------------------------------------------------------------------------------

def sum(num1, num2):
    try: 
     return num1 + num2
    except TypeError:
        print('please, enter numbers')

print(sum(1, 2))