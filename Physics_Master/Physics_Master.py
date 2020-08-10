import pygame
import math
import time
import random
pygame.init()
#Screen Conditioning
Icon = pygame.image.load("Pixel_Planet.png")
pygame.display.set_icon(Icon)
pygame.display.set_caption("Physics Master")
Int = True
Mec = False
Kin = False
F_M = False
Thermo = False
ElecMag = False
Waves = False
Atomic = False
#Movement
p_r = False
p_l = False
p_u = False
p_d = False
movex=0
movey = 0
#Planet Movement
a=0
p_y=300
#Monster Movement
monsterx = 0
#Ray Movement
shooting = False
#Colors
red = (255,45,30)
violet = (255,100,180)
green = (70,255,130)
yellow = (255,255,100)
blue = (100,130,255)
orange = (252,111,3)
purple = (240,3,252)
col2=(255,255,255)
#Screen
screen = pygame.display.set_mode((1000,1000))
#Images
beam = pygame.image.load('Beam.png')
zap = pygame.image.load('zap.png')
arrow = pygame.image.load('Left-Arrow.png')
ship = pygame.image.load('Spaceship.png')
g_Monster = pygame.image.load('Monster.png')
g_Monster2 = pygame.image.load('Monster2.png')
g_Monster3 = pygame.image.load('Monster3.png')
gMonster = pygame.image.load('M1.png')
gMonster2 = pygame.image.load('M2.png')
gMonster3 = pygame.image.load('M3.png')
Uni = pygame.image.load('P_Universe.png')
Mercury = pygame.image.load('P_Mercury.png')
Venus = pygame.image.load('P_Venus.png')
Earth = pygame.image.load('P_Earth.png')
Mars = pygame.image.load('P_Mars.png')
Jupiter = pygame.image.load('P_Jupiter.png')
Saturn = pygame.image.load('P_Saturn.png')
Neptune = pygame.image.load('P_Neptune.png')
Uranus = pygame.image.load('P_Uranus.png')
#Other Variables
points = 0
b_width = 280
b_height = 63
clock = pygame.time.Clock()
t1=38
t2 = 38
t=0
m_list = []
d_list = []
l_x = 0
jazz = pygame.mixer.music.load("Jazz.mp3")
l_sound = pygame.mixer.Sound("Laser.wav")
p_sound = pygame.mixer.Sound("Point.wav")
Wav = False
#Game Over
go = False
#Intervals
t_1 = 0
t_2 = 0
t_interval1 = 0
t_interval2 = 0
switch1 = False
switch2 = False
timer=0
t_tick=15
#Speeed
g_speed = 40
m_r = 20
m_l =m_r
u_speed = 20
#Activations
active1 = False
active2 = False
#Enemy spawn
class Monster:
    def __init__(self, monsterx,monstery,img,index):
        self.monsterx = monsterx
        self.monstery = monstery
        self.img = img
        self.index = index
    def move(self):
        global points,Thermo,F_M,col2,red,yellow,movey,movex,g_speed, l,beam,ship,g_Monster, switch1, switch2, t_interval1, t_interval2  
        screen.blit(self.img, (-200+self.monsterx,self.monstery))
        self.monsterx+=g_speed
        if self.monsterx>=1150:
            if Kin:
                g_speed=random.randint(5,25)
            self.monsterx=random.randint(-2000,-200)
            self.monstery = random.randint(400,600) 
    #Calling for impact - Monster-Beam
        #First laser
        if l.rend and (-200+self.monsterx<=450+m_list[len(m_list)-1]-(beam.get_rect().width)/2+(ship.get_rect().width)/2<=-200+self.monsterx+g_Monster.get_rect().width and -200+self.monsterx<=450+m_list[len(m_list)-1]+(beam.get_rect().width)/2+(ship.get_rect().width)/2<=-200+self.monsterx+g_Monster.get_rect().width) and (self.monstery<=l.l_y<=self.monstery+g_Monster.get_rect().height or self.monstery<=l.l_y+beam.get_rect().height<=self.monstery+g_Monster.get_rect().height): 
            l.l_y = 420
            if self.index==0:
                points+=10
                if ElecMag:
                    points+=20
            elif self.index==1:
                points+=5
                if ElecMag:
                    points+=10
            elif self.index==2:
                points-=60
                if ElecMag:
                    points-=50
                if points<=0:
                    points=0
            if Waves:
                pygame.mixer.Sound.play(p_sound)
            if Kin:
                g_speed=random.randint(5,25)
            if switch1 and t_interval1<=20:
                self.monsterx=random.randint(-300,-200)
            elif switch1:
                switch1 = False
                t_interval1 = 0
                self.monsterx = random.randint(-500,-400)
            else:
                switch1 = True
                self.monsterx = random.randint(-700,-600)
        #Second laser
        if l.rend and (-200+self.monsterx<=450+d_list[len(d_list)-1]-(beam.get_rect().width)/2+(ship.get_rect().width)/2<=-200+self.monsterx+g_Monster.get_rect().width and -200+self.monsterx<=450+d_list[len(d_list)-1]+(beam.get_rect().width)/2+(ship.get_rect().width)/2<=-200+self.monsterx+g_Monster.get_rect().width) and (self.monstery<=l.l_y<=self.monstery+g_Monster.get_rect().height or self.monstery<=l.l_y+beam.get_rect().height<=self.monstery+g_Monster.get_rect().height):
            l.l_2 = 420
            points+=10
            if Waves:
                pygame.mixer.Sound.play(p_sound)
            if ElecMag:
                points+=20
            if Kin:
                g_speed=random.randint(5,25)
            if switch2 and t_interval2<=20:
                self.monsterx= random.randint(-1000,-900)
            elif switch2:
                switch2 = False
                t_interval2 = 0
                self.monsterx =-200
            else:
                switch2 = True
                self.monsterx = random.randint(-900,-800)

        #Monster - Ship collision in case of Fluid Mechanics or Thermo (y-condition)
        if (F_M or Thermo) and (230+movey<=self.monstery<=230+movey+ship.get_rect().height or 230+movey<=self.monstery+g_Monster.get_rect().height<=230+movey+ship.get_rect().height) and (450+movex<=-200+self.monsterx<=450+movex+ship.get_rect().width or 450+movex<=-200+self.monsterx+g_Monster.get_rect().width<=450+movex+ship.get_rect().width):
            if F_M:
                ship = pygame.image.load('Spaceship_Damaged.png')
            else:
                ship = pygame.image.load('Spaceship_Damaged2.png')
                points-=10
                if points<=0:
                    points=0
        
