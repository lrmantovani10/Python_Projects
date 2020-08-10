''' 
Data sources: http://hdr.undp.org/en/data# (HDI)
World Bank Data - All the rest

Very simple ML Linear Regression Model using data values obtained. More accurate projections can
be obtained by utilizing the evolution of the parameters used to calculate HDI and their predictions. 
However, I found it difficult to obtain data containing such metrics 
for all the countries provided here.

'''
import math 
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from matplotlib.lines import Line2D
from sklearn.linear_model import Ridge as Reg

print('Welcome to the Human Development central!')
print('<Note:> Missing data have been removed from the graphs.')
df = pd.read_csv('Human Development/HDI.csv', skiprows = 1)
df = df.fillna(0)
hdi = 0
ig_data = pd.read_csv('Human Development/Income_Groups.csv')
ig_data = ig_data.fillna(0)
f_list = ['GNI', 'Government_GDP_Edu', 'HCI', 'Life_Expectancy', 'Literacy_Rate_Adult', 
'School_Enrollment_Primary_Gross', 'School_Enrollment_Primary_Net', 'School_Enrollment_Secondary_Gross',
'School_Enrollment_Secondary_Net', 'School_Enrollment_Tertiary'
]
df_list = [pd.read_csv('Human Development/'+element+'.csv', skiprows = 4).fillna(0) for element in f_list]
style.use('dark_background')

def cc_selection(m_c):
    if '(' in m_c and ')' in m_c:
        m_c = m_c[:m_c.index('(')]
    mc_list = m_c.split()
    if 'People' in m_c:
        s_c = ''
        for el in mc_list:
            if 'People' in el:
                end_index = mc_list.index(el)
        mc_list = mc_list[:end_index]
        for word in mc_list:
            s_c+=word
            if mc_list.index(word)!=len(mc_list)-1:
                s_c+=' '
        m_c = s_c
    if 'SAR' in m_c:
        s_c = ''
        mc_list = mc_list[:-2]
        for word in mc_list:
            s_c+=word
            if mc_list.index(word)!=len(mc_list)-1:
                s_c+=' '
        m_c = s_c
    return m_c
def categorize(metric):
    if 0.8<=metric<=1:
        category = "Very High"
    elif 0.7<=metric<0.8:
        category = "High"
    elif 0.55<=metric<0.7:
        category = "Medium"
    elif metric<0.55:
        category = "Low"
    else:
        category = 'Unrealistic HDI'

    return category

