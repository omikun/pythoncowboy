#get initial contact
contact = p.get_contacts()
#try to unlock with contact authentication code
p.unlock(contact.data)
#print all contacts
while contact != None:
    print(str(contact.data))
    contact = contact.next
