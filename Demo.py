


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
    #Find for search term and print the line from the file
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            print(line)

def addNewContact(fname):
    #Ask for contact information, then asks final user verification before entry into file. 
    #Could change this to get from the .csv file
    contactParams = ['First Name', 'Last Name', 'Street', 'City', 'State', 'Zip']
    contacts = ''
    contacts = createContact(contactParams)
    enterContact(confirmContact(contacts),contacts,fname)
    postContactMenuSelection(fname)

def createContact(contactList):
    #Creates list comma seperated string based on user input.
    contacts = ""
    for value in contactList:
        contact = input(f"{value}?")
        contacts += contact + ","
    return contacts

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
        enterContact(confirmContact(contactInfo),contactInfo,fname)

def enterContact(boo:bool,contactInfo:str,fname:str)->None:
    #Enters contact information if it is correct. Reruns addNewContact if value is false.
    if boo == True:
        fh = open(fname,'a')
        fh.write(contactInfo + '\n')
        fh.close
        print("Contact has been added!")
    if boo == False:
        addNewContact(fname)

def postContactMenuSelection(fname):
    #Post selection menu options after completing addNewContact()
        choice = input("What would you like to do next? Enter 1 to return to Main Menu, Enter 2 to enter another contact: ")
        if choice == '1':
            mainMenu(fname)
        elif choice == '2':
            addNewContact(fname)  
        elif choice != '1' or '2':
            postContactMenuSelection()

def wrongContact():
    #User did not enter in correct command, asking if want to return to Main Menu or addNewContact
    print('Sorry, Did not recognize that entry, please try again' )
    choice = input('1 - Return to the Menu, 2 - Return to add contact: ')
    if choice == '1':
        mainMenu()
    elif choice == '2':
        addNewContact()

def selectAddressBook():
        fname = input('What address would you like to work with? ')+".csv"
        return fname

def Menu():
    #Choose address book and return variable to use - Should be able to run again to choose address book.
    fname = selectAddressBook() 
    #Choice of adress book and Selection of Task
    choice = input('Enter 1 to look at your Contacts, Enter 2 to Search for a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to select a new address book, Enter 6 to Exit: ')
    if choice == '1':
        readAddressBook(fname)
        mainMenu(fname)
    elif choice == '2':
        search(fname)
        mainMenu(fname)
    elif choice == '3':
        addNewContact(fname)
    #elif choice == '4':
    elif choice == '5':
        Menu()
    elif choice == '6':
        print("All Done!")
    elif choice != '1' or '2' or '3' or '4' or '5':
        quit()
        

def mainMenu(fname):
    # Cutdown version of the menu that does not have the option to select an an address book
    choice = input('Enter 1 to look at your Contacts, Enter 2 to Search for a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to select a new address book, Enter 6 to Exit: ')
    if choice == '1':
        readAddressBook(fname)
        mainMenu(fname)
    elif choice == '2':
        search(fname)
        mainMenu(fname)
    elif choice == '3':
        addNewContact(fname)
    #elif choice == '4':
    elif choice == '5':
        Menu()
    elif choice == '6':
        print("All Done!")
    elif choice != '1' or '2' or '3' or '4' or '5':
        quit()
        

Menu()
