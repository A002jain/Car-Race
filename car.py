import pygame #pygame is instane or create aliase name as
#import pygame as p
import time
import random
pygame.init() #intiation function

crashsound=pygame.mixer.Sound(r"SoundTrack\Car_Crash.wav")
#music=pygame.mixer.Sound(r"E:\car\StartCar.wav")
gamestart=pygame.mixer.Sound(r"SoundTrack\start.wav")
pygame.mixer.music.load(r"SoundTrack\StartCar.wav")
display_width=800 
display_height=600

#color defination (R,G,B)
black=(0,0,0)
white=(255,255,255) # (8bit,8bit,8bit)
red=(255,0,0)

#create a display of 800*600
#gameDisplay = pygame.display.set_mode((800,600))
gameDisplay = pygame.display.set_mode((display_width,display_height))

#set Title name
pygame.display.set_caption("Car Race")

#set clock rate
clock = pygame.time.Clock()

#load  car image
carImg=pygame.image.load(r'C:\Users\Abhinav Jain\Pictures\car.png')
enmcar=pygame.image.load(r'C:\Users\Abhinav Jain\Pictures\ene.png')
carI=pygame.image.load(r'C:\Users\Abhinav Jain\Pictures\g.png')
pygame.display.set_icon(carI)
def score(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Score:"+str(count),True,black)
    gameDisplay.blit(text,(0,0))
def things(thingx,thingy):
    gameDisplay.blit(enmcar,(thingx,thingy))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))# blit use to display image which is loaded

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashsound)
    message_display('You Crashed')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again",150,450,200,50,(0,200,0),(0,255,0))
        button("Quit",550,450,200,50,(200,0,0),(255,0,0))
        pygame.display.update()
        clock.tick(15)
def button(msg,x,y,w,h,ic,ac):
    global pause
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if(x+w>mouse[0]>x and y+h>mouse[1]>y ):
        #print(click)
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if((msg=="GO" or msg=="Play Again") and click[0]==1):
            gameloop()
        elif(msg=="Quit" and click[0]==1):
            pygame.quit()
            quit()
        elif(msg=="Continue" and click[0]==1):
            pause=False
            pygame.mixer.music.unpause()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText=pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center=((x+w/2),(y+h/2))
    gameDisplay.blit(textSurf,textRect)

def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects("Paused",largeText)
    TextRect.center=((display_width/2,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue",150,450,200,50,(0,200,0),(0,255,0))
        button("Quit",550,450,200,50,(200,0,0),(255,0,0))
        pygame.display.update()
        clock.tick(15)
def gameintro():
    intro =True
    pygame.mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("Lets Race",largeText)
        TextRect.center=((display_width/2,display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("GO",150,450,100,50,(0,200,0),(0,255,0))
        button("Quit",550,450,100,50,(200,0,0),(255,0,0))
        pygame.display.update()
        clock.tick(15)
               

def gameloop():
    global pause
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r"SoundTrack\start.wav")
    pygame.mixer.music.play(-1)
    x=(display_width*0.45)
    y=(display_height*0.8)
    car_width=100
    car_height=106
    xchange=0
    Life=3
    Level=1
    color=(0,0,0)
    thing_startx=random.randrange(0,display_width-car_width)
    thing_starty=-600
    thing_speed=7
    scor=0
    gameExit=False
    #main game loop 
    while not gameExit:

        for event in pygame.event.get(): # list of event like mouse movement click kbhit
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: # when key press
                if event.key == pygame.K_LEFT:
                    xchange=-5
                if event.key == pygame.K_RIGHT:
                    xchange=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type == pygame.KEYUP:  #when key release
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange=0

        
        x+=xchange    
        gameDisplay.fill(white)
        things(thing_startx,thing_starty)
        thing_starty+=thing_speed
        car(x,y)
        score(scor)
        if x>display_width - car_width or x<0:
            crash()
        if thing_starty >display_height:
            thing_starty=0-car_height
            scor+=1
            thing_speed+=1
            #thing_width+=(scor*1)
            thing_startx=random.randrange(0,display_width-car_width)
                   
            
        if y<thing_starty+car_height:
            if x>thing_startx and x<thing_startx+ car_width or x+car_width > thing_startx and x+car_width< thing_startx+car_width   :
                crash()
                thing_starty=0-car_width
                thing_startx=random.randrange(0,display_width)
        pygame.display.update() #just update the frame
        #pygame.display.flip() change the whole frame
        # set fps
        clock.tick(60)
gameintro()
#pygame.quit()# quit pygame
#quit()#quit python program







  
