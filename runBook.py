#!/usr/bin/python3.4

# Address book: add contacts, remove, save, print
import AddressBook, Contact
from AddressBook import AddressBook
from Contact import Contact


addressBookFile = 'contacts.pckl'

def addContact():
    valid_name = valid_phone = False
    while not valid_name or not valid_phone:
        if not valid_name:
            name = input('Enter name:')
            valid_name = AddressBook.validateName(name)
        elif not valid_phone:
            phone_number = input('Enter phone number:')
            valid_phone = AddressBook.validatePhone(phone_number)
    
    c1 = Contact(name)
    c1.addPhone(phone_number)
    abook.addContact(c1)

def deleteContacts():
    contact_id = input('Enter contact ID which you want delete (type "all" to clear address book):\n')
    
    if contact_id == 'all':
        if confirmDelete('ALL'):
            abook.deleteAll()
    else:
        contact = abook.getContactByID(contact_id)
        if contact and confirmDelete(contact.name):
            abook.deleteContactByID(contact_id)

def confirmDelete(name):
    confirmation = input('You want to delete {0} contact(s). Are you sure? (y/N)'.format(name))
    return confirmation == 'y' or confirmation == 'Y'


abook = AddressBook(addressBookFile)
is_running = True

while is_running:
    option = input('''Select option:
    a - add new contact
    d - delete contact
    p - print all contacts
    q - quit
''')
    
    if option == 'p':
        abook.print()
    elif option == 'a':
        addContact()
    elif option == 'd':
        deleteContacts()
    elif option == 'q':
        is_running = False
        
    print('----------------------------------\n')



    