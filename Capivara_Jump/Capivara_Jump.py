import pygame
from pygame.locals import *
import time
clock=pygame.time.Clock()
import os
pygame.init()
#Variables
width = 800
height = 500
game_over = False
intro = True
início = True
but_color1= (30,50,255)
but_color2=but_color1
but_color3=but_color1
but_color4=but_color1
but_color5=but_color1
but_color6=but_color1
but_color7 = but_color1
but_col_alt1 = (70,90,255)
but_col_alt2 = but_col_alt1
but_col_alt3 = but_col_alt1
but_col_alt4 = but_col_alt1
but_col_alt5 = but_col_alt1
but_col_alt6 = but_col_alt1
but_col_alt7 = but_col_alt1
ret_but = (255,30,40)
q_but = ret_but
ret_col = ret_but
light_red = (255,60,70)
text_col = (255,240,240)
title_col = (255,60,60)
white = (255,255,255)
purple = (255,0,64)
but1=False
but2=False
but3=False
g_o = False
#Initial Game Difficulty
easy = False
hard = False
medium = True
#Movement Variables
movex=0
movey=0
life = -200
p_r=False
p_l = False
j = False
#Facing dirction variable
f_r = True #Animal initially facing the right
f_l = False
#Enable Jump?
e_jump = True #Initially, animal can jump
#Setting up the screen
#screen
screen = pygame.display.set_mode((width,height))
ícone = pygame.image.load("Capivara.jpg")
pygame.display.set_icon(ícone)
pygame.display.set_caption("CapivaraJump")

#Game Points
points = 0
#Villain Movement & variables
laser = False
crazy = False
binary = 0
addy1 = 0
addy2 = 0
mylist = []
q_time = 10
timer = 10 #Initial time
timer2 = timer
timer3 = 20
timer4 = timer3
crz_time = 10
waiting = 8
rest_time = 10
movex1 = 0
movex2 = movex1
movex3 = movex1
movex4 = movex1
movey1 = 0
j_speed = 11
j2 = 15
r_speed = 10
l_speed=10
m1 = 3
m2 = 0.8
m4 = 2
movey2 = movey1
movey3 = movey1
movey4 = movey1
movey6 = movey1
dead1 = False
dead2 = False
dead3 = False
dead4 = False 
temp1 = -100+movex3
temp2=-100+movex3
movex6 = temp1+addy1
#Images
back_image = pygame.image.load("Bernardão.jpg")
back_image1 = pygame.image.load("main_image.jpg")
back_pic = back_image1
back_image2 = pygame.image.load("background2.jpg")
back_image3 = pygame.image.load("UFV.jpg")
quit_im = pygame.image.load("Quit_image.jpg")
surprise = pygame.image.load("Capi.jpg")
main_1 = pygame.image.load("main1.png")
main_2 = pygame.image.load("main2.png")
run_1 = pygame.image.load("run1.png")
run_2 = pygame.image.load("run2.png")
jump_1 = pygame.image.load("jump1.png")
jump_2 = pygame.image.load("jump2.png")
power_jump1 = pygame.image.load("Jump_power.png")
power_jump2 = pygame.image.load("power2.png")
vilpic = pygame.image.load("Mico_1.png")
vilpic1 = pygame.image.load("Mico_1.png")
vilpic2 = pygame.image.load("Mico_2.png")
vilpic3 = pygame.image.load("Mutant1.png")
mutant1 = pygame.image.load("Mutant1.png")
mutant2 = pygame.image.load("mutant2.png")
fishpic = pygame.image.load("Fish1.png")
fishy1 = pygame.image.load("Fish1.png")
fishy2 = pygame.image.load("Fish2.png")
fishpic2 = pygame.image.load("Fish_E2.png")
fishy3 = pygame.image.load("Fish_E1.png")
fishy4 = pygame.image.load("Fish_E2.png")
Laser = pygame.image.load("Laser.png")
Package = pygame.image.load("Poop1.png")
Package1 = pygame.image.load("Poop1.png")
Package2 = pygame.image.load("apple.png")
Package3 = pygame.image.load("Poop2.png")
none = pygame.image.load("None.png")
#Current sprite image
cappic = main_1
#Collision Variables
col1 = False
col2 = False
col3 = False
#Fullscreen/Reduced Screen variables
full = False
s1 = 38
s2 = 28
#Quit Button
q_col = ret_but
q_col_alt = light_red
msg = False
#Blocking other input when pop up message appears
inp = True
#Pop Up Button Border Color
brown = (102, 51, 0)
brown1 = brown
brown2 = brown
l_brown = (102, 81, 30)

