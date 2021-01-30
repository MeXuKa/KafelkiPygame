import pygame
import random

#Const
SCREEN_WIDTH=600
SCREEN_HEIGHT=500
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
FPS=60

pygame.init()
#class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(playerImage,(50,50))
        #self.image=pygame.Surface((50,50))
        #self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.points=0
        self.hp=100
    def update(self):
        self.velocityX = 0
        keylistening = pygame.key.get_pressed()
        if keylistening[pygame.K_d]:
            self.velocityX += 8
        if keylistening[pygame.K_a]:
            self.velocityX -= 8
        self.rect.x += self.velocityX
        self.velocityY = 0
        keylistening=pygame.key.get_pressed()
        if keylistening[pygame.K_w]:
            self.velocityY -=8
        if keylistening[pygame.K_s]:
            self.velocityY +=8
        self.rect.y += self.velocityY

        if self.rect.left>SCREEN_WIDTH:
            self.rect.right=0
        if self.rect.right<0:
            self.rect.left=SCREEN_WIDTH

        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def UpdateHP (self,value):
            self.hp += value



    def GetHP(self):
            return self.hp

    def Shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.y-5)
        allSprites.add(bullet)
        bullets.add(bullet)
    def UpdatePoints(self,value):
        self.points+=value
    def GetPoints(self):
        return self.points




class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bulletImage,(10,20))
        #self.image=pygame.Surface((30,10))
        #self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.velocityY=-10
    def update(self):
        self.rect.y+=self.velocityY
        if self.rect.bottom<-10:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(enemyImage,(50,50))
        #self.image=pygame.Surface((35,35))
        #self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(SCREEN_WIDTH-self.rect.width)
        self.rect.y=(random.randrange(-1000,-10))
        self.velocityY = random.randrange(1,10)
    def update(self):
        self.rect.y += self.velocityY
        if self.rect.top>SCREEN_HEIGHT+10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = (random.randrange(-1000, -10))
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(enemyImage,(100,100))
        #self.image=pygame.Surface((35,35))
        #self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(SCREEN_WIDTH-self.rect.width)
        self.rect.y=(random.randrange(-1000,-10))
        self.velocityY = random.randrange(1,10)
    def update(self):
        self.rect.y += self.velocityY
        if self.rect.top>SCREEN_HEIGHT+10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = (random.randrange(-1000, -10))

def UpdateHealthBar(value):
    x=pygame.Surface((50,20))
    return x

#variables
background=pygame.image.load("images/space4.png")
background_rect=background.get_rect()
playerImage=pygame.image.load("images/enemyGreen3.png")
enemyImage=pygame.image.load("images/meteorBrown_med3.png")
bulletImage=pygame.image.load("images/laserRed07.png")
bossImage=pygame.image.load("images/enemyRed3.png")

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders v0.0.1")
loop=True
timer = pygame.time.Clock()

healthBar=pygame.Surface((100,20))
healthBar.fill(RED)
healthBarContainer=healthBar.get_rect()
healthBarContainer.x=10
healthBarContainer.y=SCREEN_HEIGHT-10

player = Player()
allSprites = pygame.sprite.Group()
allSprites.add(player)
enemies=pygame.sprite.Group()
bullets=pygame.sprite.Group()
boss=pygame.sprite.Group()

for x in range(8):
    enemy=Enemy()
    allSprites.add(enemy)
    enemies.add(enemy)

pointsText = "Points:"+ str(player.GetPoints())
font = pygame.font.SysFont("Ariel", 30)
pointsInfo = font.render(pointsText, True, BLACK)
pointsInfo_container = pointsInfo.get_rect()
pointsInfo_container.x = 5
pointsInfo_container.y = 5

#Game LOOP:

while loop:
    timer.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.Shoot()
    allSprites.update()
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if hits:

        player.UpdatePoints(10)
        pointsText = "Points:"+ str(player.GetPoints())
        font = pygame.font.SysFont("Ariel", 30)
        pointsInfo = font.render(pointsText, True, BLACK)
        pointsInfo_container = pointsInfo.get_rect()
        pointsInfo_container.x = 5
        pointsInfo_container.y = 5
    if player.GetPoints()<100:
        for hit in hits:
            e=Enemy()
            allSprites.add(e)
            enemies.add(e)
    if player.GetPoints()>50:
        b=Boss()
        allSprites.add(e)


    hits=pygame.sprite.spritecollide(player, enemies, True)
    if hits:
        player.UpdateHP(-35)
        if (player.GetHP()<0):
            loop=False
        if healthBar.get_width() -35 >=0:
            healthBar=pygame.Surface((healthBar.get_width()-35,10))
        healthBar.fill(RED)
        healthBarContainer=healthBar.get_rect()
        healthBarContainer.x=10
        healthBarContainer.y=SCREEN_HEIGHT-20





    screen.fill(BLACK)
    screen.blit(background, background_rect)
    screen.blit(pointsInfo,pointsInfo_container)
    screen.blit(healthBar,healthBarContainer)
    allSprites.draw(screen)
    pygame.display.flip()



pygame.quit()