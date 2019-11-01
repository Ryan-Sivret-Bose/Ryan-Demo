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

# def addPerson():

# def addAddress():

def addNewPersonAddress():
    p1 = createPersonAddress()
    p2 = p1.prepForFile()
    enterPerson(confirmContact(p2),p1)

def addNewPerson():
    #Ask for contact information, then asks final user verification before entry into file. 
    #Could change this to get from the .csv file
    p1 = createPerson()
    p2 = p1.prepForFile()
    enterPerson(confirmContact(p2),p1)

def createPerson():
    #Creates list comma seperated string based on user input.
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    p1 = Person(name, age)
    return p1

def createPersonAddress():
    #Creates list comma seperated string based on user input.
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    street = input("Enter Street: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zipc = input("Enter Zip Code: ")
    p1 = Person(name, age)
    p1.addr = Address(street, city, state, zipc)
    return p1


# def createContact(contactList):
#     #Creates list comma seperated string based on user input.
#     contacts = []
#     for value in contactList:
#         info = input(f"{value}?")
#         contacts += info
#         p1 = Person(contacts)
#     return p1


def confirmContact(contactInfo): 
    #Prints contact info and asks if it correct or not. Returns boolean. 
    print(contactInfo)
    choice = input("Is this the correct contact information Y/N?")
    if choice.upper() == 'Y':
        return True
    elif choice.upper() == 'N':
        return False
    elif choice.upper() != 'N' or 'Y':
        print("Did not understand your response. Please try again")
        enterPerson(confirmContact(p2),p2)

def enterPerson(boo,contactInfo):
    #Enters contact information if it is correct. Reruns addNewContact if value is false.
    if boo == True:
        contactInfo = contactInfo.prepForFile()
        fh = open(fname,'a')
        fh.write(contactInfo + '\n')
        fh.close
        print("Contact has been added!")
    elif boo == False and contactInfo.addr == None:
        addNewPerson()
    else:
        addNewPersonAddress()


            


p1 = Person("Ryan Sivret","28")
a1 = Address("157 Shirley Road","Lancaster","MA","01523")


p1.addr = a1

#print(p1.getInfo())

fname = "data.csv"    
addNewPersonAddress()