while not game_over:
    #########################################  Game Intro ###############################
    if intro:
        if início is True:
            cord = (355,232)
            gametext = pygame.font.SysFont("PolandCannedIntoFuture",40)
            gametext1 = pygame.font.SysFont("PolandCannedIntoFuture",60)
            g_text1 = gametext.render("Jogar", True , text_col)
        else:
            cord = (320,232)
            g_text1 = gametext.render("Continuar", True , text_col)
        #background image
        screen.blit(back_image,(0,0))
        #buttons
        pygame.draw.rect(screen,but_color1,(300,225,200,50))
        pygame.draw.rect(screen,but_color2,(300,350,200,50))
        pygame.draw.rect(screen,but_color3,(300,100,200,50))
        #Quit Button
        pygame.draw.rect(screen,q_col,(20,20,50,50))
        pygame.draw.line(screen, white, (26,26), (64,64),6)
        pygame.draw.line(screen, white, (26,64), (64,26),6)  
        #Fullscreen vs reduced window
        if not full:
            s1 = 38
            s2 = 28
        else:
            s1 = 33
            s2 = 25.31
        pygame.draw.rect(screen,but_color7,(730,20,50,50))
        pygame.draw.rect(screen,white,(730+(50-s1)/2,20+((50-s1)/2),s1,s1))
        pygame.draw.rect(screen,but_color7,(730+(50-s2)/2,20+((50-s2)/2),s2,s2))          
        #Text in Buttons 
        g_text3 = gametext.render("Reiniciar", True , text_col)
        g_text4 = gametext.render("Dificuldade", True , text_col)
        g_text2 = gametext1.render("Capivara Jump", True , title_col)
        screen.blit(g_text1,cord)
        screen.blit(g_text2,(230,25))
        screen.blit(g_text3,(328,357))
        screen.blit(g_text4,(310,107))
        #Quit game message
        if msg:

            pygame.draw.rect(screen,brown,(175,150,450,200))
            pygame.draw.rect(screen,(255, 204, 102),(185,160,430,180))
            d1_text = gametext.render("Deseja realmente",True , brown)
            d_text = gametext.render("sair do jogo",True , brown)
            screen.blit(d1_text,(280,175))
            screen.blit(d_text,(300,225))
            #Question
            pygame.draw.rect(screen,brown,(518,227,19,5))
            pygame.draw.rect(screen,brown,(533,227,4,12))
            pygame.draw.rect(screen,brown,(518,239,19,5))
            pygame.draw.rect(screen,brown,(518,244,4,9))
            pygame.draw.rect(screen,brown,(518,257,4,4))
            #Buttons
            pygame.draw.rect(screen,brown1,(220,290,160,40))
            pygame.draw.rect(screen,brown2,(420,290,160,40))
            #Text in Buttons
            y_text = gametext.render("SIM",True , white)
            n_text = gametext.render("NAO",True , white)
            screen.blit(y_text,(470,295))
            screen.blit(n_text,(270,295))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            mouse = pygame.mouse.get_pos()
            if inp:
                #Exit game
                if 20<mouse[0]<70 and 20<mouse[1]<70:
                    q_col = q_col_alt
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        msg = True
                        inp = False
                else:
                    q_col = (255,30,40)
                #Fullscreen/ Reduced screen shift
                if 730<mouse[0]<780 and 20<mouse[1]<70:
                    but_color7 = but_col_alt7
                    if event.type==pygame.MOUSEBUTTONDOWN and not full:
                        screen = pygame.display.set_mode((width,height),FULLSCREEN)
                        full = True
                    elif event.type==pygame.MOUSEBUTTONDOWN and full:
                        screen = pygame.display.set_mode((width,height))
                        full = False
                else:
                    but_color7 = (30,50,255)
                if 300<mouse[0]<500 and 225<mouse[1]<275:
                    but_color1 = but_col_alt1
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro=False
                        início = False
                        but1=True
                        but2=False
                        but3=False
                else:
                    but_color1=(30,50,255)
                        
                if 300<mouse[0]<500 and 350<mouse[1]<400:
                    but_color2 = but_col_alt2
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro=False
                        início = False
                        but2=True
                        but1=False
                        but3=False
                else:
                    but_color2=(30,50,255)

                if 300<mouse[0]<500 and 100<mouse[1]<150:
                    but_color3 = but_col_alt3
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro=False
                        but3=True
                        but1=False
                        but2=False
                else:
                    but_color3=(30,50,255)
            else:
                #Deciding whether or not to quit
                if 220<mouse[0]<380 and 290<mouse[1]<330:
                    brown1 = l_brown
                else:
                    brown1 = brown

                if 420<mouse[0]<580 and 290<mouse[1]<330:
                    brown2 = l_brown
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        game_over = True
                else:
                    brown2 = brown
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        inp = True
                        msg = False
                    
                #pygame.draw.rect(screen,brown,(220,290,160,40))
                #pygame.draw.rect(screen,brown,(420,290,160,40))

        pygame.display.flip()
    ######################################################