monster1 = Monster(0,random.randint(370,600),g_Monster,0)
monster2 = Monster(0,random.randint(370,600),g_Monster2,1)
monster3 = Monster(0,random.randint(370,600),g_Monster3,2)
m1 = Monster(0,random.randint(370,600),gMonster,0)
m2 = Monster(0,random.randint(370,600),gMonster2,1)
m3 = Monster(0,random.randint(370,600),gMonster3,2)
#Laser Spawn
class Laser:
    beam_x = 20
    rend = False
    def __init__(self,l_y,l_2):
        self.l_y = l_y
        self.l_2 = l_2

#Laser Movement
    def move(self):
        if self.l_y==1120 or self.l_y==420:
            m_list.append(movex)

        elif (F_M or Thermo) and self.l_y == 230+movey+ship.get_rect().height:
            m_list.append(movex)

        if self.l_2 ==1120 or self.l_2==420:
            d_list.append(movex)
        elif (F_M or Thermo) and self.l_2 == 230+movey+ship.get_rect().height:
            d_list.append(movex) 

        if self.rend:
            screen.blit(beam,(450+m_list[len(m_list)-1]-(beam.get_rect().width)/2+((ship.get_rect().width)/2),self.l_y))
            if t==20:
                screen.blit(beam,(450+d_list[len(d_list)-1]-(beam.get_rect().width)/2+((ship.get_rect().width)/2),self.l_2))
                self.l_2+=40
            self.l_y+=40
        if self.l_y>=1000:
            m_list.append(movex)
            self.l_y=1120
            if shooting:
                if Waves:
                    pygame.mixer.Sound.play(l_sound)
                if not (F_M or Thermo):
                    self.l_y = 420
                else:
                    self.l_y = 230+movey+ship.get_rect().height
        if self.l_2>=1000:
            d_list.append(movex)
            self.l_2=1120
            if shooting:
                if not (F_M or Thermo):
                    self.l_2 = 420
                else:
                    self.l_2 = 230+movey+ship.get_rect().height

