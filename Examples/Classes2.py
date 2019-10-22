class Computer:
    
    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def update(self):
        self.age = 30
    
    def compare(self,other):
        if self.age == other.age:
            return True 
        else:
            return False


c1 = Computer()
c1.update()
c2 = Computer()

if c1.compare(c2):
    print("Same")
else:
    print('Not the same')

print(c1.age)
print(c2.name)