def graphy(dataframe, year, country, category, Metric, ccon, labs):
    global ig_data, hdi
    # Finding countries with similar metrics and graphing their data
    c_list = list()
    c_rank = list()
    i_list = list()
    caty = category.title()
    for yt in dataframe[year]:
        try:
            i_list.append(round(float(yt), 3))
        except:
            pass
    if Metric == 'HDI':
        d_lis = [cc_selection(item) for item in dataframe['Country']]
        cc_rank = Metric+' Rank ('+year+')'
        c_lis = list(dataframe[cc_rank])
    else:
        d_lis = [cc_selection(item) for item in dataframe['Country Name']]
        c_lis = []
        m_listy = [float(floaty) for floaty in  dataframe[year]]
        part_list = [float(floaty) for floaty in  dataframe[year]]
        part_list.sort(reverse=True)
        for yu in m_listy:
            c_lis.append(part_list.index(yu)+1)
        o_list = list(ig_data['IncomeGroup'])
    temp = -1
    if Metric == 'HCI' or Metric == 'HDI':
        for item in i_list:
            temp+=1
            try:
                c_name = d_lis[temp]
                c_pos = int(c_lis[temp])
                if country in c_name:
                    position = c_pos
                    metric = item
                if Metric == 'HDI':
                    if categorize(item) == category:
                        c_list.append([c_name,item])
                        c_rank.append([c_name,c_pos])
                elif Metric == 'HCI':
                    if o_list[temp] == category:
                        c_list.append([c_name,item])
                        c_rank.append([c_name,c_pos])

            except:
                pass
    else:
        ky = -1
        for item in d_lis:
            ky+=1
            tent = -1
            for ity in list(ig_data['TableName']):
                tent+=1
                if item in ity and o_list[tent]==category:
                    c_list.append([item,i_list[ky]])
                    c_rank.append([item,c_lis[ky]])
    # General Info
    try:
        if Metric == 'HDI':
            print(country+"'s "+year+' '+Metric+" is "+str(metric)+', which is in the '+caty+' category.')
        else:
            print(country+"'s "+year+' '+Metric+" is "+str(metric)+", considering that it's in the "+caty+' HCI category.')
        print('Position in the '+year+' '+Metric+' world ranking: '+str(position))
    except:
        if Metric != 'HDI':
            print("Could not calculate current "+Metric+" because it is not listed for "+year)
        else:
            pass
    h_list = list()
    d_list = list()
    variable = -1
    #Filtering
    if len(c_list)>0 and len(c_rank)>0:
        for item in c_list:
            variable+=1
            try:
                if item not in h_list and int(c_rank[variable][1])>=1 and float(item[1])>0:
                    h_list.append(item)
            except:
                pass
        country_names = [ky[0] for ky in h_list]
        for item in c_rank:
            try:
                if item not in d_list and int(item[1])>=1 and item[0] in country_names:
                    d_list.append(item)
            except:
                pass
    c_rank = d_list
    c_list = h_list
    if len(ccon)==0 and Metric == 'HDI':
        c_list.append([country, hdi])
    #Bar Colors
    col_lis = ['crimson', 'red', 'yellow', 'green', 'blue', 'cyan', 'indigo']
    rdcol = rd.choice(col_lis)
    c_list.sort(key = lambda x: x[0])
    c_rank.sort(key = lambda x: x[0])
    metrics = [float(item[1]) for item in c_list]
    names = [item[0] for item in c_list]
    colors = list()
    condition = True
    for element in names:
        if country not in element or not condition:
            colors.append(rdcol)
        elif condition:
            c2 = col_lis
            c2.pop(col_lis.index(rdcol))
            colors.append(rd.choice(c2))
            condition = False
    if len(c_list)!=0:
        print('Position of countries with the same '+Metric+' category in our data, '+year+':')
        for element in c_rank:
            k_indx = c_list[c_rank.index(element)]
            if k_indx[0] != country:
                p_metric = k_indx[1]
                print(element[0]+' ('+str(p_metric)+')'+': '+str(element[1]))
    if len(names) > 4 and len(ccon)>0:
        fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout = True)
        ax1.set_title('Countries in '+year+' categorized as '+caty+' and their '+Metric+ ' values')
        ax1.bar(names, metrics, color = colors)
        ax1.set_xlabel('Country')
        ax1.set_xticklabels(names,rotation='vertical')
        ax1.set_ylabel(labs)
        ax2.set_title(country+' '+Metric+' values between '+ccon[0][0]+' and '+ccon[0][-1])
        col2_list = ['lime','darkmagenta','navy','fuchsia','tomato','springgreen']
        col_choice = rd.choice(col2_list)
        col2_list.pop(col2_list.index(col_choice))
        col_choice2 = rd.choice(col2_list)
        col2_list.pop(col2_list.index(col_choice2))
        plt_col = rd.choice(col2_list)
        m_colors = list()
        for item in ccon[0]:
            if ccon[0].index(item)<(len(ccon[0])-10):
                m_colors.append(col_choice)
            else:
                m_colors.append(col_choice2)

        ax2.scatter(ccon[0], ccon[1], c = m_colors, zorder = 1)
        ax2.plot(ccon[0], ccon[1], c = plt_col, zorder = 0)
        ax2.set_xlabel('Year')
        ax2.set_xticklabels(ccon[0], rotation = 'vertical')
        ax2.set_ylabel(labs)
        legend_elements = [Line2D([0], [0], color=plt_col, label='Line of best fit'),
                           Line2D([0], [0], marker='o', color=col_choice, label='Past Values',markerfacecolor=col_choice),
                           Line2D([0], [0], marker='o', color=col_choice2, label='Predicted Values',markerfacecolor=col_choice2)]
        ax2.legend(handles=legend_elements, loc='upper left')
        fig.canvas.set_window_title(country+' '+Metric+' Data')

    elif len(names)>4:
        fig, ax1 = plt.subplots(1,1, constrained_layout = True)
        ax1.set_title('Countries in '+year+' with a '+caty+' '+Metric+' and their values')
        ax1.bar(names, metrics, color = colors)
        ax1.set_xlabel('Country')
        ax1.set_xticklabels(names,rotation='vertical')
        ax1.set_ylabel(labs)
        fig.canvas.set_window_title('Countries with a '+caty+' '+Metric+' and their values')
    elif len(ccon)>0:
        fig, ax1 = plt.subplots(1,1, constrained_layout = True)
        ax1.set_title(country+' '+Metric+' values between '+ccon[0][0]+' and '+ccon[0][-1])
        col2_list = ['lime','darkmagenta','navy','fuchsia','tomato','springgreen']
        col_choice = rd.choice(col2_list)
        col2_list.pop(col2_list.index(col_choice))
        col_choice2 = rd.choice(col2_list)
        col2_list.pop(col2_list.index(col_choice2))
        plt_col = rd.choice(col2_list)
        m_colors = list()
        for item in ccon[0]:
            if ccon[0].index(item)<(len(ccon[0])-10):
                m_colors.append(col_choice)
            else:
                m_colors.append(col_choice2)

        ax1.scatter(ccon[0], ccon[1], c = m_colors, zorder = 1)
        ax1.plot(ccon[0], ccon[1], c = plt_col, zorder = 0)
        ax1.set_xlabel('Year')
        ax1.set_xticklabels(ccon[0], rotation = 'vertical')
        ax1.set_ylabel(labs)
        legend_elements = [Line2D([0], [0], color=plt_col, label='Line of best fit'),
                           Line2D([0], [0], marker='o', color=col_choice, label='Past Values',markerfacecolor=col_choice),
                           Line2D([0], [0], marker='o', color=col_choice2, label='Predicted Values',markerfacecolor=col_choice2)]
        ax1.legend(handles=legend_elements, loc='upper left')
        fig.canvas.set_window_title(country+' '+Metric+' Data')
    try:
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()
    except:
        pass 