# Game itself

    if not intro:


        #In case the user is playing the game
        if but1 is True:
            screen.blit(back_pic,(0,0))

        
            #Pause Button
            pygame.draw.rect(screen,ret_col,(10,10,50,50))
            pygame.draw.rect(screen,white,(20,18,10,33))
            pygame.draw.rect(screen,white,(40,18,10,33))
            
            #Game Speed
            if easy:
                clock.tick(40)
            if medium:
                clock.tick(80)
            if hard:
                clock.tick(100)
            #Events
            #Setting up x boundaries
            if movex>=335:
                movex=335
            elif movex<=-295:
                movex=-295
    
            #Moving right
            if p_r is True:
                movex+=r_speed
                if j is False:
                    cappic = run_1
                else:
                    cappic = jump_1
            #Moving left
            if p_l is True:
                movex-=l_speed
                if j is False:
                    cappic = run_2
                else:
                    cappic = jump_2
            #Jumping
            if j:

                if movey<=-250:
                    movey+=j_speed
                    up = False
                elif up:
                    movey-=j2
                else:
                    movey+=j2
                if f_r:
                    cappic = jump_1
                elif f_l:
                    cappic = jump_2

                #lower jump boundaries
                if movey>=0:
                    movey = 0
                    j = False
                    e_jump = True
                    if f_r:
                        cappic = main_1
                    elif f_l:
                        cappic=main_2
            

            for event in pygame.event.get():
                #Quitting the game
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                #Pausing the game
                mouse = pygame.mouse.get_pos()
                if 10<=mouse[0]<=60 and 10<=mouse[1]<=60:
                    ret_col = light_red

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro = True
                        início = False
                        but1=False
                        but2=False
                        but3=False
                else:
                    ret_col = ret_but

                #Moving left and right
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        p_r = True
                        f_r = True
                        f_l = False
                    if event.key==pygame.K_LEFT:
                        p_l = True
                        f_r = False
                        f_l = True
                    if event.key==pygame.K_SPACE and e_jump is True:
                        j = True
                        up = True
                        e_jump=False #While jumping, user can't jump again


                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        p_r = False
                        cappic=main_1
                    if event.key==pygame.K_LEFT:
                        p_l = False
                        cappic=main_2
            #Enemy 1
            if not dead1:
                movex1+=m1
                timer -=0.3
                if timer>0:
                    vilpic = vilpic1
                else:
                    vilpic = vilpic2
                    if timer<=-10:
                        timer+=30.12
                        
            #Respawn enemies
            else:
                movex1 = -300
                points+=5
                dead1 = False
            if movex1>=800:
                dead1 = True
                 

            #Enemy2
            if not dead2:
                movex2+=m2
                timer2 -=0.3
                if timer2>0 and m2 !=0:
                    vilpic3 = mutant1
                else:
                    vilpic3 = mutant2
                    if timer2<=-10:
                        timer2+=20.12
                        
            #Respawn enemies
            else:
                movex2 = -400
                points+=5
                dead2 = False
            if movex2>=1150:
                dead2 = True

            #Enemy 3
            if not dead3:
                timer3-=0.1
                if timer3<=0:
                    fishpic = fishy1
                    #Fish stops and rests
                    rest_time -=0.1
                    if rest_time<=0:
                        movex3+=100
                        mylist.append(-100+movex3)
                        fishpic = fishy2
                        timer3+=15
                        rest_time+=5
                if movex3>=1400:
                    dead3 = True
                    mylist = []
            
            else:
                movex3=0
                dead3 = False
            #Enemy 4
            if not dead4:
                movex4+=m4
                timer4 -=0.1
                if timer4<=0:
                    fishpic2 = fishy3
                    laser = True
                if timer4<=-10:
                    fishpic2 = fishy4
                    laser = False
                    pygame.display.flip()
                    timer4+=30
                if movex4>=1600:
                    dead4 = True
            else:
                movex4 = -800
                dead4 = False
            

            #Drawing the character
            screen.blit(cappic,(300+movex,365+movey))
            #Drawing the villains
            screen.blit(vilpic,(-50+movex1,380+movey1))
            screen.blit(vilpic3,(-400+movex2,312+movey2))

            #"Package Operations"
            #if package:
            if len(mylist)>=1:
                movex6 = temp1+addy1
                addy1+=0.2
                movey6+=3.5
                screen.blit(Package,(movex6,75+movey6))
            #Respawning Poop - *poop makes the Capivara slower*
            if movey6>=440:
                movey6=0
                addy1=0
                temp1 = mylist[len(mylist)-1]
                if binary==0:
                    binary=1
                    Package = Package1
                else:
                    binary = 0
                    Package = Package2
                pygame.display.flip()


            #Drawing Fish1
            screen.blit(fishpic,(-100+movex3,50+movey3))
            #screen.blit(fishpic,(-400+movex3,50+movey3))

            #"Laser operations"
            if laser:
                #Drawing the laser
                screen.blit(Laser,(-815+movex4,275+movey4))

            #Drawing Fish2
            screen.blit(fishpic2,(-800+movex4,95+movey4))
            

             #Life Bar
            pygame.draw.rect(screen,light_red,(790,20,life,35))
            #Game Over
            if life>=-5:
                life=-5
                g_o = True
                but1 = False


            #Collisions
            #Monkey collisions
            if (300+movex<-10+movex1<460+movex or 300+movex<80+movex1<460+movex) and (365+movey<400+movey1<445+movey):
                col1 = True
            else:
                if col1:
                    if easy:
                        life+=10
                    if medium:
                        life+=16
                    if hard:
                        life+=20
                    col1 = False
                else:
                    col1 = False
            if (300+movex<-320+movex2<460+movex or 300+movex<-240+movex2<460+movex) and e_jump:
                col2 = True
            else:
                if col2:
                    crazy = True
                    col2 = False
                else:
                    col2 = False
            if crazy:
                crz_time-=0.01
            if crz_time>0 and crazy:
                back_pic = surprise
                j_speed = 3
                j2 = 3
                r_speed = 2
                l_speed = 2
                m1 = 5
                m2 = 0
                m4 = 4

            else:
                back_pic = back_image1
                j_speed = 11
                j2 = 15
                r_speed = 10
                l_speed = 10
                m1 = 3
                m2 = 0.8
                m4 = 2
                crazy = False
                if crz_time<0:
                    movex2 = -400
                    crz_time=10
                else:
                    crz_time=10

            #Laser Collisions
            if (300+movex<-800+movex4<460+movex or 300+movex<-750+movex4<460+movex) and laser:
                if easy:
                    life+=0.25
                if medium:
                    life+=0.4
                if hard:
                    life+=0.6
                
            #Poop/Apple collisions
            if (300+movex<-30+movex6<460+movex or 300+movex<100+movex6<460+movex) and (365+movey<-15+movey6<445+movey or 365+movey<125+movey6<445+movey):
                col3  =True
            else:
                if col3 and Package==Package2:
                    if easy:
                        life-=15
                    if medium:
                        life-=8
                    if hard:
                        life-=5
                    binary = 1
                    points+=20
                    Package = none
                    col3 = False

                elif col3 and Package==Package1:
                    col3 = False
                    Package = Package3
                else:
                    col3 = False

                    
            #Life limit
            if life<=-200:
                life = -200
            


            gametext2 = pygame.font.SysFont("Arial",40)
            g_text9 = gametext.render("Pontos ", True ,light_red)
            g_text10 = gametext2.render(str(points), True ,light_red)
            g_text11 = gametext2.render(":", True ,light_red)
            screen.blit(g_text9,(90,30))
            screen.blit(g_text11,(210,25))
            screen.blit(g_text10,(230,25))
            
             



            #Update screen
            pygame.display.flip()


        if g_o:
            screen.blit(quit_im,(0,0))
            gametexty = pygame.font.SysFont("Arial",60)
            g_text12 = gametext1.render("GAME OVER", True , light_red)
            g_text13 = gametext1.render("PONTOS", True , light_red)
            g_text14 = gametexty.render(":", True , light_red)
            g_text15 = gametexty.render(str(points), True , light_red)
            g_text16 = gametext1.render("REINICIAR", True ,white)
            screen.blit(g_text12,(230,25))
            screen.blit(g_text13,(230,240))
            screen.blit(g_text14,(410,220))
            screen.blit(g_text15,(430,227))
            pygame.draw.rect(screen,q_but,(230,350,270,60))
            screen.blit(g_text16,(235,360))
            for event in pygame.event.get():
                #Quitting the game
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                mouse = pygame.mouse.get_pos()
                if 230<mouse[0]<500 and 350<mouse[1]<410:
                    q_but = light_red
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        def opengame():
                            os.startfile("Capivara_Jump.py")                 
                        opengame()
                        pygame.quit()
                else:
                    q_but = ret_but
