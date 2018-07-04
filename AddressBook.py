#import Contact
import pickle
import random

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
        #return round(random.random() * 1000000)
        self.size += 1
        return self.size
    
    def addContact(self, contact):
        contact.setID(self.__generateContactID())
        self.contacts.append(contact)
        self.__saveContacts()
    
    def getContactByID(self, contact_id):
        for contact in  self.contacts:
            if contact.contact_id == contact_id:
                return contact
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

