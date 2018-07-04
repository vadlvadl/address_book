class Contact:
    phones = []
    
    def __init__(self,name):
        self.name = name
        self.phones = []
    
    def __str__(self):
        return self.name + ": " + '; '.join(self.phones)
    
    def setID(self, contact_id):
        self.contact_id = contact_id
    
    def addPhone(self, phone):
        self.phones.append(phone)