#  Restarting

        if but2 is True:
            screen.blit(back_image2,(0,0))

            #Pause Button
            pygame.draw.rect(screen,ret_col,(10,10,50,50))
            pygame.draw.rect(screen,white,(20,18,10,33))
            pygame.draw.rect(screen,white,(40,18,10,33))
            #Rendered Text
            gametext5 = pygame.font.SysFont("PolandCannedIntoFuture",60)
            gametext6 = pygame.font.SysFont("Arial",60)
            g_text17 = gametext5.render("Reiniciando", True ,ret_but)
            g_text18 = gametext6.render("...", True , ret_but)
            screen.blit(g_text17,(220,30))
            screen.blit(g_text18,(300,30))
            #Events
            def opengame():
                os.startfile("Capivara_Jump.py") 
            for event in pygame.event.get():
                #Quitting the game
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                #Pausing the game
                mouse = pygame.mouse.get_pos()
                if 10<=mouse[0]<=60 and 10<=mouse[1]<=60:
                    ret_col = light_red

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro = True
                        início = False
                        but1=False
                        but2=False
                        but3=False
                else:
                    ret_col = ret_but                
            q_time -=0.2
            if q_time<=0:
                opengame()
                pygame.quit()
            #Update screen
            pygame.display.flip()

# Changing game difficulty

        if but3 is True:
            screen.blit(back_image3,(0,0))

            #Pause Button
            pygame.draw.rect(screen,ret_col,(10,10,50,50))
            pygame.draw.rect(screen,white,(20,18,10,33))
            pygame.draw.rect(screen,white,(40,18,10,33))
            #Other Buttons
            pygame.draw.rect(screen,but_color4,(300,225,200,50))
            pygame.draw.rect(screen,but_color5,(300,350,200,50))
            pygame.draw.rect(screen,but_color6,(300,100,200,50))
            #Text in Buttons 
            g_text7 = gametext.render("Dificil", True , text_col)
            g_text8 = gametext.render("Medio", True , text_col)
            g_text6 = gametext.render("Facil", True , text_col)
            g_text5 = gametext1.render("Dificuldade", True , title_col)
            screen.blit(g_text8,(355,232))
            screen.blit(g_text5,(250,25))
            screen.blit(g_text7,(355,357))
            screen.blit(g_text6,(355,107))
            #Events
            for event in pygame.event.get():
                #Quitting the game
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                #Pausing the game
                mouse = pygame.mouse.get_pos()
                if 10<=mouse[0]<=60 and 10<=mouse[1]<=60:
                    ret_col = light_red

                    if event.type==pygame.MOUSEBUTTONDOWN:
                        intro = True
                        but1=False
                        but2=False
                        but3=False
                else:
                    ret_col = ret_but

                #Changing button colors
                if 300<mouse[0]<500 and 225<mouse[1]<275:
                    but_color4 = but_col_alt4     
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        medium = True
                        easy = False
                        hard = False
                        intro = False
                        início = False
                        but1=True
                        but2=False
                        but3=False
                else:
                    but_color4=(30,50,255)
                        
                if 300<mouse[0]<500 and 350<mouse[1]<400:
                    but_color5 = but_col_alt5
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        hard = True
                        easy = False
                        medium = False
                        intro = False
                        início = False
                        but1=True
                        but2=False
                        but3=False
                else:
                    but_color5=(30,50,255)

                if 300<mouse[0]<500 and 100<mouse[1]<150:
                    but_color6 = but_col_alt6
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        easy = True
                        hard = False
                        medium = False
                        intro = False
                        início = False
                        but1=True
                        but2=False
                        but3=False

                else:
                    but_color6=(30,50,255)
        #Update screen
        pygame.display.flip()

