from functions import addUser, searchUser, printPhonebook, deleteUser, loadFile,uploadFile

phonebook = []

def main():
    print("0. Exit")
    print("1. Load phonebook from file")
    print("2. Add new user to phonebook")
    print("3. Search for user by name and address")
    print("4. Delete user from list")
    print("5. Upload current phonebook to file")
    print("6. Print phonebook")
    
    while 1 > 0:
        option = int( input("Enter option:") )
        if option == 1:
            one()
        elif option == 2 and not phonebook:
            print("List is empty. You have to load it first. \n")
        elif option == 2:
            two()
        elif option == 3 and not phonebook:
            print("List is empty. You have to load it first. \n")
        elif option == 3:
             three()
        elif option == 4 and not phonebook:
            print("List is empty. You have to load it first. \n")
        elif option == 4:
             four()
        elif option == 5 and not phonebook:
            print("List is empty. You have to load it first. \n")
        elif option == 5:
             five()
        elif option == 6:
              six()
        elif option == 0:
              break
      
            
#Load Phonebook
def one():
    loadFile(phonebook)
    print("Phonebook was successfully loaded from file.")
    
#2 Add a new user
def two():
    #Here we have 4 test cases:
        #a) the inserted user is at the begining of the list:
    newName1 = "Alouis Pietr"     
    newAddress1 = "1516  Tavern Place"
    newPhone1 = "318-304-8215"
    newPhone1 += "\n"
    addUser(phonebook, newName1, newAddress1, newPhone1)    
    print("User",newName1,"was successfully added to the phonebook")    
    
        #b) the inserted user is in the middle of the list:
    newName2 = "Gordon Richard"     
    newAddress2 = "1141  American Drive"
    newPhone2 = "212-891-5203"
    newPhone2 += "\n"
    addUser(phonebook, newName2, newAddress2, newPhone2)  
    print("User",newName2,"was successfully added to the phonebook") 
    
        #c) the inserted user is at the end of the list:     
    newName3 = "Zayden John"     
    newAddress3 = "3812  Pearl Street"
    newPhone3 = "507-472-4991"
    newPhone3 += "\n"
    addUser(phonebook, newName3, newAddress3, newPhone3)
    print("User",newName3,"was successfully added to the phonebook") 
    
        #d) the inserted user has the same name as another user, but different address:
    newName4 = "Alouis Pietr"     
    newAddress4 = "1823  Grand Avenue"
    newPhone4 = "408-614-1263"
    newPhone4 += "\n"
    addUser(phonebook, newName4, newAddress4, newPhone4)
    print("User",newName4,"was successfully added to the phonebook") 
    
    
#3 Search a user by name and address
def three():
    #a) for a normal case:
    searchedName1 = "Valdez Pluto"
    searchedAddress1 = "2439  Arlington Avenue"
    result1 = searchUser(phonebook, searchedName1, searchedAddress1)
    if(result1 == -1):
         print("User",searchedName1, "not found in current list! \r")
    else:
        print("User",phonebook[result1][0], "was found at index:",result1)
        print("Phone:",phonebook[result1][2], "\r")
        
        #b)when 2 users have the same name, but different addresses
    searchedName2 = "Alouis Pietr"
    searchedAddress2 = "1823  Grand Avenue"
    result2 = searchUser(phonebook, searchedName2, searchedAddress2)
    if(result2 == -1):
        print("User",searchedName2, "not found in current list! \r\n")
    else:
        print("User",phonebook[result2][0], "was found at index:",result2)
        print("Phone:",phonebook[result2][2],"\r\n")

        #c) when the user is not in the current list:
    searchedName3 = "Susan Maxwell"
    searchedAddress3 = "3921  Pointe Lane"
    result3 = searchUser(phonebook, searchedName3, searchedAddress3)
    if(result3 == -1):
        print("User",searchedName3, "not found in current list! \r\n")
    else:
        print("User",phonebook[result3][0], "was found at index:",result2)
        print("Phone:",phonebook[result3][2],"\r\n") 
        
        
#4 Delete a user from the list
def four():
    #a) for a normal case:
    searchedName = "Gordon Richard"
    searchedAddress = "1141  American Drive"
    result1 = deleteUser(phonebook, searchedName, searchedAddress)
    if(result1 == -1):
        print("User",searchedName, "not found in current list! \r\n")
    else:
         print("User",searchedName, "was successfully deleted from list! \r\n")     
      
        #b) when 2 users have the same name, but different addresses
    searchedName = "Alouis Pietr"
    searchedAddress = "1823  Grand Avenue"
    result2 = deleteUser(phonebook, searchedName, searchedAddress)
    if(result2 == -1):
        print("User",searchedName, "not found in current list! \r\n")
    else:
         print("User",searchedName, "was successfully deleted from list! \r\n") 
         
        #c) when the user is not in the current list:
    searchedName = "John Gonzalez"
    searchedAddress = "4230  Maloy Court"
    result3 = deleteUser(phonebook, searchedName, searchedAddress)
    if(result3 == -1):
        print("User",searchedName, "not found in current list! \r\n")
    else:
         print("User",searchedName, "was successfully deleted from list! \r\n") 
         
         
#5 Upload data to .txt file
def five():
    uploadFile(phonebook)  
    print("Phonebook was successfully uploaded! \r")    
    

def six():
     if not phonebook:
         print("Phonebook is empty")
     else:
        print("*********************Phonebook******************************")
        printPhonebook(phonebook)
        print("************************************************************")

main()