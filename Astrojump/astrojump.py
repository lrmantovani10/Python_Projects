#starting pygame
import pygameM random, time, os
pygame.init()
#variables used
width = 700
height = 700
white = (255,255,255)
purple = (204, 0, 255)
blue1 = (51, 204, 255)
red = (255,30,30)
green = (30,255,20)
yellow = (255,255,30)
magenta = (255,0,255)
pink = (255,30,150)
blue =(0,30,255)
movex = 0
movey=0
red1 = red
red2 = (180,0,0)
ximg = "NY.jpg"
yimg = "Paris.jpg"
zimg = "Tokyo.jpg"
pimg = "Sydney.jpg"
light_purple = (80,80,185)
purple1 = (40,40,105)
purple2 = (40,40,105)
purple3 = (40,40,105)
purple4 = (40,40,105)
purple5 = (40,40,105)
clock = pygame.time.Clock()
backgroundimg1 = pygame.image.load("NY.jpg")
backgroundimg = pygame.image.load("starry_sky.jpg")
#screen
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Astrojump")
#Screen astronaut icon
icon = pygame.image.load("astro_icon.jpg")
pygame.display.set_icon(icon)
game_over = False
intro = True
moving_r = False
moving_l = False
moving_up = False
moving_down=False
points = 0
monsterx = random.randint(10,660)
monsterx1 = random.randint(10,660)
monsterx2 = random.randint(10,660)
monsterx3 = random.randint(10,660)
monsterx4 = random.randint(10,660)
monsterx5 = random.randint(10,660)
monstery = 0
monstery1 = 0
monstery2 = 0
monstery3 = 0
monstery4 = 0
monstery5 = 0
box_y = 0
monsterspeed = 5
box_x = random.randint(10,660)
textcolor = green
eyemonster = white
life_length = 80
color_life1 = 255
color_life2 = 255
customcolor = 255
Tokyo = False
NY = False
Australia = False
Paris = False
count = True
#Delete intro function
def deletemyintro():
    global intro
    del intro
#Game Over function
def gameoverfunc():
    global intro,width,height,screen,backgroundimg,yellow,points,purple5,light_purple,game_over
    screen.blit(backgroundimg,(0,0))
    gametext3 = pygame.font.SysFont("havetica",60) 
    g_text3 = gametext3.render("Game Over!", True , yellow)
    g_text4 = gametext3.render("Your Points:"+" " + str(points), True , yellow)
    g_text5 = gametext3.render("Play Again", True ,yellow)
    screen.blit(g_text3, (240,220))
    screen.blit(g_text4, (220,300))
    pygame.draw.rect(screen,purple5,(240,400,225,60))
    screen.blit(g_text5, (245,400))
    pygame.display.flip()
    for event in pygame.event.get():
        #Getting the mouse coordinates
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
        if 240<mouse[0]<460 and 400<mouse[1]<460:
            purple5 = light_purple
            if event.type ==pygame.MOUSEBUTTONDOWN:
                game_over = False
                points = 0
                def opengame():
                    os.startfile("astrojump.py")                 
                opengame()
                pygame.quit()
        else:
            purple5=(40,40,105)
    
        
