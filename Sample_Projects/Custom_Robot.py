import pyttsx3 as ps
import pygame
import time
import os
pygame.init()
st = ps.init()
st.say("Hello!! Create a cool robot ahead:")
st.runAndWait()
class Robot:
        def __init__ (self,name,color,height,words):
                self.name = name
                self.color=color
                self.height = height
                self.words = words
        def speak(self):
                global myheight
                global mywords
                global mycolor
                global myname
                
                valid_color = False
                if myheight>=8:
                        st.say("Please enter a height that is less than 8 meters")
                        myheight = float(input("Please enter a robot height, in meters (please do not surpass eight meters):"))
                elif myheight<=0:
                        st.say("Please enter a valid height")
                        myheight = float(input("Please enter a robot height, in meters (please do not surpass eight meters):"))
                mycol2 = (255,255,255)
                mycol1 = (100,200,180)
                mycol3 = (19,160,150)
                mycol4 = (100,200,60)
                mycol5 = (150,250,230)
                if mycolor =='yellow' or mycolor =="Yellow":
                        mycol1 = (255,255,0)
                        mycol3 = (255,0,170)
                        mycol4 = (255,0,0)
                        mycol5 = (255,255,50)
                        valid_color = True
                if mycolor =='green' or mycolor =="Green":
                        mycol1 = (10,255,10)
                        mycol3 = (255,0,255)
                        mycol4 = (255,255,10)
                        mycol5 = (60,255,60)
                        valid_color = True
                if mycolor == 'red' or mycolor =="Red":
                        mycol1 = (255,10,10)
                        mycol3 = (10,30,255)
                        mycol4 = (30,255,20)
                        mycol5 = (255,60,60)
                        valid_color = True
                if mycolor == 'blue' or mycolor =="Blue":
                        mycol1 = (25,10,255)
                        mycol3 = (255,30,20)
                        mycol4 = (150,150,20)
                        mycol5 = (75,60,255)
                        valid_color = True
                if mycolor == 'purple' or mycolor =="Purple":
                        mycol1 = (100,80,160)
                        mycol3 = (255,230,10)
                        mycol4 = (30,30,200)
                        mycol5 = (150,130,210)
                        valid_color = True

                height = float(myheight*3)
                                
                
                ##Function Content:
                
                screen = pygame.display.set_mode((800,800))
                pygame.display.set_caption("Robot Screen")
                screen.fill((255,255,255))
                
                ##
                pygame.draw.rect(screen,mycol1,(330,500,70+height,20+height))
                pygame.draw.rect(screen,mycol1,(450,500,70+height,20+height))
                pygame.draw.rect(screen,mycol1,(350,500,50+height,-150+height))
                pygame.draw.rect(screen,mycol1,(470,500,50+height,-150+height))
                pygame.draw.rect(screen,mycol1,(350,400,170+height,-300+height))
                pygame.draw.rect(screen,mycol2,(385,170,35+height,35+height))
                pygame.draw.rect(screen,mycol2,(385,110,30+height,30+height))
                pygame.draw.rect(screen,mycol2,(460,110,30+height,30+height))
                pygame.draw.rect(screen,mycol3,(350,400,170+height,-180+height))
                pygame.draw.rect(screen,mycol4,(520,220,30+height,130+height))
                pygame.display.flip()
                st.say("Hello, master! My name is "+myname+" and I am "+str(myheight)+" meters tall! It is a pleasure to meet you!")
                st.runAndWait()
                if valid_color ==True:
                        st.say("You just created me.  A  "+mycolor+' robot.')
                        st.runAndWait()
                else:
                        st.say("You did not enter a valid robot color, so I just chose my own color. Haha")
                        st.runAndWait()
                st.say("HA HA HA. My creator wanted me to say the following words:   ...."+mywords)
                st.runAndWait()
                game_on=True
                #Play again button
                mousecol = mycol1
                pygame.draw.rect(screen,mousecol,(350,600,80,20))
                pygame.display.flip()

                def drawbut():
                        #Draw Button
                        pygame.draw.rect(screen,mousecol,(310,580,270,60))
                        
                        #Button text
                        gametext1 = pygame.font.SysFont("havetica",60) 
                        g_text2 = gametext1.render("Play Again", True , mycol3)
                        screen.blit(g_text2, (330,590))
                        #Speeech Bubble
                        pygame.draw.ellipse(screen,mycol5,(80,35,50+len(myname)*20,80))
                        #Robot Name
                        g_text2 = gametext1.render(myname, True , mycol3)
                        screen.blit(g_text2, (100,55))
                        
                        pygame.display.flip()
                        
                
                while game_on:
                        
                        
                        for event in pygame.event.get():
                                drawbut()
                                mymouse = pygame.mouse.get_pos()
                                if 350<mymouse[0]<650 and 600<mymouse[1]<660:
                                        mousecol = (mycol5)
                                        if event.type==pygame.MOUSEBUTTONDOWN:
                                               os.startfile("Custom_Robot.py")
                                               game_on = False
                                               pygame.quit()
                                else:
                                        mousecol = mycol1
                                



                pygame.display.update()
                
                while game_on:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        game_on = False
                                        pygame.quit()
                
                                        
myname = str(input("Please enter a name for your robot:"))
mycolor = str(input("Please enter a color for your robot (green,red,blue,yellow or purple):"))
myheight = float(input("Please enter a robot height, in meters (please do not surpass eight meters):"))
mywords = str(input("Please tell your robot what it needs to say:"))
mybot = Robot(myname,mycolor,myheight,mywords)
mybot.speak()
