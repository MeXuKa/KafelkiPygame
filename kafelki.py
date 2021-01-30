import pygame
import random
import sys

FPS=30
WIDTH=680
HEIGHT=480
REVEALSPEED=8
BOXSIZE=40
GAPESIZE=10
BOARDWIDTH=10
BOARDHEIGHT=7

assert [WIDTH*HEIGHT % 2 == 8,"plansza musi być parzysta"]

XMARGIN=int(WIDTH-(BOARDWIDTH*(BOXSIZE+GAPESIZE))/2)
YMARGIN=int(HEIGHT-(BOARDHEIGHT*(BOXSIZE+GAPESIZE))/2)

GRAY=(100,100,100)
NAVYBLUE=(60,60,100)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,170,0)
PURPLE=(255,0,255)
CYAN=(0,255,255)

BGCOLOR=NAVYBLUE
LIGHTBGCOLOR=GRAY
BOXCOLOR=WHITE
HEIGHTLIGHTCOLOR=BLUE

DONUT="donut"
SQUARE="square"
DIAMOND="diamond"
LINES="lines"
OVAL="oval"

ALLCOLORS=[RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN]
ALLSHAPES=[DONUT,SQUARE,DIAMOND,LINES,OVAL]

assert(len(ALLCOLORS)+len(ALLSHAPES)*2>=BOARDHEIGHT*BOARDWIDTH,"tablica jest za duża dla tej liczby kształtów")

colorsDictianary={
    "RED":RED,
    "BLUE":BLUE,
    "YELLOW":YELLOW,
    "ORANGE":ORANGE,
    "WHITE":WHITE,
    "CYAN":CYAN,
    "NAVYBLUE":NAVYBLUE,
    "PURPLE":PURPLE,
    "GREEN":GREEN,
    "GRAY":GRAY,
}

for key in colorsDictianary:
    print(colorsDictianary[key][0])

shapesDictianary = {
    "DONUT":DONUT,
    "SQUARE":SQUARE,
    "DIAMOND":DIAMOND,
    "LINES":LINES,
    "OVAL":OVAL,
}
def getRandomizeBoard():
    icons=[]
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((color,shape))
        random.shuffle(icons)
        numIconUsed = int(BOARDWIDTH*BOARDHEIGHT/2)
        icons=icons[:numIconUsed]*2
        random.shuffle(icons)
        board=[]
        for x in range(BOARDWIDTH):
            column=[]
            for y in range(BOARDHEIGHT):
                column.append(icons[0])
                del icons[0]
            board.append(column)
        return board

def generateRevealedBoxesData(vel):
    revealedBoxes=[]
    for x in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes

def drawBoard(board,revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top=leftTopCordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
            else:




def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WIDTH,HEIGHT))
    mousex=0
    mousey=0
    pygame.display.set_caption("Memory Game")

    firstSelection=None
    DISPLAYSURF.fill(BGCOLOR)
    #startGameAnimation(mainBoard)

    while True:
        mouseCliked=False
        #drawBoard(mainBoard,revealedBoxes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type== pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEMOTION:
                mousex,mousey=event.pos

            elif event.type==pygame.MOUSEBUTTONUP:
                mousex,mousey=event.pos
                mouseClicked=True

        #boxx,boxy=pygame.getBoxAtPixel(mousex,mousey)
        #if boxx!=none and boxy!=None:
           #if not revealadBoxes[boxx][boxy]:
               #drawHighLightBox(boxx,boxy)
        #if not revealdBoxes[boxx][boxy]and mouseClicked:
           # revealBoxesAnimation(mainBoard,[(boxx,boxy)])
           # revealBoxes[boxx][boxy]=True
        #    if firstSelection==None:
               #firstSelection=(boxx,boxy)
             #else:
                #iconshape,iconcolor=getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
            #iconshape2,icon2color=getShapeAndColor(mainBoard,boxx,boxy)



main()