#Generate Monsters
def monstergen():
    global monsterx, monsterx1, monsterx2, monsterx3, monsterx4, monsterx5, screen, monsterspeed, green, points, count, movey, movex, monstery, monstery1, monstery2, monstery3, monstery4, monstery5, eyemonster, life_length, box_x, box_y, color_life1, color_life2, customcolor, Paris, NY, Tokyo, Australia, purple1, ligh_purple

    #Life Boxes that glow
    if NY is True:
        customcolor=255
        color_life1-=10
        color_life2-=10
        if color_life1<=20:
            color_life1 =200
            color_life2 =200
            customcolor = 255
    if Paris is True:
        color_life1-=10
        customcolor-=10
        color_life2 = 255
        if color_life1<=20:
            color_life1 =200
            customcolor=200
            color_life2 = 255
    if Tokyo is True:
        color_life1=255
        customcolor-=10
        color_life2 -=10
        if color_life2<=20:
            color_life2 =200
            customcolor=200
            color_life1 = 255
    if Australia is True:
        color_life1=255
        customcolor-=10
        color_life2 -=10
        if color_life2<=215:
            color_life2 =255
        if customcolor<=10:
            customcolor=255
            color_life2 = 255

            
    #Box generating new boxes after box exits the screen
    if box_y+20>=700:
        box_y=-60
        box_x = random.randint(10,660)
    myvar3 = customcolor
    myvar1 = color_life1
    myvar2= color_life2
    pygame.draw.ellipse(screen,(myvar1,myvar2,myvar3),(box_x,20+box_y,40,40))

    #Life Box collisions with character

    if 300+movey<=box_y<=383+movey and 400-58+movex<=box_x<=452.5-58+movex:
        life_length+=2
        box_y = -160
        box_x = random.randint(10,660)
    if 300+movey<=box_y+20+40<=383+movey and 400-58+movex<=box_x<=452.5-58+movex:
        life_length+=2
        box_y = -160
        box_x = random.randint(10,660)
    if 300+movey<=box_y+20<=383+movey and 400-58+movex<=box_x+40<=452.5-58+movex:
        life_length+=2
        box_y = -160
        box_x = random.randint(10,660)
    if 300+movey<=box_y<=383+movey and 400-58+movex<=box_x+40<=452.5-58+movex:
        life_length+=2
        box_y = -160
        box_x = random.randint(10,660)

    #1st monster
    pygame.draw.rect(screen,textcolor,(monsterx,20+monstery,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx+5,22+monstery,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx+28,22+monstery,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx+15,45+monstery,10,10))

    #2nd monster
    pygame.draw.rect(screen,textcolor,(monsterx1,20+monstery1-80,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx1+5,22+monstery1-80,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx1+28,22+monstery1-80,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx1+15,45+monstery1-80,10,10))

    #MiddleMonster
    pygame.draw.rect(screen,textcolor,(monsterx2,20+monstery2-160,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx2+5,22+monstery2-160,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx2+28,22+monstery2-160,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx2+15,45+monstery2-160,10,10))

    #3d monster
    pygame.draw.rect(screen,textcolor,(monsterx3,20+monstery3-240,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx3+5,22+monstery3-240,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx3+28,22+monstery3-240,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx3+15,45+monstery3-240,10,10))

    #4th monster
    pygame.draw.rect(screen,textcolor,(monsterx4,20+monstery4-320,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx4+5,22+monstery4-320,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx4+28,22+monstery4-320,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx4+15,45+monstery4-320,10,10))

    #5th monster
    pygame.draw.rect(screen,textcolor,(monsterx5,20+monstery5-400,40,40))
    pygame.draw.rect(screen,eyemonster,(monsterx5+5,22+monstery5-400,7,15))
    pygame.draw.rect(screen,eyemonster,(monsterx5+28,22+monstery5-400,7,15))
    pygame.draw.ellipse(screen,eyemonster,(monsterx5+15,45+monstery5-400,10,10))

    #Monsterspeed increases + reaches limit
    monsterspeed+=0.01
    box_y+=monsterspeed
    monstery+=monsterspeed
    monstery1+=monsterspeed
    monstery2+=monsterspeed
    monstery3+=monsterspeed
    monstery4+=monsterspeed
    monstery5+=monsterspeed

    if monsterspeed>=20:
        monsterspeed=20

    if monstery+20>=700:
        monstery=-60
        monsterx = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10
        pygame.display.update()
    if monstery1-60>=700:
        monstery1=0
        monsterx1 = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10 
        pygame.display.update()
    if monstery2-140>=700:
        monstery2=0
        monsterx2 = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10 
        pygame.display.update()

    if monstery3-220>=700:
        monstery3=0
        monsterx3 = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10 
        pygame.display.update()

    if monstery4-300>=700:
        monstery4=0
        monsterx4 = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10 
        pygame.display.update()

    if monstery5-380>=700:
        monstery5=0
        monsterx5 = random.randint(10,660)
        #add 10 points
        if count is True:
            points+=10 
        pygame.display.update()


    #Draw lives
    gametext1 = pygame.font.SysFont("havetica",60) 
    g_text2 = gametext1.render("Life Bar:", True , textcolor)
    screen.blit(g_text2, (430,10))
    #Life bar
    pygame.draw.rect(screen, green, (610,20,life_length,25))
    life_length-=0.1
 

    #Minimum point limit:0
    if points<=0:
        points = 0
        pygame.display.update()
    #1st collision: bottom of monster
    if 300+movey<=monstery+60<=383+movey and 400-58+movex<=monsterx<=452.5-58+movex:
        monstery=-70
        monsterx = random.randint(10,660)      
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery1-20<=383+movey and 400-58+movex<=monsterx1<=452.5-58+movex:
        monstery1=-70
        monsterx1 = random.randint(10,660)
        if count is True:
            points-=10 
        pygame.display.update()
    if 300+movey<=monstery2-100<=383+movey and 400-58+movex<=monsterx2<=452.5-58+movex:
        monstery2=-70
        monsterx2 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery3-180<=383+movey and 400-58+movex<=monsterx3<=452.5-58+movex:
        points-=10
        monstery3=-70
        monsterx3 = random.randint(10,660)
    pygame.display.update()
    if 300+movey<=monstery4-260<=383+movey and 400-58+movex<=monsterx4<=452.5-58+movex:
        monstery4=-70
        monsterx4 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery5-340<=383+movey and 400-58+movex<=monsterx5<=452.5-58+movex:
        monstery5=-70
        monsterx5 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()

    #2nd collision:monster top
    if 300+movey<=monstery+20<=383+movey and 400-58+movex<=monsterx<=452.5-58+movex:
        monstery=-70
        monsterx = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery1-60<=383+movey and 400-58+movex<=monsterx1<=452.5-58+movex:
        monstery1=-70
        monsterx1 = random.randint(10,660)
        if count is True:
            points-=10 
    if 300+movey<=monstery2-140<=383+movey and 408.5-58+movex<=monsterx2<=452.5-58+movex:
        monstery2=-70
        monsterx2 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery3-220<=383+movey and 400-58+movex<=monsterx3<=452.5-58+movex:
        monstery3=-70
        monsterx3 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery4-300<=383+movey and 400-58+movex<=monsterx4<=452.5-58+movex:
        monstery4=-70
        monsterx4 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery5-380<=383+movey and 400-58+movex<=monsterx5<=452.5-58+movex:
        monstery5=-70
        monsterx5 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()

    #3d collision: right edge of monster
    if 300+movey<=monstery+60<=383+movey and 400-58+movex<=monsterx+40<=452.5-58+movex:
        monstery=-70
        monsterx = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()

    if 300+movey<=monstery1-20<=383+movey and 400-58+movex<=monsterx1+40<=452.5-58+movex:
        monstery1=-70
        monsterx1 = random.randint(10,660)
        if count is True:
            points-=10 
    if 300+movey<=monstery2-100<=383+movey and 400-58+movex<=monsterx2+40<=452.5-58+movex:
        monstery2=-70
        monsterx2 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery3-180<=383+movey and 400-58+movex<=monsterx3+40<=452.5-58+movex:
        monstery3=-70
        monsterx3= random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery4-260<=383+movey and 400-58+movex<=monsterx4+40<=452.5-58+movex:
        monstery4=-70
        monsterx4 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
    if 300+movey<=monstery5-340<=383+movey and 400-58+movex<=monsterx5+40<=452.5-58+movex:
        monstery5=-70
        monsterx5 = random.randint(10,660)
        if count is True:
            points-=10 
    pygame.display.update()
