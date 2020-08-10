'''
Creates a bibliographical reference generator,
where a user enters his name and two second names, and the program
creates a bibliographical reference for the user.
'''
def runprogram():
        print("Welcome to the bibliographical reference generator! :)")
        name =str(input("Please enter your full name:"))
        county = name.count(" ")
        namesplit = name.split(" ",county)
        index = 1
        namy1 = ""
        while index<=(len(namesplit) - 2):        
        #I already know that this is true:index>=0:        
                        for character in namesplit[index]:                        
                                midy = namesplit[index]
                                if character == midy[0]:                        
                                        capital = character                              
                                        namy1+=(capital+".")
                                        printy = namy1.upper()
                                        index+=1

        if index==1:
                printy = ""               
        print((namesplit[len(namesplit)-1]).upper()+",",namesplit[0].title(),printy)
        print("To render another bibliographical reference,")
        runprogram()
runprogram()
