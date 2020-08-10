import pandas as pd
import bs4 as bs
import requests, os, csv
import matplotlib.pyplot as plt
from matplotlib import style

#Data source: New York Times (license and README of data source provided.)

#Get data 
covid_data = pd.read_csv('us-states.csv')
style.use('ggplot')
s_list=list()
us_states = list()
for usstate in covid_data['state']:
    if usstate not in s_list:
        s_list.append(usstate)

#Reading file, if existent
def r_file(way):
    global us_states
    with open(way+'.csv', 'r') as myfile:
        filecontent = csv.reader(myfile)
        us_states.append([line[:] for line in filecontent])
    #Removing blank spaces
    us_states = us_states[0]
    j_help = 0
    for element in us_states:
        if len(element) ==0:
            del us_states[j_help]
        j_help+=1
    func(c=False, an=False)

#Saving tickers, if file doesn't exist
def save_tickers():
    global s_list, us_states

    if os.path.exists('us_val_states.csv'):
        r_file('us_val_states')

    else:
        resp = requests.get('https://www.bls.gov/news.release/laus.t01.htm')
        soup = bs.BeautifulSoup(resp.text,'lxml')
        m_divs = soup.find_all('tr')
        s_divs = soup.find_all('span',{'class':'datavalue'})
        val_list = list()
        
        for el in s_divs:
            try:
                val_list.append(el.text)
            except:
                pass

        # 1st clean - Removing irrelevant unemployed data
        o = 0
        m_lim = ((len(val_list)/12)*6)-6
        while o<=m_lim:
            del val_list[0+o:5+o], val_list[3+o]
            o+=6

        # 2nd clean - Removing non-US states
        num = 0
        indx = 0
        for el in m_divs:
            if len(el)!=0:
                try:
                    #Delete data irrelevant to US states
                    indx+=1
                    if el.th.p.text not in s_list:
                        num+=1
                        if num==1:
                            start_val = (indx-4) * 6
                        else:
                            start_val = ((indx-3-num)*6)
                            
                        del val_list[start_val : start_val+6]

                    #Combining state names and values
                    else:
                        us_states.append(el.th.p.text)
                        if num==0:
                            us_states.append(val_list[(indx-4) * 6 :((indx-4) * 6)+6])
                        else:
                            us_states.append(val_list[((indx-4-num)*6) :((indx-4-num)*6)+6])
                except:
                    pass
           
        # 3d clean - Adjustments
        temp_list = list()
        p_val1 = 0
        p_val2 = 0
        while p_val1 <= len(us_states)-1:
            if p_val1 % 2 ==0:
                temp_list.append(us_states[p_val1])
                p_val1+=1
            elif p_val2<=5:
                temp_list.append(us_states[p_val1][p_val2])
                p_val2 +=1
            else:
                p_val2 = 0
                p_val1 +=1

        us_states = temp_list

        for data in us_states:
            ind = us_states.index(data)
            if ',' in data:
                m_temp = data.replace(',','')
                us_states[ind] = m_temp
                temp_num = m_temp
            else:
                temp_num = data
            try:
                if ind % 7 !=0 and float(temp_num)!=0:
                    pass
            except: 
                us_states[ind] = 0

        # Writing data to file
        m_dex = 0
        with open('us_val_states.csv', 'w') as n_file:
            w_csv = csv.writer(n_file)
            while m_dex <= len(us_states) - 7:
                w_csv.writerow(us_states[m_dex : m_dex+7])
                m_dex+=7
                
        r_file('us_val_states', us_states)

