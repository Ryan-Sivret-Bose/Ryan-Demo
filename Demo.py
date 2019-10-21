

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
    #Find for search term and print the line from the file
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            print(line)

def addNewContact():
    #Ask for contact information, then asks final user verification before entry into file. 
    #Could change this to get from the .csv file
    contactParams = ['First Name', 'Last Name', 'Street', 'City', 'State', 'Zip']
    contacts = ""
    enterContact(confirmContact(createContact(contactParams),contacts),contacts)
    postContactMenuSelection()

def createContact(contactList):
    #Creates list comma seperated string based on user input.
    contacts = ""
    for value in contactList:
        contact = input(f"{value}?")
        contacts += contact + ","
    return contacts   

def confirmContact(contactInfo,contacts): 
    #Prints contact info and asks if it correct or not. Returns boolean. 
    print(contactInfo)
    choice = input("Is this the correct contact information Y/N?")
    if choice.upper() == 'Y':
        return True
    elif choice.upper() == 'N':
        return False
    elif choice.upper() != 'N' or 'Y':
        print("Did not understand your response. Please try again")
        enterContact(confirmContact(contactInfo,contacts),contacts)

def enterContact(boo,contactInfo):
    #Enters contact information if it is correct. Reruns addNewContact if value is false.
    if boo == True:
        fh = open(fname,'a')
        fh.write(contactInfo + '\n')
        fh.close
        print("Contact has been added!")
    if boo == False:
        addNewContact()

def postContactMenuSelection():
    #Post selection menu options after completing addNewContact()
        choice = input("What would you like to do next? Enter 1 to return to Main Menu, Enter 2 to enter another contact: ")
        if choice == '1':
            Menu()
        elif choice == '2':
            addNewContact()  
        elif choice != '1' or '2':
            postContactMenuSelection()



#def 
    #  if choice.upper() == 'Y':
    #     fh = open(fname,'a')
    #     fh.write(contactInfo + '\n')
    #     fh.close
    #     print("Contact has been added!")
    # elif choice.upper() == 'N':
    #     addNewContact()
    # elif choice.upper() != 'N' or 'Y':
    #     wrongContact()

def wrongContact():
    #User did not enter in correct command, asking if want to return to Main Menu or addNewContact
    print('Sorry, Did not recognize that entry, please try again' )
    choice = input('1 - Return to the Main Menu, 2 - Return to add contact: ')
    if choice == '1':
        Menu()
    elif choice == '2':
        addNewContact()

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
        addNewContact()
    #elif choice == '4':
    elif choice == '5':
        print("All Done!")
    elif choice != '1' or '2' or '3' or '4':
        quit()
        #print("Sorry, Did not recognize that entry, please try again")
        #Menu()

Menu()
