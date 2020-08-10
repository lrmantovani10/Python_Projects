import csv
import matplotlib as mpl
from matplotlib import pyplot as plt
from colorama import *
from datetime import date, datetime, timedelta
#Number of expense index
init(autoreset=False)
print(Style.BRIGHT+Fore.GREEN+"Welcome to your personal expenses manager. Add a number ahead, that corresponds to your latest expense, in USD, and its name. Type 'del' to delete an expense.")
m_list = list()
def execfunc():
    global m_list
    file_path = "Sample_Expenses.csv"
    mylist=[]
    m_list = list()
    s=0
    with open(file_path,'r',encoding='utf-8') as myfile:
        reader = csv.reader(myfile)
        print("Total Expenses:")
        for line in reader:
            if len(line)!=0:
                mylist.append(line)
                m_list.append(line[2:4])
        if len(mylist)==0:
            print("The document is still empty. type in your expenses to fill it.")
        else:
            for i in mylist:
                s+=1
                print("Expense "+str(s)+": "+str(i[0])+' - '+str(i[2])+'. Payment Date:'+str(i[3]))
    def v_func():
        global m_list
        v_func.value = input("Please enter a value ahead: (Enter 'Graph' to trace expenses over time) ")
        if v_func.value == 'Graph':
            #Sorting elements in tuple based on date sortage so that correct date-value correspondences are maintained
            m_list.sort(key=lambda mylist:(datetime.strptime(mylist[1], '%m/%d/%Y'),mylist[0]))
            date_list = []
            cash_list = []
            for element in m_list:
                date_list.append(element[1])
                cash_list.append(element[0])
            #Cutting older/ahead of time(impossible to have already occured) expenses (we only want expenses over the last year)
            #For practical purposes and convenience, all months were assumed to be comprised of 30 days
            y_ago = datetime.now()-timedelta(days=365)
            now = datetime.now()
            k = 0
            del_list = []
            for itemx in date_list:
                itemd = int(itemx[0:2])+int(itemx[3:5])*(1/30)+int(itemx[6:])*12
                item_a = y_ago.year*12+y_ago.month+y_ago.day*(1/30)
                item_b = now.year*12+now.month+now.day*(1/30)
                if not item_a<=itemd<=item_b:
                    i = date_list.index(itemx)+k
                    del_list.append (i)
                    k-=1
            for element in del_list:
                date_list.pop(element)
                cash_list.pop(element)
            #Removing dollar signs
            for element in cash_list:
                cash_list[cash_list.index(element)] = float(element[1:])
            plt.figure(figsize=(10,6))
            ax = plt.axes()
            plt.rc('font',family='Arial',weight='bold', size='14')
            mpl.rcParams['lines.linewidth'] = 5
            mpl.rcParams['lines.linewidth'] = 5
            ax.set_facecolor("white")
            plt.title("Expenses over the last year",color = (1,0.2,0.2))
            plt.plot(date_list,cash_list, zorder=0)
            plt.scatter(date_list,cash_list, color = (1,0.2,0.2),s=100, zorder=1)
            plt.xlabel("Date", color = (1,0.2,0.2),size = 12)
            plt.ylabel("Value (USD)", color = (1,0.2,0.2),size=12)
            # Add this line if wanting to show the value of exactly all expenses made - plt.yticks([y for y in cash_list])
            plt.tight_layout()
            plt.grid(True)
            plt.style.use('ggplot')
            #Available styles - print(plt.style.available)
            plt.show()
            v_func()
        if v_func.value=='del':
            del_row = int(input("Enter the number of the expense you wish to delete (Enter '0' if you do not wish to delete anything, or -1 IF YOU WISH TO DELETE EVERYTHING.):"))
            deleterow(del_row,file_path,mylist)
        if len(v_func.value)==0:
            v_func()
    v_func()
    def n_func():
        n_func.expense_name = str(input("Please enter the name of the expense you just entered: "))
        if str(n_func.expense_name)=='del':
            del_row = int(input("Enter the number of the expense you wish to delete (Enter '0' if you do not wish to delete anything, or -1 IF YOU WISH TO DELETE EVERYTHING.):"))
            deleterow(del_row,file_path,mylist)
        if len(n_func.expense_name)==0:
            n_func()
    n_func()
    def exp_date():
        exp_date.expense_date = input("Please enter the expense date, in the MM/DD/YYYY format. Type 'Today' for the current date. ")
        exp_date.expense_date.strip()
        if str(exp_date.expense_date)=='Today':
            exp_date.expense_date= date.today().strftime('%m/%d/%Y')
        if str(exp_date.expense_date)=='del':
            del_row = int(input("Enter the number of the expense you wish to delete (Enter '0' if you do not wish to delete anything, or -1 IF YOU WISH TO DELETE EVERYTHING.):"))
            deleterow(del_row,file_path,mylist)
        if len(exp_date.expense_date)==0:
            exp_date()
    exp_date()
        
        

    with open(file_path,'a',encoding='utf-8') as myfile:
        writer = csv.writer(myfile)
        writer.writerow([n_func.expense_name,' ('+'Expense'+str(len(mylist)+1)+')','$'+str(int(v_func.value)),exp_date.expense_date])
        myfile.close()
    execfunc()

def deleterow(del_row,file_path,mylist):
    if del_row==(-1):
            with open(file_path,'w') as out:
                pass
            
    if 0<=del_row<=len(mylist) and del_row!=0:
        with open(file_path,'w') as out:
            pass
        addition=0
        for element in mylist:
            if mylist.index(element)!=del_row-1:
                addition+=1
                with open(file_path,'a',encoding='utf-8') as overwrite_file:
                    writer = csv.writer(overwrite_file)
                    writer.writerow([element[0],' ('+'Expense'+str(addition)+')',element[2],element[3]])
    elif del_row!=0:
        print("Row number out of range. Please try again.")
        execfunc()
        
    else:
        execfunc()
    execfunc()
    

execfunc()
    
        
