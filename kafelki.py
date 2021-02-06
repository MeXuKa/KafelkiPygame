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
        revealedBoxes.append([vel]*BOARDHEIGHT)
    return revealedBoxes

def leftTopCordsOfBox(boxx,boxy):
    left = boxx * (BOXSIZE * BOXSIZE) + XMARGIN
    top = boxy * (BOXSIZE * BOXSIZE) + YMARGIN
    return (left,top)

def getShapeAndColor(board,boxx,boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawIcon(shape,color,boxx,boxy):
    quarter=int(BOXSIZE * 0.25)
    half=int(BOXSIZE * 0.5)

    left,top=leftTopCordsOfBox(boxx,boxy)
    if shape==DONUT:
        pygame.draw.circle(DISPLAYSURF,color,(left+half,top+half),half-5)
        pygame.draw.circle(DISPLAYSURF,BGCOLOR,(left+half,top+half), quarter -5)
    elif shape==SQUARE:
        pygame.draw.rect(DISPLAYSURF,color(left+quarter,top+quarter,BOXSIZE - half,BOXSIZE - half))
    elif shape==DIAMOND:
        pygame.draw.polygon(DISPLAYSURF,color,((left+half,top),(left+BOXSIZE-1,top+half),(left+half,top+BOXSIZE-1),(left,top+half)))
    elif shape==LINES:
        for i in range(0,BOXSIZE,4):
            pygame.draw.lines(DISPLAYSURF,color(left,top+i)(left+1,top))
            pygame.draw.lines(DISPLAYSURF,color(left+i,top+BOXSIZE-1),left+BOXSIZE-1,top*1)
    elif shape.color==OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color,(left,top+quarter,BOXSIZE,half))


def drawBoard(board,revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top=leftTopCordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
            else:
                shape,color= getShapeAndColor(board,boxx,boxy)
                drawBoard(shape,color,boxx,boxy)


def getBoardPixel(x,y):
    for boxx in range (BOARDHEIGHT):
        for boxy in range(BOARDHEIGHT):
            left,top=leftTopCordsOfBox(boxx,boxy)
            boxRect=pygame.Rect(left,top,BOXSIZE,BOXSIZE)
            if boxRect.collisidepoint(x,y):
                return(boxy,boxx)
    return(None,None)

def drawHighLightBox(boxx,boxy):
    left,top=leftTopCordsOfBox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HEIGHTLIGHTCOLOR,(left-5,top-5,BOXSIZE+10,BOXSIZE+10),4)

def splitIntoGroups(groupSize,theList):
    result=[]
    for i in range(0,len(theList),groupSize):
        result.append(theList[1:i+groupSize])
    return result

def drawBoxCovers(board,boxes,coverage):
    for box in boxes:
        left,top=leftTopCordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,BOXSIZE,BOXSIZE))
        shape,color=getShapeAndColor(board,box[0],box[1])
        drawIcon(shape,color,box[0],box[1])
        coverage.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,coverage,BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board,boxesToReveal):
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)

def startGameAnimation(board):
    coveredBoxes=generateRevealedBoxesData(False)
    boxes=[]
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))
        random.shuffle(boxes)
        boxGroups=splitIntoGroups(0,boxes)
        drawBoard(board,coveredBoxes)
        for boxGroups in boxGroups:
            revealBoxesAnimation


def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WIDTH,HEIGHT))
    mousex=0
    mousey=0
    pygame.display.set_caption("Memory Game")
    revealedBoxes=generateRevealedBoxesData(False)
    firstSelection=None
    DISPLAYSURF.fill(BGCOLOR)

    mainBoard=getRandomizeBoard()
    startGameAnimation(mainBoard)

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

        boxx,boxy=pygame.getBoxAtPixel(mousex,mousey)
        if boxx!=None and boxy!=None:
           if not revealedBoxes[boxx][boxy]:
               drawHighLightBox(boxx,boxy)
        if not revealedBoxes[boxx][boxy]and mouseClicked:
            revealBoxesAnimation(mainBoard,[(boxx,boxy)])
            revealedBoxes[boxx][boxy]=True
            if firstSelection==None:
                firstSelection=(boxx,boxy)
            else:
                iconshape,iconcolor=getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                iconshape2,icon2color=getShapeAndColor(mainBoard,boxx,boxy)



main()