def ML_func(custom_listy, year1):
    reg = Reg()
    xo = np.array([int(t[0]) for t in custom_listy]).reshape(-1,1)
    yo = np.array([t[1] for t in custom_listy]).reshape(-1,1)
    reg.fit(xo, yo)
    for value in range(int(year1)+1, int(year1)+11):
        prediction = reg.predict(np.array(value).reshape(-1,1))
        custom_listy.append([str(value),prediction])
    years = [g[0] for g in custom_listy]
    d_values = [g[1] for g in custom_listy]
    return [years, d_values]

def Main():
    global df, ig_data, df_list, f_list, hdi
    f_year = [col for col in df.columns][-1]
    updated_year = [col for col in df_list[2]][-2]
    choice1 = input('Would you like to calculate an HDI of a fictional country or predict a future one for an existing nation? (1 = calculate, 2 = predict) ')
    if choice1 == '1':
        m_c = input('Enter country name: ').title()
        country_name = cc_selection(m_c)
        for country in df['Country']:
            if country_name in country:
                print('Already have data for that country. Please try again.')
                Main()
        for country in ig_data['TableName']:
            if country_name in country:
                print('Already have data for that country. Please try again.')
                Main()
        try:
            le = float(input('Enter the life expectancy, in years: '))
            lei = ((le - 20)/65)
            mys = float(input('Enter the mean years of schooling, in years: '))
            eys = float(input('Enter the expected years of schooling, in years: '))
            ei = ((mys/15)+(eys/18))/2
            gnipc = float(input('Enter the GNI per capita: '))
            ii = (math.log(gnipc) - math.log(100))/(math.log(750))
            hdi = (lei*ei*ii)**(1/3)
        except:
            print('Operation Failed. Please try again.')
            Main()
        try:
            category = categorize(float(hdi))
        except:
            category = 'Unrealistic HDI'
        print(country_name+"'s inserted HDI is "+str(round(hdi, 3))+', which is in the '+category.title()+' category.')
        graphy(df, f_year, country_name, category,'HDI', [], 'HDI (0-1)')
        Main()  

    elif choice1 == '2':
        m_c = input('Enter country name: ').title()
        country_name = cc_selection(m_c)
        list1 = list(df['Country'])
        list2 = list(ig_data['TableName'])
        positions = []
        con1 = False
        con2 = False
        for item in list1:
            if country_name in item:
                positions.append(list1.index(item))
                con1 = True
                break
        for item in list2:
            if country_name in item:
                positions.append(list2.index(item))
                con2 = True
                break
        try:
            country_name = cc_selection(list1[positions[0]])
        except:
            try:
                country_name = cc_selection(list2[positions[0]])
            except:
                print('Country not listed. Please try again.')
                Main()
        
        if con1:
            hdi = list(df[f_year])[positions[0]]
            category = categorize(float(hdi))
            hdis_lis = list()
            for element in list(df.columns)[2:]:
                try:
                    add2 = float(df[element][positions[0]])
                    hdis_lis.append([element, add2])
                except:
                    pass
            try:
                F_entry = ML_func(hdis_lis, f_year)
                appended = [[],[]]
                hkey = -1
                for tr in F_entry[1]:
                    hkey+=1
                    if tr != 0:
                        appended[0].append(F_entry[0][hkey])
                        appended[1].append(tr)
                F_entry = appended
                graphy(df, f_year, country_name, category,'HDI', F_entry, 'HDI (0-1)')
            except:
                print("Error calculating country HDI.")
                Main()
        else:
            print('Country HDI not listed.')
        if con2:
            try:
                country2 = list2[positions[1]]
            except:
                country2 = list2[positions[0]]
            hci = list(df_list[2][updated_year])[list(df_list[2]['Country Name']).index(country2)]
            hci = round(float(hci), 3)
            vindx = list(ig_data['TableName']).index(country2)
            income_group = list(ig_data['IncomeGroup'])[vindx]
            Table_Note = str(list(ig_data['SpecialNotes'])[vindx])
            if len(Table_Note)>1:
                print('<Note:> '+Table_Note)
            country2 = cc_selection(country2)
            try:
                graphy(df_list[2], updated_year, country2, income_group,'HCI', [], 'HCI (0-1)')
            except:
                print("Unable to calculate this country's HCI.")
                Main()
        else:
            print("Country's HCI or HCI Income Group is not listed")
        
        print('If you want to  view any of the following data, enter the number next to it. Enter 0 to exit.')
        coeff = 1
        eny = -1
        for entry in df_list:
            eny+=1
            if eny!=2:
                used = entry['Indicator Name'][0]
                print(used+': '+str(coeff))
                coeff+=1
        try:
            number_entered = int(input('Insert a number: '))
            if number_entered <3 and number_entered!=0:
                worked_df = df_list[number_entered -1]
            elif number_entered == 0:
                Main()
            else:
                worked_df = df_list[number_entered]
            desired_year = list(worked_df.columns)[-2]
            colus = list(worked_df.columns)
            timy = colus[(colus.index('Indicator Code')+1) : len(colus) -1]
            country_index = [cc_selection(ew) for ew in worked_df['Country Name']].index(country2)
            per_list = []
            perf_list = []
            for column in timy:
                per_list.append(worked_df[column][country_index])
            # Removing possible non numeric/0 values from data
            # after addition to be more organized.
            verified_list = []
            for e in per_list:
                try:
                    u_e = float(e)
                    if u_e!=0:
                        verified_list.append(u_e)
                except:
                    pass
            if len(verified_list) < 4:
                print("We don't have sufficient "+country2+" data on the parameter provided, so we'll try to share information about the country's region, alongside the country's HCI classification.")
                region_name = ig_data['Region'][list(ig_data['TableName']).index(country2)]
                fork = True
                possibilities = list()
                for itm in worked_df['Country Name']:
                    if region_name in itm:
                        possibilities.append(itm)
                if len(possibilities)>1:
                    print('The following regions were associated with the country entered. Enter the number associated with the one you would like to see data for.')
                    num = 0
                    for er in possibilities:
                        num+=1
                        print(er+' '+str(num))
                    try:
                        selection = int(input('Select a number: '))
                        region_index = list(worked_df['Country Name']).index(possibilities[selection-1])
                    except:
                        print('Invalid number entered. Please retry.')
                        Main()
                else:
                    region_index = list(worked_df['Country Name']).index(region_name)
                for b in timy:
                    try:
                        a_val = float(worked_df[b][region_index])
                        if a_val!=0:
                            perf_list.append([b, a_val])
                    except:
                        pass
                if len(perf_list)<2:
                    print('Insufficient data for the selected region. Please try again.')
                    Main()
            else:
                for b in timy:
                    try:
                        a_val = float(worked_df[b][country_index])
                        if a_val!=0:
                            perf_list.append([b, a_val])
                    except:
                        pass
                fork = False
            yaxis = ML_func(perf_list, desired_year)
            hhentry = worked_df['Indicator Name'][country_index]
            if '%' in hhentry and 'enrollment' in hhentry:
                ty = 'Enrollment(%)'
            elif 'expenditure' in hhentry:
                ty = '% of Total Expend.'
            elif 'Literacy' in hhentry:
                ty = 'Literacy Rate (%)'
            elif 'expectancy' in hhentry:
                ty = 'Years'
            else:
                ty = 'USD'

            if not fork:
                graphy(worked_df, desired_year, country2, income_group, hhentry, yaxis, ty)
                Main()
            else:
                graphy(worked_df, desired_year, region_name, income_group, hhentry, yaxis, ty)
                Main()
        except:
            print('Operation failed. Please try again.')
            Main()

    else:
        print('Operation failed. Please try again.')
        Main()


Main()