class Address:

    def __init__(self, street:str, city:str, state:str, zipc:str):

        self.street = street
        self.city = city
        self.state = state 
        self.zipc = zipc 

    def getInfo(self):
        info = self.street,self.city,self.state,self.zipc
        return info
        
class Person:

    def __init__(self, name:str, age:int):

        self.name = name 
        self.age = age
        self.addr = None

    def getInfo(self):
        info = self.name,self.age
        if self.addr != None:
            info2 = self.addr.street, self.addr.city, self.addr.state, self.addr.zipc
            return info + info2

    def prepForFile(self):
        #Changes the Person object into a comma seperated string for entry into data file. 
        if self.addr != None:
            return self.name + "," + self.age + "," + self.addr.street + "," + self.addr.city + "," + self.addr.state + "," + self.addr.zipc
        else:
            return self.name + "," + self.age
    
    def changeName(self):
        name = input("Please enter a new name.")
        choice = input(f'Is {name} the correct name Y/N?')
        if choice.upper() == "Y":
            self.name = name
        elif choice.upper() == "N":
            changeName(name)
