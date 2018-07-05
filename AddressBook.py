#import Contact
import pickle
import random
import re

class AddressBook:
    size = 0
    contacts = []
    
    def __init__(self, filename):
        self.dbfile = filename
        self.contacts = []
    
    def __readContacts(self):
        with open(self.dbfile, 'rb') as db:
            try:
                self.contacts = pickle.load(db)
                self.size = len(self.contacts)
            except EOFError:
                print('Can\'t find any contact')
                
    def __saveContacts(self):
        with open(self.dbfile,'wb') as db:
            pickle.dump(self.contacts,db,0)
    
    def __generateContactID(self):
        if self.size < 1:
            return 1
        
        last_id = self.contacts[-1].contact_id
        return last_id + 1
    
    def addContact(self, contact):
        contact.setID(self.__generateContactID())
        self.contacts.append(contact)
        self.__saveContacts()
    
    def getContactByID(self, contact_id):
        for contact in  self.contacts:
            if contact.contact_id == int(contact_id):
                return contact
        return False
    
    def deleteContactByID(self, contact_id):
        for index, contact in  enumerate(self.contacts):
            if contact.contact_id == int(contact_id):
                del self.contacts[index]
                self.__saveContacts()
                return True
        return False
    
    def deleteAll(self):
        self.contacts = []
        self.__saveContacts()
    
    def print(self):
        self.__readContacts()
        print("You have ", self.size, " contacts in your Address book")
        
        print("ID\t|\tName\t|\tPhones\n-------------------------------------|")
        for c in self.contacts:
            print(c.contact_id,"\t|\t",c.name,"\t|\t",'; '.join(c.phones),"|")
    
    def validateName(name):
        return re.match('^[ .0-9a-zA-Z()]+$',name)
    
    def validatePhone(phone):
        return re.match('^\+?[- 0-9]+',phone)
