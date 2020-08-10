'''
Same mechanism as creating files for people at a dental office, for example.
Utilizes classes and OOP (Object-Oriented Programming)
'''
class Person:
    def __init__(self,name,ethnicity,sex,age):
        self.name = name
        self.age = age
        self.ethnicity = ethnicity
        self.sex = sex
        self.age = age
        self.u = [self.name,self.ethnicity,self.sex,self.age]
    def filedata(self):        
        for element in self.u:
            D = dict(Name=self.name,Ethnicity=self.ethnicity,Sex=self.sex,Age=self.age)
            return D
            break
        
database1 = []

def entername():
    global database1
    name = str(input("Please enter your name:"))
    ethnicity= str(input("Please enter your ethnicity: "))
    sex = str(input("Please enter your sex: "))
    age = int(input("Please enter your age: "))
    person1 = Person(name,ethnicity,sex,age)
    person1_exec = person1.filedata()
    office_list = []
    additional_entries = 0
    index=0
    index1=0
    index2=0
    temp=0   
    addy=True
    addy1=False
    list1=[]
    for keys,values in person1_exec.items():
        office_list.append([keys,values])
    #Everything OK till here
    while temp == 0:
        for name in office_list[index]:            
            list1.append(name)
        index+=1
        if len(list1)==8:
            break
        
    while temp == 0:
        if addy == addy1:
            addy=True
            pass
        else:
            print(list1[index1]+":",list1[index1+1])
            addy = False
            
           
        if index1==(len(list1)-2):
            database1.append(list1)
            print("______________________")
            print("Stored entries in the datbase:")
            break
       
        index1+=1
    for element in database1:
        print(element[0]+":",element[1])
        print(element[2]+":",element[3])
        print(element[4]+":",element[5])
        print(element[6]+":",element[7])

        print("                      ")
    print("________________________")   
    entername()
            
entername()
