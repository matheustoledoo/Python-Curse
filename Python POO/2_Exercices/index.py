
class Cat:
    species = 'Animal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

        

cat1 = Cat('alfred', 2)
cat2 = Cat('garfield', 3)


def oldest(*args):
    return max(args) #o max ve o maior


print(f'Oldest cat is {oldest(cat1.age, cat2.age)}')