# Short Circuiting

isFriend = True
isUser = True

if isFriend and isUser:
    print('Best Friend Forever')
elif isFriend or isUser:
    print('Best Friend Forever too')


# Logical Operators

#>
#<
#==
#<=
#>=
#!=
#and
#or
#not
#is (is é tipo um ===)

# exercice

isMagic = True
isExpert = True

if isMagic and isExpert:
    print('you´re a good magic')
elif isMagic and not isExpert:
    print("you´re soso")
elif not isMagic:
    print('you need magic powers')