l = Laser(420,420)
#Drawing Buttons
def drawbutton(color,y_pos,i,txt):
        global screen,b_width,b_height,g_text2
        x_array = [250,740,490,230,670,300,700]
        x_start = x_array[i]
        if i>3:
            if i==6:
                b_width = 520
            else:
                b_width = 380
        else:
            b_width = 280
        pygame.draw.rect(screen,color,((x_start-(b_width)/2),y_pos,b_width,b_height))
        #Button Text
        b_text = g_text2.render(txt, True , (255,255,255))
        screen.blit(b_text,(((x_array[i]-(b_text.get_rect().width)/2)),y_pos+10))
def Rendfunc():
    global g_Monster,g_Monster2,g_Monster3,r_x,ship,Wav,beam,Uni,movey,points,m_r,m_l,timer,g_speed,col,violet,Mec,Kin,F_M,green,yellow,red,blue,orange,purple,Thermo,ElecMag,Waves,Atomic
    #Choice - specific layouts
    text =''
    if Mec:
        col = violet
        text = "When analyzing Mechanics, gravitational effects are considered"
        if timer>20:
            timer-=0.1
            g_speed-=0.4
        elif timer<0:
            timer+=0.1
            g_speed+=0.4

    elif not Kin:
        g_speed = 40
        m_r=30
        m_l=m_r

    if Kin:
        col = green
        text = "When analyzing Kinematics, monster speeds change"
    elif not Mec:
        g_speed = 40
    if F_M:
        col = yellow
        text = "The ship's fuel and retracting gas are fluids too!"
    elif not Thermo:
        movey =0
    if Thermo:
        col = red
        text = "Using the Carnot Cycle, the ship could move faster"
        Uni = pygame.image.load('p_sky.png')
    elif not F_M:
        movey = 0
    if not Thermo:
        Uni = pygame.image.load('P_Universe.png')
    if ElecMag:
        col = blue
        beam = pygame.image.load('zap.png')
        Uni = pygame.image.load('P_Park.png')
        text = "'Zap. Electricty also created this spinning wheel and LED smiley face'"
    else:
        beam = pygame.image.load('Beam.png')

    if Waves:
        text = "Everybody likes a little Jazz."
        if not Wav:
            pygame.mixer.music.play(-1)
            Wav = True
        else:
            pygame.mixer.music.unpause()
        col = orange
    else:
        if Wav:   
            pygame.mixer.music.pause()

    if Atomic:
        text = "At high speeds and/or quantum scales, distance contract or expand"
        col = purple
        ship = pygame.transform.scale(ship,(r_x,int(149*r_x/127)))
        beam = pygame.transform.scale(beam,(int(22*(r_x/127)),int(34*r_x/127)))
    else:
        g_Monster = pygame.transform.scale(g_Monster,(68,127))
        g_Monster2 = pygame.transform.scale(g_Monster2,(68,127))
        g_Monster3 = pygame.transform.scale(g_Monster3,(68,127))
        ship = pygame.transform.scale(ship,(127,149))
        beam = pygame.transform.scale(beam,(22,34))
    M_text1 = g_text2.render(text,True, col2)
    screen.blit(M_text1,(screen.get_rect().width/2-(M_text1.get_rect().width/2),110))
    M_text2 = g_text2.render("Points: "+str(points),True, col2)
    screen.blit(M_text2,(screen.get_rect().width/2-(M_text2.get_rect().width/2),170))
