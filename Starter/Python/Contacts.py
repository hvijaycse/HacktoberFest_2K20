class Contacts():

	def __init__(self, last_name, first_name, email):


		self.last_name = last_name
		self.first_name = first_name
		self.email = email

	def getContact(self):
		return self.last_name.first_name.email

	def addContact():
		contact = input("Enter contacts: ")
		contact_instance = Contacts(contact)
		return contact_instance

	def main():

	    mycontacts = []   #create a list

	    while True:
	        print("""
	        Program Options.
	        1.) Display all contacts
	        2.) Create new contact
	        3.) Save and exit
	        """)

	        opt = input("Enter 1, 2, or 3: ")

	        if opt == "1":
	            printContacts(mycontacts)

	        elif opt == "2":
	            contact = addContact()
	            mycontacts.append(contact)

	        elif opt == "3":
	            pass
	        else:
	            print("That is not a valid entry.")

	if __name__ == '__main__':
    		main()

		
