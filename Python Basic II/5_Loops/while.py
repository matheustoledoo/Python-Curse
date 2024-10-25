
# while

i = 0

while i < 100:
    pass
    print(i)
    i += 1
    continue
else:
    print('done')
    

# exercice

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,1,1]
]

for i in picture:
    for pixel in i:
        if(pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')