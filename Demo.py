

fname = input('Hello, Welcome, What is the name of your address book? ')+".csv"

#

def readData(fname):
    fh = open(fname)
    for line in fh:
        print(line)
    fh.close
#Print contents of the address book
def readAddressBook(fname):
    fh = open(fname,"r")
    file_contents = fh.read()
    print(file_contents)
    fh.close

def writeData(data):
    fh = open(fname,'w')
    f.write(str(data))

#Find for search term and print the line from the file
def search(fname):
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            print(line)

#Ask for contact information, final verification and entry into file.

def addContact():
    contactParams = ['First Name', 'Last Name', 'Street', 'City', 'State', 'Zip']
    contact = ""
    for index,value in enumerate(contactParams):
        contact = input(f"{value}?")
        contacts += contact + ","
    print(contacts)
    choice = input("Is this the correct contact information Y/N?")
    #try:
        #if choice == 'Y':
            #fh = open(fname,'a')
            #fh.write(contact + '\n')
            #fh.close
        #elif choice == 'N':
            #addContact()
        #elif choice != 'N' or 'Y':
            #quit()
    #except:   
        #print('Sorry, Did not recognize that entry, please try again' )
        #choice = input('1 - Return to the Main Menu, 2 - Return to add contact: ')
        #if choice == '1':
            #Menu()
        #elif choice == '2':
            #addContact()

def addContact1():
    name = input("First Name? ")
    contact = "placeholder"
    contact = name + ","
    lname = input('Last Name? ')
    contact = contact + lname + ","
    street = input("What is their street address? ")
    contact = contact + street + ","
    city = input("What city/town do they live in? ")
    contact = contact + city + ","
    state = input("What state do they live in? ")
    contact = contact + state + ","
    zip1 = input("What is zipcode of where they live? ")
    contact = contact + zip1 
    print(contact)
    choice = input("Is this the correct contact information Y/N?")
    try:
        if choice == 'Y':
            fh = open(fname,'a')
            fh.write(contact + '\n')
            fh.close
        elif choice == 'N':
            addContact()
        elif choice != 'N' or 'Y':
            quit()
    except:   
        print('Sorry, Did not recognize that entry, please try again' )
        choice = input('1 - Return to the Main Menu, 2 - Return to add contact: ')
        if choice == '1':
            Menu()
        elif choice == '2':
            addContact()

def Menu():
    #Choice of adress book and Selection of Task
    choice = input('Enter 1 to look at your Contacts, Enter 2 to Search for a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to Exit: ')
    try:
        if choice == '1':
            readAddressBook(fname)
            Menu()
        elif choice == '2':
            search(fname)
            Menu()
        elif choice == '3':
            addContact()
            #Menu()
        #elif choice == '4':
        elif choice == '5':
            print("All Done!")
        elif choice != '1' or '2' or '3' or '4':
            quit()
    except:
        print("Sorry, Did not recognize that entry, please try again")
        #Menu()

Menu()
