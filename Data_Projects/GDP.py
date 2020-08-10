#note: Program built in February 2020. For this reason, data only goes up to 2024 projections.
# Data source: Wikipedia
import kivy, requests, re, os, ctypes
import numpy as np
kivy.require('1.8.0') 
from kivy.config import Config
#Changing app logo
Config.set('kivy','window_icon','wrld.png')
Config.set('graphics', 'resizable','0')
Config.set('graphics','fullscreen','0')
Config.set('graphics','boarderless',True)
Config.set('graphics', 'height','450')
Config.set('graphics', 'width','800')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.uix.label import Label
from kivy.core.text import FontContextManager
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import matplotlib.pyplot as plt
from matplotlib import style
import bs4 as bs
style.use('dark_background')

k=0
v = ''
c_listy =[]
c_list = []
c_data=[]
c_years = []

def get_countries():
    global k, c_list, c_data, c_years
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_GDP_(nominal)')
    soup = bs.BeautifulSoup(resp.text,'lxml')
    for text in soup.find_all('tr'):
        #Getting years of data
        try:
            c_year = text.find_all('th')
            c_year = [ele.text.strip() for ele in c_year][1:]
            if len(c_year)!=0:
                c_years.append(c_year)  
        except:
            pass

        #Getting Country Names
        try:
            c_name = text.td.a.text
            #Fixing name repetitions
            if c_name =='Cabo Verde':
                    c_name = 'Cape Verde'
            if c_name =='Republic of Congo':
                c_name = 'Republic of the Congo'
            if c_name =="Côte d'Ivoire":
                c_name = 'Ivory Coast'
            if c_name =="Korea, South":
                c_name = 'South Korea'
            if c_name =="Micronesia":
                c_name = 'Federated States of Micronesia'
            if c_name =="Swaziland":
                c_name = 'Ewatini'
            
            if c_name!='None':
                if c_name in c_list:
                    #Adding numbers next to repeated names to sort them later
                    c_list.append(c_name+str([line.rstrip(line[-1]) for line in c_list].count(c_name)+1))
                else:
                    c_list.append(c_name)
                    c_listy.append(c_name)
        except:
            pass
        
        #Getting Country Data
        try:
            c_GDP = text.find_all('td')
            c_GDP = [ele.text.strip() for ele in c_GDP][1:]
            c_GDP = [line.replace(',','') for line in c_GDP]
            c_data.append(c_GDP)
        except:
            pass

    #Removing additional information that isn't country-related from lists
    del c_list[-9:]
    del c_listy[-9:]
    c_data.pop(0)

    for element in c_years:
        try:
            if type([int(wrd) for wrd in element])==list:
                pass
        except:
            del c_years[c_years.index(element):]
    #Removing blank elements
    for element in c_data:
        elt = c_data.index(element)
        if 0 not in [len(el) for el in element]:
            try:
                if type([int(nbr) for nbr in element])==list:
                    pass
            except:
                del c_data[elt-1:]
                break
        if len(element)==0:
            c_data.remove(element)
    #Sorting out data so that there's an accurate correspondence between c_list's indexes and c_data's
    c_data = [x for _,x in sorted(zip(c_list,c_data))]
    c_list=sorted(c_list)

#Checking for existing file and, if false, creating new ones to store data gathered from Wikipedia
def ch_file(pat,lis):
    with open(pat+'.txt', 'r') as myfile:
        filecontent = myfile.readlines()
        lis.append([line for line in filecontent])

def cr_file(pat,lis):
    with open(pat+'.txt', 'w') as myfile:
        myfile.writelines("%s\n" % i for i in lis) 

if os.path.exists('c_GDP.csv') and os.path.exists('c_list.csv') and os.path.exists('c_listy.csv'):
    ch_file('c_GDP',c_data)
    ch_file('c_list',c_list)
    ch_file('c_listy',c_listy)