state = str()
#Dropping uninteresting rows
def func(c=False, an=False):
    global s_list, covid_data, us_states, state

    #Variables
    county_data = pd.read_csv('us-counties.csv')
    us_data = pd.read_csv('us.csv')
    USA_2020 = [5892, 5787, 7140]
    USA_UN = [3.6, 3.5, 4.4]
    if c==False and an==False:
        #Define state for which data will be analyzed
        state = input('Please enter the state name (or U.S.A for nationwide data): ')
        state1 = state.title().split()
        state=''
        for w in state1:
            state+=w
            if state1.index (w)!= len(state1)-1:
                state+= ' '
        if state in s_list:
            #Filtering the data to what we want
            n_data = covid_data.loc[covid_data['state']==state]        
            myb = False
            u = 0
            while u<=len(us_states)-1 and not myb:
                if us_states[u][0] == state:
                    myb = True
                u+=1
            if myb:          
                #COVID-19 data
                fig, (ax1, ax2, ax3) = plt.subplots(3,1, constrained_layout=True)
                fig.canvas.set_window_title(state)
                ax1.set_title('COVID-19 Data for '+state+' state', fontweight='bold')
                ax1.set_xlabel("Date")
                ax1.set_ylabel("Number of people")
                ax1.plot(n_data['date'],n_data['cases'], color='b', label='Cases')
                ax1.plot(n_data['date'],n_data['deaths'], color='r', label='Deaths')
                ax1.set_xticklabels(n_data['date'], rotation= 'vertical')
                ax1.legend(loc="upper left")

                #Unemployment Data
                ax2.set_title('2020 Unemployment Data for '+state+' state', fontweight='bold')
                ax2.set_xlabel("Month")
                ax2.set_ylabel("Number of people")
                ax2.bar(['January', 'February', 'March'],[int(lol) for lol in us_states[u-1][1  : 4]], color='g')
                plt.xticks(rotation='horizontal')

                ax3.set_title('2020 Percentage of Unemployment for '+state+' state', fontweight='bold')
                ax3.set_xlabel("Month")
                ax3.set_ylabel("Percentage of the population")
                ax3.plot(['January', 'February', 'March'],[float(lol) for lol in us_states[u-1][4 : 7]], color='y')
                
            else:
                fig, ax1 = plt.subplots(nrows=1, ncols=1)
                ax1.set_title('COVID-19 Data for '+state+' state', fontweight='bold')
                ax1.set_xlabel("Date")
                ax1.set_ylabel("Number of people")
                ax1.plot(n_data['date'],n_data['cases'], color='b', label='Cases')
                ax1.plot(n_data['date'],n_data['deaths'], color='r', label='Deaths')
                plt.xticks(rotation='vertical')
                ax1.legend(loc="upper left")
            plt.show()
            func(c=True, an=False)
            
        elif state=='USA' or state=='U.S.A' or state=='United States' or state=='United States of America' or state=='US' or state=='Usa' or state=='Us':
           
            #COVID-19 data
            fig, (axa, axb, axc) = plt.subplots(3,1, constrained_layout=True)
            fig.canvas.set_window_title('U.S.A')
            axa.set_title('COVID-19 Data for the United States', fontweight='bold')
            axa.set_xlabel("Date")
            axa.set_ylabel("Number of people")
            axa.plot(us_data['date'],us_data['cases'], color='b', label='Cases')
            axa.plot(us_data['date'],us_data['deaths'], color='r', label='Deaths')
            axa.set_xticklabels(us_data['date'], rotation= 'vertical')

            #Unemployment Data
            axb.set_title('2020 Unemployment Data for the United States', fontweight='bold')
            axb.set_xlabel("Month")
            axb.set_ylabel("Number of people, in 1000s")
            axb.bar(['January', 'February', 'March'],USA_2020, color='g')
            plt.xticks(rotation='horizontal')

            axc.set_title('2020 Percentage of Unemployment for the United States', fontweight='bold')
            axc.set_xlabel("Month")
            axc.set_ylabel("Percentage of the population")
            axc.plot(['January', 'February', 'March'],USA_UN, color='y')

            plt.show()
            
            func(c=True, an=False)
        else:
            print("Sorry! That isn't a valid U.S state!")
            func(c=False, an=False)

    elif c and not an:
        county = input('Specify the county name: ')
        county1 = county.title().split()
        county = county.title().replace(' ','')
        bol = False
        for count in county_data.loc[county_data['state']==state]['county']:
            count = count.title().replace(' ','')
            if count==county:
                bol = True
        if bol:
            county = ''
            for word in county1:
                county+=word
                if county1.index (word)!= len(county1)-1:
                    county+= ' '
            county = county.title()
            plt.figure(num=(county+' county, '+state))
            county_data1 = county_data.loc[(county_data['state']==state) & (county_data['county']==county)]
            plt.title('COVID-19 Data for '+state+'  '+county+' county', fontweight='bold')
            plt.xlabel("Date")
            plt.ylabel("Number of people")
            plt.plot(county_data1['date'],county_data1['cases'], color='g', label='Cases')
            plt.plot(county_data1['date'],county_data1['deaths'], color='purple', label='Deaths')
            plt.xticks(rotation='vertical')
            plt.legend(loc="upper left")
            plt.show()
            func(c=False, an=True)
        else:
            print("Sorry! That isn't a valid " +state+' county')
            func(c=False, an=True)
            
    elif not c and an:
        a = input('Would you like to try another county for this state? (y/n) ')
        if a=='y' or a=='Y' or a=='yes' or a=='Yes':
            func(c=True, an=False)
        elif a=='n' or a=='N' or a=='no' or a=='No':
            func(c=False, an=False)
        else:
            func(c=False, an=True)
                
    func(c=False, an=False)

save_tickers()

