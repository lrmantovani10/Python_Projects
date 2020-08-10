import csv
print("Welcome to the Police Database!")
data_file_path = "Police_Database.csv"

def print_data():
    with open (data_file_path,'r',encoding = 'utf-8') as file:
        file_list = list()
        reader = csv.reader(file)
        for line in reader:
            if len(line)!=0:
                file_list.append(line)
        if len(file_list)==0:
            print("The document is currently empty. Enter criminal data to fill it.")
        else:
            print("Current database entries:")
            index1 = 0
            index2 = 0
            sum_value = 1
            while index1<=len(file_list)-1:
                print(' ')
                print("Criminal {} :".format(sum_value))
                while index2<=4:
                    print(file_list[index1][index2])
                    index2+=1
                index2=0
                index1+=1
                sum_value+=1
                print(' ')
    try:         
        name = str(input("Please enter the criminal's name:"))
        age = int(input("Please enter the criminal's age:"))
        Ethnicity = str(input("Please enter the criminal's ethnicity:"))
        Height = float(input("Please enter the criminal's height (in meters):"))
        Location_of_crime = str(input("Please enter the criminal's crime location:"))
        Crime_Dict = {'Name' : name, 'Age' : age, 'Ethnicity' : Ethnicity, 'Height (in m)' : Height, 'Crime Location' : Location_of_crime}
    except:
        print("An error occured while entering the criminal data. Please try again.")
        print_data()
    with open (data_file_path,'a',encoding = 'utf-8') as file:
        writer = csv.writer(file)
        try:
            entry_data = [(key+" : " + str(values)) for (key,values) in Crime_Dict.items()]
            writer.writerow(entry_data)
            file.close()
            file_list.append(entry_data)
        except:
            print("An error occured while writing on the file. Please try again")
            print_data()
            
        def Del_Choice():
            Del_Bol = str(input("Successfuly entered the criminal data. Would you like to delete any previous entries? (Type Y for Yes and N for No) "))
            if Del_Bol == 'Y' or Del_Bol =='Yes':
                try:
                    num_entry = int(input("Please enter the number of the entry you would like to delete. "))
                except:
                    print("Error identifying entered value. Please try again.")
                    Del_Choice()
                    
                with open (data_file_path,'w',encoding = 'utf-8') as file:
                    list_index = 0
                    writer = csv.writer(file)
                    for entry in file_list:
                        list_index +=1
                        if num_entry==list_index:
                            pass
                        else:
                            writer.writerow(entry)

            elif (Del_Bol == 'N') or (Del_Bol =='No'):
                print("No previous entries were deleted.")
                print_data()
            else:
                print("You did not answer the question properly. Please try again.")
                Del_Choice()
        Del_Choice()
        print_data()
        
#Running this function after the program starts
print_data()