else:
    get_countries()
    #Turning incomplete data into int-readable lists so that
    #incomplete data can be plotted, with the exception of empty lists
    for l in c_data:
        o = c_data.index(l)
        l = np.array(l)
        indices = [i for i, x in enumerate(l) if len(x)==0]
        if len(indices)<10:
            l[indices] = '0'
            c_data[o] = list(l)

    #Cleaning up c_listy name repetitions
    bol = False
    for el in c_listy:
        indx = c_listy.index(el)
        if el =='Cabo Verde':
            el = 'Cape Verde'
            bol = True
        if el =='Republic of Congo':
            el = 'Republic of the Congo'
            bol = True
        if el =="Côte d'Ivoire":
            el = 'Ivory Coast'
            bol = True
        if el =="Korea, South":
            el = 'South Korea'
            bol = True
        if el =="Micronesia":
            el = 'Federated States of Micronesia'
            bol = True
        if el =="Swaziland":
            el = 'Ewatini'
            bol = True
        if bol:
            c_listy[indx] = el

    cr_file('c_GDP',c_data)
    cr_file('c_list',c_list)
    cr_file('c_listy',c_listy)

#Visual Aspect

class MyManager(ScreenManager):
    pass

class M_Page(Screen):
    myinput = ObjectProperty(None)
    mybut = ObjectProperty(None)
    class SearchWindow(Widget):
        class SearchWindow(Widget):
             #Making program run "Submit" function whenever user presses enter
            def __init__(self,**kwargs):
                super(M_Page.SearchWindow.SearchWindow,self).__init__(**kwargs)
                self._keyboard = Window.request_keyboard(self.my_keyboard_close, self)
                self._keyboard.bind(on_key_up=self.my_keyboard)
            def my_keyboard_close(self):
                self._keyboard.unbind(on_key_down = self.my_keyboard)
                self._keyboard = None
            def my_keyboard(self,keyboard, keycode,*args):
                global k
                if keycode[1]=='enter':
                    if k<2:
                        k+=1
                    else:
                        self.submit()
                        k=0
            def submit(self):
                global c_list, c_listy,v
                #Capitalizing adequate letters, Removing Spaces to fit data gathered
                chosen_country = str(self.myinput.text.title().replace(' ',''))
                c_list = [f.replace(' ','') for f in c_list]
                c_listy = [f.replace(' ','') for f in c_listy]
                if chosen_country in c_listy:
                #Country Found  - Move Page Left
                    v = chosen_country
                    words = re.findall('[A-Z][a-z]*', v)
                    Page.Wind.Wind.c = ''
                    for word in words: 
                        Page.Wind.Wind.c+=(word+' ')
                    kivy_file.current = "Page"
                    kivy_file.transition.direction = "left"
                    print(Page().ids.lbl.text)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "No data found for "+chosen_country, "Error",0)

class Page(Screen):
    class Wind(Widget):
        class Wind(Widget):
            c = StringProperty('Country')
            global v, c_data, c_list
            def __init__(self,**kwargs):
                super(Page.Wind.Wind,self).__init__(**kwargs)
            def d(self,years,index,nb,col,c,Prj):
                try:
                    l = c_data[c_list.index(v+str(nb))]
                    if 0 in [len(k) for k in l]: 
                        plt.title(Page.Wind.Wind.c+' '+years+' (Incomplete) GDP Data '+Prj)
                    else:
                        plt.title(Page.Wind.Wind.c+' '+years+' GDP Data '+Prj)
                    plt.scatter(c_years[index], [int(i) for i in l],c=c,s=15)
                    gr = plt.plot(c_years[index],[int(i) for i in l],color=col,linewidth=2)
                    plt.ylabel('Millions of USD')
                    plt.xlabel('Year')
                    plt.show()
                except:
                    ctypes.windll.user32.MessageBoxW(0, "No data found for "+Page.Wind.Wind.c+"during these years.", "Error",0)
            def tr(self):
                kivy_file.current = "M_Page"
                kivy_file.transition.direction = "right"

######################################################
kivy_file = Builder.load_file("GDP.kv")
class GDPApp(App):
    def build(self):
        return kivy_file

if __name__ =="__main__":
    GDPApp().run()