#Program Running
while not go:
    if Int:
        for event in pygame.event.get():
            #Mouse
            mouse = pygame.mouse.get_pos()
            #Quitting Game
            if event.type==pygame.QUIT:
                go = True

            if 110<=mouse[0]<=390 and 150<=mouse[1]<213:
                violet = (255,150,230)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Int = False
                    Mec = True
                    col = violet
                    col2 = (255,100,180)
            else:
                violet = (255,100,180)

            if 600<=mouse[0]<=840 and 230<=mouse[1]<293:
                green = (120,255,180)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Kin = True
                    g_speed=random.randint(5,25)
                    Int = False
                    col = green
                    col2 = (70,255,130)

            else:
                green =(70,255,130)

            if 350<=mouse[0]<=630 and 310<=mouse[1]<373:
                yellow = (255,255,150)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    F_M = True
                    Int = False
                    col = yellow
                    col2 = (255,255,100)
            else:
                yellow = (255,255,100)

            if 90<=mouse[0]<=370 and 390<=mouse[1]<453:
                red = (255,95,80)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Thermo = True
                    Int = False
                    col = red
                    col2 = (255,45,30)
            else:
                red = (255,45,30)

            if 480<=mouse[0]<=860 and 470<=mouse[1]<533:
                blue = (150,180,255)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    ElecMag = True
                    Int = False
                    col = blue
                    col2 = (100,130,255)
            else:
                blue = (100,130,255)

            if 110<=mouse[0]<=490 and 550<=mouse[1]<613:
                orange = (255,161,53)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Waves = True
                    Int = False
                    col = orange
                    col2 = (252,111,3)
            else:
                orange = (252,111,3)

            if 440<=mouse[0]<=960 and 630<=mouse[1]<693:
                purple = (255,53,255)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Atomic = True
                    r_x = random.randint(80,150)
                    r_y = random.randint(35,80)
                    r_y_2 = random.randint(35,80)
                    r_y_3 = random.randint(35,80)
                    g_Monster = pygame.transform.scale(g_Monster,(r_y,int(127*r_y/68)))
                    g_Monster2 = pygame.transform.scale(g_Monster2,(r_y_2,int(127*r_y_2/68)))
                    g_Monster3 = pygame.transform.scale(g_Monster3,(r_y_3,int(127*r_y_3/68)))
                    m_monster1 = Monster(0,random.randint(370,600),g_Monster,0)
                    m_monster2 = Monster(0,random.randint(370,600),g_Monster2,1)
                    m_monster3 = Monster(0,random.randint(370,600),g_Monster3,2)
                    Int = False
                    col = purple
                    col2 = (240,3,252)
            else:
                purple = (240,3,252)


     #Filling screen with black + Major writings
        screen.fill((0,0,0))
        g_text1 = pygame.font.SysFont("Cambria",40)
        g_text2 = pygame.font.SysFont("Cambria",30)
        title = g_text1.render("Welcome to Physics Master!", True , red)
        headline = g_text2.render("Pick a topic below:", True , red)
        screen.blit(title,((500-(title.get_rect().width)/2),20))
        screen.blit(headline,((500-(headline.get_rect().width)/2),100))
        
        #Buttons
        #Mechanics
        drawbutton(violet,150,0, 'Mechanics')
        #Kinematics
        drawbutton(green,230,1,'Kinematics')
        #Fluid Mechanics
        drawbutton(yellow,310,2, 'Fluid Mechanics')
        #Thermodynamics
        drawbutton(red,390,3, 'Thermodynamics')
        #Electricity and Magnetism
        drawbutton(blue,470,4, 'Electricity and Magnetism')
        #Oscillation and Waves
        drawbutton(orange,550,5, 'Oscillation and Waves')
        #Atomic, Nuclear, and Particle Physics
        drawbutton(purple,630,6, 'Atomic, Nuclear, and Particle Physics')
    
    else:
        #Determining default ship image, considering that it's altered when F_M is true and ship-monster collisions occur
        if not (Thermo or ElecMag):
            ship = pygame.image.load('Spaceship.png')
        elif Thermo:
            ship = pygame.image.load('Spaceship_Turbo.png')
        else:
            ship = pygame.image.load('E_Spaceship.png')
        if not Kin:
            g_speed = 40
        #True for all Subdivisions
        for event in pygame.event.get():
            #Mouse
            mouse = pygame.mouse.get_pos()
            press = pygame.mouse.get_pressed()
            #Quitting Game
            if event.type==pygame.QUIT:
                go = True

            #Shooting
            if event.type==pygame.MOUSEBUTTONDOWN and (press[0] or press[1]):
                shooting = True
            elif event.type==pygame.MOUSEBUTTONUP and (not press[0] and not press[1]):
                shooting = False
                t=0
            if 30<=mouse[0]<=90 and 20<=mouse[1]<=60:
                violet = (255,150,230)
                green = (120,255,180)
                yellow = (255,255,150)
                red = (255,95,80)
                blue = (150,180,255)
                orange = (255,161,53)
                purple = (255,53,255)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Int = True
                    Mec = False
                    Kin = False
                    F_M = False
                    Thermo = False
                    ElecMag = False
                    Waves = False
                    Atomic = False

            else:
                violet = (255,100,180)
                green =(70,255,130)
                yellow = (255,255,100)
                red = (255,45,30)
                blue = (100,130,255)
                orange = (255,111,3)
                purple = (240,3,252)

            if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT:
                        p_r = True
                    if event.key==pygame.K_LEFT:
                        p_l = True
                    if event.key==pygame.K_UP:
                        p_u = True
                    if event.key==pygame.K_DOWN:
                        p_d = True

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    p_r = False
                if event.key==pygame.K_LEFT:
                    p_l = False
                if event.key==pygame.K_UP:
                    p_u = False
                    u_speed = 20
                if event.key==pygame.K_DOWN:
                    p_d = False
                    u_speed = 20

        screen.fill((0,0,0))
        pygame.draw.rect(screen,col,(30,20,60,40))
        screen.blit(arrow, (35,26))
        Formulas = g_text1.render("Space Arcade", True , col2)
        screen.blit(Formulas,((500-((Formulas.get_rect().width)/2),10)))
        Rendfunc()
        screen.blit(Uni, ((1000-Uni.get_rect().width)/2,250))
        #Planet_Movement
        planets = [Mercury,Venus,Earth,Mars,Saturn,Jupiter,Neptune,Uranus]
        p_y+=1
        if p_y>=1500:
            a+=1
            p_y = 300
        if a>6:
            a=0
        planets = [Mercury,Venus,Earth,Mars,Saturn,Jupiter,Neptune,Uranus]
        screen.blit(planets[a], (20,p_y))
        if movex>=380:
            movex=380
        elif movex<=-430:
            movex = -430

        if movey>=320:
            movey=320
            u_speed=20
        elif movey<=0:
            movey =0
            u_speed=20

        if p_r:
            movex+=m_r
            if Mec:
                active1 = True
                active2 = False
            else:
                active1 = False
        if p_l:
            movex-=m_l
            if Mec:
                active2 = True
                active1 = False
            else:
                active2 = False

        if p_u and (F_M or Thermo):
            movey-=u_speed
            if Thermo:
                u_speed+=4
            else:
                u_speed = 20
            t_1+=1
            if t_1<7:
                if F_M:
                    ship = pygame.image.load('Spaceship_U.png')
                if Thermo:
                    ship = pygame.image.load('Spaceship_T.png')
            else:
                if F_M:
                    ship = pygame.image.load('Spaceship.png')
                if Thermo:
                    ship = pygame.image.load('Spaceship_Turbo.png')
                if t_1>14:
                    t_1=0
        if p_d and (F_M or Thermo):
            movey+=u_speed
            if Thermo:
                u_speed+=4
            else:
                u_speed = 20
            t_2+=1
            if t_2<7:
                if F_M:
                    ship = pygame.image.load('Spaceship_D_1.png')
                if Thermo:
                    ship = pygame.image.load('Spaceship_Turbine_1.png')
            else:
                if F_M:
                    ship = pygame.image.load('Spaceship_D_2.png')
                if Thermo:
                    ship = pygame.image.load('Spaceship_Turbine_2.png')
                if t_2>14:
                    t_2=0
        if active1 and Mec:
            movex+=3
        if active2 and Mec:
            movex-=3
        #Laser limit + Movement 
        Laser.move(l)
        #Interval between spawns
        if switch1:
            t_interval1+=0.8
        if switch2:
            t_interval2+=0.8
        #Monster Action
        if not (ElecMag or Atomic):
            Monster.move(monster1)
        elif ElecMag:
            Monster.move(m1)
        else:
            Monster.move(m_monster1)
        if t1>0:
            t1-=1
        else:
            if not (ElecMag or Atomic):
                Monster.move(monster2)
            elif ElecMag:
                Monster.move(m2)
            else:
                Monster.move(m_monster2)
            if t2>0:
                t2-=1
            else:
                if not (ElecMag or Atomic):
                    Monster.move(monster3) 
                elif ElecMag:
                    Monster.move(m3) 
                else:
                    Monster.move(m_monster3)

        if shooting:
            if ElecMag:
                ship = pygame.image.load('E_Spaceship2.png')
                if l_x>=-295:
                    l_x-=4
                    Laser.rend = True
                else:
                    Laser.rend = False
            else:
                Laser.rend = True
            if t<20:
                t+=1
        else:
            if l.l_y>=1000:
                m_list.clear()
            if l.l_2>=1000:
                d_list.clear()
            if ElecMag and l_x<=0:
                if l_x<=-295:
                    if 0<=t_tick<=15:
                        t_tick-=1
                    else:
                        l_x+=10
                        t_tick=15
                else:
                    l_x+=0.5
        #Blitting the ship
        screen.blit(ship, (450+movex,230+movey))
        if ElecMag:
            pygame.draw.rect(screen,yellow,(675,200,300+l_x,40))
    pygame.display.flip()
    clock.tick(30)