'''
Oriinal images sources: 
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjkuNH3kdrjAhUrIbkGHSl2CVoQjhx6BAgBEAI&url=https%3A%2F%2Fwww.portaldosanimais.com.br%2Finformacoes%2Fcapivara-caracteristicas-e-fotos%2F&psig=AOvVaw3udSGFKlhPCxFELIIZ15E0&ust=1564489986779974
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjt8rym-tjjAhVRLLkGHSHqDZwQjhx6BAgBEAI&url=https%3A%2F%2Fwww.flickr.com%2Fphotos%2Fvinicius_maciel%2F390439792&psig=AOvVaw0NFJMQ5RM-p5IiFFfzYj_k&ust=1564449027557266
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjGibb8-NjjAhX-ILkGHe-iDb4Qjhx6BAgBEAI&url=https%3A%2F%2Fprimeiroasaber.com.br%2F2018%2F04%2F26%2Fufv-divulga-10-editais-para-contratacao-de-professores-campus-vicosa%2F&psig=AOvVaw0NFJMQ5RM-p5IiFFfzYj_k&ust=1564449027557266
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjSrNGJztjjAhVUHbkGHdolAtQQjhx6BAgBEAI&url=https%3A%2F%2Fprimeiroasaber.com.br%2F2019%2F05%2F07%2Freitoria-da-ufv-divulga-nota-sobre-bloqueio-orcamentario%2F&psig=AOvVaw3EiHdLZklqfPyTBniQxMpz&ust=1564437518887038
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiOx9qs9djjAhWpH7kGHbyLC5wQjhx6BAgBEAI&url=http%3A%2F%2Fwww.sbqp2015.ufv.br%2F%3Fpage_id%3D20&psig=AOvVaw2IysCl-OaZOZnnaErofmsC&ust=1564447811277244
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjl1-miztjjAhWnLLkGHWm2DkgQjhx6BAgBEAI&url=http%3A%2F%2Fwww.portal.ufv.br%2Fflorestal%2F%3Fpage_id%3D174&psig=AOvVaw3EiHdLZklqfPyTBniQxMpz&ust=1564437518887038

Font source:
https://www.fontspace.com/category/pixelated - Poland canned into Space

Pixeltor: https://pinetools.com/pixelate-effect-image

Image Resizor:https://resizeimage.net/

Sprite Creator: Piskel

LunaPic: used for mirroring pixelated images
'''