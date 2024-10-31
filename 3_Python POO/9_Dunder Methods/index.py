
class Toy():
    def __init__(self, color, agr, myDict):
        self.color = color
        self.age = agr
        self.myDict = {
            'name': 'yoyo',
            'hasPet': False
        }

    def __str__(self):
       return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __del__(self):
        return 'deleted!'
    
    def __getitem__(self, i):
        return self.myDict[i]
    

actionFigure = Toy('red', 0)

print(actionFigure.__str__()) # é o mesmo que vc fazer str(actionfigure)
print(actionFigure['name'])