#Text Function - Intro
def text_display():
    , white
    , screen
    mytext = pygame.font.SysFont("arial",50) 
    citytext = pygame.font.SysFont("havetica",35) 
    text1 = mytext.render("Choose a city below:", True , white)
    text2 = citytext.render("New York", True , red)
    text3 = citytext.render("Paris", True , green)
    text4 = citytext.render("Tokyo", True , yellow)
    text5 = citytext.render("Sydney", True , pink)
    screen.blit(text1, (100,30))
    screen.blit(text2, (290,210))
    screen.blit(text3, (315,310))
    screen.blit(text4, (315,410))
    screen.blit(text5, (305,510))
    pygame.display.update()
#Text Function - Game
def gametext():
    , green
    , textcolor
    , points
    gametext = pygame.font.SysFont("havetica",60) 
    g_text1 = gametext.render("Points:" + " " + str(points), True , textcolor)
    screen.blit(g_text1, (70,10))

    #Menu function
def startmenu():
    global intro,textcolor,screen, purple, blue1, white, magenta, backgroundimg, ximg, backgroundimg1, purple1, purple2, purple3, purple4, light_purple, eyemonster, Paris  , NY , Tokyo , Australia , color_life1, color_life2, customcolor, life_length
    intro = True
    if intro is True and life_length>=0:
        #Getting the mouse coordinates
        mouse = pygame.mouse.get_pos()
        #Adding text to the game
        text_display()
        screen.blit(backgroundimg,(0,0))
        pygame.draw.rect(screen,purple1,(260,200,180,50))
        pygame.draw.rect(screen,purple2,(260,300,180,50))
        pygame.draw.rect(screen,purple3,(260,400,180,50))
        pygame.draw.rect(screen,purple4,(260,500,180,50))
        for event in pygame.event.get():
        #Quitting the game in the menu
            if event.type == pygame.QUIT:
                pygame.quit()
        #Hovering and pressing buttons        
            if 260+180 > mouse[0] > 260 and 200+50 > mouse[1] > 200:
                purple1=light_purple
                #Makes game background image be NY
                textcolor = yellow
                eyemonster = purple
                color_life1=255
                color_life2 = 255
                customcolor = 255
                Paris= False
                NY = True
                Australia = False
                Tokyo = False
                backgroundimg1 = pygame.image.load(ximg)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deletemyintro()
                    intro = False
                   
            else:
                purple1=(40,40,105)

            if 260+180 > mouse[0] > 260 and 300+50 > mouse[1] > 300:
                #Paris background image
                purple2=light_purple
                Paris= True
                NY = False
                Australia = False
                Tokyo = False
                color_life1=255
                color_life2 = 255
                customcolor = 255
                textcolor = red
                eyemonster = blue1
                backgroundimg1 = pygame.image.load(yimg)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deletemyintro()
                    intro = False
              
            else:
                purple2=(40,40,105)

            if 260+180 > mouse[0] > 260 and 400+50 > mouse[1] > 400:
                #Tokyo background image
                purple3=light_purple
                textcolor = green
                eyemonster = magenta
                Paris= False
                NY = False
                Australia = False
                color_life1=255
                color_life2 = 255
                customcolor = 255
                Tokyo = True
                backgroundimg1 = pygame.image.load(zimg)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deletemyintro()
                    intro = False
                

            else:
                purple3=(40,40,105)

            if 260+180 > mouse[0] > 260 and 500+50 > mouse[1] > 500:
                #Sydney background image
                purple4=light_purple
                eyemonster = white
                Paris= False
                NY = False
                Australia = True
                Tokyo = False
                color_life1=255
                color_life2 = 255
                customcolor = 255
                backgroundimg1 = pygame.image.load(pimg)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deletemyintro()
                    intro = False
                
            else:
                purple4=(40,40,105)
                

