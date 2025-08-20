#utility function used to print the phonebook
def printPhonebook(phonebook):
    for i in range(len(phonebook)):
        print("#",i,"\t",sep="", end = '') ,
        print(phonebook[i][0],phonebook[i][1],phonebook[i][2], sep=",\t")

#Function used to upload data from text file
def loadFile(phonebook):
    with open("input.txt","r") as file:
        #read one line at a time
        for line in file.readlines(): 
            #separator used to determine where string ends
            #this is done so we can use space to separate names and addresses
            values = line.split(", ")
            #on each line there are 3 values: name, address and phone number
            addUser(phonebook, values[0], values[1], values[2])
     #since we no longer need the file, we should close it       
    file.close()
            
#Function used to upload the current phonebook to a text file          
def uploadFile(phonebook):
    f = open("output.txt", "w")
    #the same order will apply when uploading: name, address, phonenumber
    for i in range(len(phonebook)):
        f.write(phonebook[i][0])
        f.write(", ")
        f.write(phonebook[i][1])
        f.write(", ")
        f.write(phonebook[i][2])
        #f.write('\r')
    f.close()
        
#searched for a user after name and address using binary search
def searchUser(phonebook, name, address):
    #first we have to concatenate the name and address into the same string
    searchedString = name + address
    start = 0 #starting index of first half
    end = len(phonebook) - 1  #"ending" index of second half
    mid = 0 #index of the middle of the "array"
    
    #while we can still divide the "array"
    while start <= end:
        
        #update index of middle
        mid = (start + end) // 2
        #concatenate the values we want to compare
        currentString = phonebook[mid][0] + phonebook[mid][1]
        #check is values are present at mid
        if currentString < searchedString:
            start = mid + 1

        #if name is "smaller", ignore right half
        elif searchedString< currentString:
            end = mid -1

        #if name is "bigger", ignore left half
        else:
            return mid
            
    #If we reach here, then the element was not present
    return -1

#returns the position of a user if it exists, or where we should insert it if it is
#not present in the current list. The function acts as an auxiliary function when we
#want to insert a new element in the list.
def searchInsert(phonebook, name, address, phone):
    n = len(phonebook)
    #base case
    if n < 1:
        return 0
    
    start = 0 #starting index of first half
    end = n-1 #"ending" index of second half
    #concatate all elements of user, since we have to search if all are present
    searchString = name + address + phone
    
    #while we can still divide the sequence
    while start <= end:
        #update middle
        mid = (start+end)//2
        #concatenate the values we want to compare
        currentString = phonebook[mid][0] + phonebook[mid][1] + phonebook[mid][2]
        #if elements are present in the middle
        if currentString == searchString:
            return mid
        #if name is "bigger", ignore right half and retain position
        elif currentString > searchString:
            end = mid - 1
            position = mid
        else:
        #if name is "smaller", ignore right half
            start = mid + 1
            position = mid + 1
            

    return position
  
#we add a new user, keeping the list ordered
def addUser(phonebook, newName, newAddress, newPhone):
    #first we need to know the position where we should insert an element
    #such that the list remains ordered after its insertion
    position = searchInsert(phonebook, newName, newAddress, newPhone)
    #user predefined function to insert at the given position
    #all elements after it are moved one positino to the right
    phonebook.insert(position, [newName, newAddress, newPhone])

#Remove a user from the list
def deleteUser(phonebook, name, address):
    #here we use the search function, as we can have 2 cases
    position = searchUser(phonebook, name, address)
    #first case, user does not exist
    #returns -1 so we know no used was deleted
    if position == -1:
        return position
    #second case, removes element from position and moves the others
    #one position to the left
    del phonebook[position]
    #returns 1 so we know the user was successfully deleted from the list
    return 1

 


    