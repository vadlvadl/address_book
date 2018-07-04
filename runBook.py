#!/usr/bin/python3.4

# Address book: add contacts, remove, save, print
import AddressBook, Contact
from AddressBook import AddressBook
from Contact import Contact


from pprint import pprint

addressBookFile = 'contacts.pckl'

abook = AddressBook(addressBookFile)
is_running = True

def addContact():
    name = input('Enter name:')
    phone_number = input('Enter phone number:')
    
    c1 = Contact(name)
    c1.addPhone(phone_number)
    
    abook.addContact(c1)
    pprint(c1)

def deleteContacts():
    contactID = input('Enter contact ID which you want delete (type "all" to clear address book):\n')
    
    if contactID == 'all':
        confirmation = input('You want to delete ALL contacts. Are you sure? (y/N)')
        if confirmation == 'y' or confirmation == 'Y':
            abook.deleteAll()
    else:
        

while is_running:
    option = input('''Select option:
    a - add new contact
    d - delete contact
    p - print all contacts
    q - quit
''')
    
    if option == 'p':
        abook.print()
        repr(abook)
    elif option == 'a':
        addContact()
    elif option == 'd':
        deleteContacts()
    elif option == 'q':
        is_running = False
        
    print('----------------------------------\n')



    