#Character moving function
def moverightfunc():
    , movex
    movex+=+25
def moveleftfunc():
    , movex
    movex-=25
def moveupfunc():
    , movey
    movey-=25
def movedownfunc():
    , movey
    movey+=25

#Running the game
while not game_over:
    if intro is True:
        startmenu()
    if intro is False and life_length>=0:
        screen.blit(backgroundimg1,(-150,0))
        #Pause Button
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if 20+40 > mouse[0] > 20 and 20+40 > mouse[1] > 20:
                #Pause Game / Hover mouse button
                red1 = red2
                if event.type == pygame.MOUSEBUTTONDOWN:
                    deletemyintro()
                    intro = True
                    red1=red
            else:
                red1=red
        #Quitting the game
            if event.type == pygame.QUIT:
                pygame.quit()
        #Moving the Character around
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    moving_r = True
                    moverightfunc()             
                if event.key==pygame.K_LEFT:
                    moving_l=True
                    moveleftfunc()
                if event.key==pygame.K_UP:  
                    moving_up=True                       
                    moveupfunc()
                if event.key==pygame.K_DOWN:
                    moving_down=True
                    movedownfunc()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    moving_r = False
                if event.key==pygame.K_LEFT:
                    moving_l=False
                if event.key==pygame.K_UP:
                    moving_up=False
                if event.key==pygame.K_DOWN:
                    moving_down=False
        if moving_r is True:
            moverightfunc()
        if moving_l is True:
            moveleftfunc()
        if moving_up is True:
            moveupfunc()
        if moving_down is True:
            movedownfunc()
        #Game Boundaries
        #X Boundaries
        if movex<=-342:
            movex=-342
        if movex>=+308:
            movex=+308
        #Y Boundaries
        if movey>=317:
           movey=317
        if movey<=-300:
           movey=-300
        
    #The main character
    #Head
        pygame.draw.ellipse(screen, white, (400-58+movex,300+movey,50,50))
    #Visor
        pygame.draw.ellipse(screen, blue, (410.5-58+movex,310.5+movey,30,30))
    #Body
        pygame.draw.rect(screen, white, (415.5-58+movex,345+movey,20,30))
    #Jetpack
        pygame.draw.rect(screen, (40,40,40), (408.5-58+movex,353+movey,7,15))
        pygame.draw.rect(screen, (40,40,40), (435.5-58+movex,353+movey,7,15))
    #Legs
        pygame.draw.rect(screen, white, (415.5-58+movex,373+movey,7,10))
        pygame.draw.rect(screen, white, (428.5-58+movex,373+movey,7,10))
    #Apparel
        pygame.draw.rect(screen, (0,255,30), (422.5-58+movex,353+movey,6,6))
        pygame.draw.rect(screen, (255,30,0), (422.5-58+movex,362+movey,6,6))
    #Pause Button
        pygame.draw.rect(screen,red1,(20,20,40,40))
        pygame.draw.rect(screen,white,(27,25,8,28))
        pygame.draw.rect(screen,white,(42,25,8,28))

    #Monsters + Game Over
        gametext()
        monstergen()
    #Minimum life limit:0
        if life_length<=0:
            life_length=0
            count = False
            game_over = True
        #Draw the game 
        pygame.display.update()
        #Frames per second
        clock.tick(30)
#If the game ends
while game_over:
    gameoverfunc() 