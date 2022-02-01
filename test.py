
# game 
import pygame, sys
from pygame.locals import *

pygame.init()

#setting up the refresh rate
FPS = 30
fpsClock = pygame.time.Clock()

# set the size of the display window in pixels
screen = pygame.display.set_mode((800, 600))

# change the caption of the display window
pygame.display.set_caption("Laura's game")

#define colour tuples in the form colourname = (R,G,B)
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)

gamefont = pygame.font.SysFont("comicsans",48)
gamefont2 = pygame.font.SysFont("comicsans",24)

map = pygame.image.load("map.png")
map = pygame.transform.scale(map,(820,500))

mode = pygame.image.load("startbutton.png")
mode = pygame.transform.scale(mode,(700,600))

credits = pygame.image.load("creditsbutton.png")
credits = pygame.transform.scale(credits,(700,600))

one =  pygame.image.load("1.png")
one = pygame.transform.scale(one,(500,400))

two =  pygame.image.load("2.png")
two = pygame.transform.scale(two,(500,400))

three =  pygame.image.load("3.png")
three = pygame.transform.scale(three,(500,400))

four =  pygame.image.load("4.png")
four = pygame.transform.scale(four,(500,400))

five =  pygame.image.load("5.png")
five = pygame.transform.scale(five,(500,400))

six =  pygame.image.load("6.png")
six = pygame.transform.scale(six,(500,400))

title = pygame.image.load("title.png")
title = pygame.transform.scale(title,(700,500))

earth = pygame.image.load("earth.png")
earth = pygame.transform.scale(earth,(1000,600))

creditstext = pygame.image.load("credits.png")
creditstext = pygame.transform.scale(creditstext,(700,500))

correct = pygame.image.load("correct.png")
correct = pygame.transform.scale(correct,(550,400))

wrong = pygame.image.load("wrong.png")
wrong = pygame.transform.scale(wrong,(550,400))

question = pygame.image.load("question.png")
question = pygame.transform.scale(question,(550,400))

chart = pygame.image.load("chart.png")
chart = pygame.transform.scale(chart,(550,400))

font1 =pygame.font.Font("font.ttf",30);
font = pygame.font.SysFont("comicsans",48)

answerdone = True 
gameactive = False 
buttonactive = False
time = 600
score = 0 
answertime = 0 

import random
continents = ["North America","Africa","South America","Australia","Asia","Europe"]
easyquestions = ["North America","South america","Asia","Europe","Australia","Africa"]
mediumquestions= ["Canada","Germany","Italy","Spain","France","China","Russia","India","Mexico","Egypt","Nigeria","Poland"]
hardquestions= ["Colombia","Eithopia","Argentina","Pakistan","Cuba","Mongolia","Algeria","Urugay","Rwanda","Croatia","Taiwan","Peru"]

def randomizer():
    choice = easyquestions[random.randint(0,5)]
    return choice

def randomizer2():
    choice2 = mediumquestions[random.randint(0,10)]
    return choice2

def randomizer3():
    choice3 = hardquestions[random.randint(0,11)]
    return choice3


def game1 ():
    global map 
    global time
    global score
    global choice
    global notdone
    screen.blit(map,(0,0))    
    time -= 1

    screen.blit(one,(50,80))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 117 < mouseX <167 and 145 < mouseY < 167: 
            answerdone = True
            continentchoice = "North America"
            correctchoice = choice
            if continentchoice == correctchoice:
                screen.blit(correct,(40,80))
                score += 10
            else:
                screen.blit(wrong,(40,80))
                score -= 10 

    screen.blit(two,(292,220))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 362 < mouseX <408 and 284 < mouseY < 304:
            answerdone = True 
            continentchoice = "Africa"
            correctchoice = choice
            if continentchoice == correctchoice:
                screen.blit(correct,(282,220))
                score += 10
            else:
                screen.blit(wrong,(282,220))
                score -= 10 

    screen.blit(three,(150,270))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 219 < mouseX <259 and 332 < mouseY < 358:
            answerdone = True 
            continentchoice = "South America"
            correctchoice = choice
            if continentchoice == correctchoice:
                screen.blit(correct,(140,270))
                score += 10
            else:
                screen.blit(wrong,(140,270))
                score -= 10 

    screen.blit(four,(570,310))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 640 < mouseX <689 and 375 < mouseY < 398:
            answerdone = True  
            continentchoice = "Australia"
            correctchoice = choice
            if continentchoice == correctchoice:
                screen.blit(correct,(560,310))
                score += 10
            else:
                screen.blit(wrong,(560,310))
                score -= 10 

    screen.blit(five,(550,80))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 618 < mouseX <671 and 141 < mouseY < 166:
            answerdone = True 
            continentchoice = "Asia"
            correctchoice = choice
            if continentchoice == correctchoice:
                screen.blit(correct,(540,80))
                score += 10
            else:
                screen.blit(wrong,(540,80))
                score -= 10 

    screen.blit(six,(300,70))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 370 < mouseX <415 and 135 < mouseY < 160:
            answerdone = True  
            continentchoice = "Europe"
            correctchoice = choice
            if continentchoice == correctchoice:
                notdone = False
                screen.blit(correct,(290,70))
                score += 10
            else:
                screen.blit(wrong,(290,70))
                score -= 10 

def modebutton():
    global gameactive
    screen.blit(mode,(140,70))
    for event in pygame.event.get():
        if event.type ==MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX,mouseY = pygame.mouse.get_pos()
                if 300 < mouseX <500 and 250 < mouseY < 350:
                    gameactive = True
                    
def creditsbutton():
    global buttonactive 
    screen.blit(credits,(35,220))
    if pygame.mouse.get_pressed()[0] == 1:
        mouseX,mouseY = pygame.mouse.get_pos()  
        if 300 < mouseX <505 and 364 < mouseY < 460:  

            if gameactive == False:
                buttonactive = True

while True:
    notdone = True

    choice = randomizer()
    choice2 = randomizer2()
    choice3 = randomizer3()

    easyquestionstext = font1.render(str(choice),True,Black)
    mediumquestionstext = font1.render(str(choice2),True,Black)
    hardquestionstext = font1.render(str(choice3),True,Black)
    
    while notdone:
        timetext = font1.render(str(time),True,Black)
        scoretext = font1.render(str(score),True,Black)
        screen.blit(earth,(-110,0))
        screen.blit(title,(70,40))
        creditsbutton()
        modebutton()

        if gameactive == True:
            game1()
            screen.blit(question,(-40,250))
            screen.blit(chart,(415,250))
            screen.blit(timetext,(682,544))
            screen.blit(scoretext,(582,544))
        
        if answerdone == True:
            
            if score <= 50:
                screen.blit(easyquestionstext,(60,544))
            elif score >= 70:
                screen.blit(mediumquestionstext,(60,544))
            elif score >= 80:
                screen.blit(hardquestionstext,(60,544))
        if answertime >= 10:
            answertime == 0
            answerdone = False

        if buttonactive == True:
            screen.fill(White)
            screen.blit(creditstext,(40,50)) 
        # if score == -10:
        #     screen.fill(Black)
        #     break
        if score == 300:
            screen.fill(White)
            break
        if time == -10:
            screen.fill(Black)
            break

        mouseX,mouseY = pygame.mouse.get_pos()
        print(mouseX, mouseY)

        for event in pygame.event.get():
            if event.type == QUIT:   # Check if user closes window
                pygame.quit()
                sys.exit()
            
        # update the display window

        pygame.display.update()
        fpsClock.tick(FPS)
