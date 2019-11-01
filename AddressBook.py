import AddressModel

fname = ''
person = None

def readData():
    fh = open(fname)
    for line in fh:
        print(line)
    fh.close

def readAddressBook():
    fh = open(fname,"r")
    file_contents = fh.read()
    print(file_contents)
    fh.close

def writeData(data):
    fh = open(fname,'w')
    f.write(str(data))

def simpleSearch():
    #Find for search term and print the line from the file
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            print(line)

def searchAndGetContactInfo():
    global person
    fh = open(fname, 'r')
    choice = input('Enter in a piece of information about this person: ')
    searchlines = fh.readlines()
    fh.close()
    for i, line in enumerate(searchlines):
        if choice in line:
            realline = line.rstrip()
            li = list(realline.split(","))
            a1 = getAddressFromList(li)
            person = getPersonFromAdrLst(li,a1)
            return person

def contactOptions():
    choice = input('Enter 1, Enter 2 to Search for a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to Exit: ')

def addNewContact():
    #Ask for contact information, then asks final user verification before entry into file. 
    contactParams = ['Name', 'Age', 'Street', 'City', 'State', 'Zip']
    mylist = createContact(contactParams)
    a1 = getAddressFromList(mylist)
    p1 = getPersonFromAdrList(mylist,a1)
    #contacts = createContact(contactParams)
    enterContact(confirmContact(p1,mylist),mylist)
    postContactMenuSelection()

def getPersonFromAdrLst(mylist:list,addr:object):
    p1 = AddressModel.Person(mylist[0],mylist[1])
    p1.addr = addr
    return p1
    
def getAddressFromList(mylist):
    a1 = AddressModel.Address(mylist[2],mylist[3],mylist[4],mylist[5])
    return a1 

def createContact(contactList):
    #Creates list comma seperated string based on user input.
    contacts = []
    for value in contactList:
        contact = input(f"{value}?")
        contacts.append(contact)
    return contacts

def enterAddress():
    getAddressFromList(createContact())

def createString(mylist):
    mylist = ",".join(mylist)
    return mylist

def confirmContact(pers:object): 
    #Prints contact info and asks if it correct or not. Returns boolean.
    string1 = pers.name + "," + pers.age
    string2 = pers.addr.street + "," + pers.addr.city + "," + pers.addr.state + "," + pers.addr.zipc
    string3 = string1 + "," + string2
    print(string3)
    choice = input("Is this the correct contact information Y/N?")
    if choice.upper() == 'Y':
        return True
    elif choice.upper() == 'N':
        return False
    # elif choice.upper() != 'N' or 'Y':
    #     print("Did not understand your response. Please try again")
    #     enterContact(confirmContact(pers),mylist)

def enterContact(boo:bool,prs:object):
    #Enters contact information if it is correct. Reruns addNewContact if value is false.
    contactInfo = createString(contactInfo)
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

def wrongContact():
    #User did not enter in correct command, asking if want to return to Main Menu or addNewContact
    print('Sorry, Did not recognize that entry, please try again' )
    choice = input('1 - Return to the Main Menu, 2 - Return to add contact: ')
    if choice.strip() == '1':
        Menu()
    elif choice.strip() == '2':
        addNewContact()

def addressBookSelection():
    fname = input('Hello, Welcome, What is the name of your address book? ')+".csv"
    return fname 

def editContactMenu():
    choice = input('''What would you like to change about your person's contact information? 
Enter 1 for Name,
Enter 2 for Age,
Enter 3 for Street,
Enter 4 for City,
Enter 5 for State,
Enter 6 for zip
Enter 7 to return: ''')
    if choice.strip() == "1":
        person.changeName()
    if choice.strip() == "2":
        person.changeAge()
    if choice.strip() == "3":
        person.changeStreet()
    if choice.strip() == "4":
        person.changeCity()
    if choice.strip() == "5":
        person.changeState()
    if choice.strip() == "6":
        perosn.changeZip()
    if choice.strip() == "7":
        pass


def Menu():
    #Choose between options of being able to perform basic operations on an address book.
    choice = input('Enter 1 to look at your Contacts, Enter 2 to Search or Edit a Contact, Enter 3 to Add a Contact, Enter 4 to Delete a Contact, Enter 5 to select a new address book, Enter 6 to Exit: ')
    if choice == '1':
        readAddressBook()
        Menu()
    elif choice == '2':
        selection = confirmContact(searchAndGetContactInfo())
        if selection == True:
            editContactMenu()
            enterContact(confirmContact())
            Menu()
        else:
            Menu()
    elif choice == '3':
        addNewContact()
    #elif choice == '4':
    elif choice == '5':
        fname = addressBookSelection()
        Menu()
    elif choice == '6':
        print("All Done!")
    elif choice != '1' or '2' or '3' or '4':
        quit()
        #print("Sorry, Did not recognize that entry, please try again")
        #Menu()

fname = addressBookSelection()
Menu()
#searchAndGetContact()


