

fname = input('Hello, Welcome, What is the name of your address book? ')+".csv"

def readData(fname):
    fh = open(fname)
    for line in fh:
        print(line)
    fh.close

def readAddressBook(fname):
    fh = open(fname,"r")
    file_contents = fh.read()
    print(file_contents)
    fh.close

def writeData(data):
    fh = open(fname,'w')
    f.write(str(data))

def search(fname):
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            print(line)
                
    #c = list(contact)
    #for line in range(0, len(list)):
    #    if choice in line:
    #        print(line)


#def searchstreet(street):
    #fh=open(fname)
    #for line in fh:

def addContact():
    name = input("First Name? ")
    contact = []
    contact.append(name)
    lname = input('Last Name? ')
    contact.append(lname)
    street = input("What is their street address? ")
    contact.append(street)
    city = input("What city/town do they live in? ")
    contact.append(city)
    state = input("What state do they live in? ")
    contact.append(state)
    zip1 = input("What is zipcode of where they live? ")
    contact.append(zip1)
    fh = open(fname,'a')
    fh.write(','.join(map(str, contact)))
    fh.write('\n')
    fh.close

    #str(contact).strip('[]')
   #','.join(map(str, contact)) 


def Menu():
    #Choice of adress book and Selection of Task
    choice = input('Enter 1 to look at your Contacts, Enter 2 to Search for a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to Exit: ')
    if choice == '1':
        readAddressBook(fname)
        Menu()
    elif choice == '2':
        search(fname)
        Menu()
    elif choice == '3':
        addContact()
        Menu()
    #elif choice == '4':
    elif choice == '5':
        quit()

Menu()








#fname = input("Enter an Address Book you would like to read: ")
#name = input("Enter a name you are lookin for: ")
#searchname(name)
#addContact()





#f=open('data.txt','w')
#f.write('this is some sample data...')
#f.close()



