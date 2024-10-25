# enumerate

#ele vai enumerar algo

for i, char in enumerate('Hello'):
    print(i, char) #ele vai inumerar o 'Hello' dando cada letra um numero

for i, char in enumerate(list(range(0, 100))):
    print(i, char)