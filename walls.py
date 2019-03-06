import pygame
import sys
#from pygame import stuff
colors={"screen":(144,219,255),"walls":(0,0,204),"player":(0,204,102)}
sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
wallSize = 10
screenWidth = 1280
screenHeight = 720
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(colors["player"])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.deltaX = 0
        self.deltaY = 0
        self.walls = None
    def keydown(self,key,speed):
        if key == pygame.K_LEFT:
            self.deltaX = -speed
        if key == pygame.K_RIGHT:
            self.deltaX = speed
        if key == pygame.K_UP:
            self.deltaY = -speed
        if key == pygame.K_DOWN:
            self.deltaY = speed
    def keyup(self,key):
        if key == pygame.K_LEFT:
            self.deltaX = 0
        if key == pygame.K_RIGHT:
            self.deltaX = 0
        if key == pygame.K_UP:
            self.deltaY = 0
        if key == pygame.K_DOWN:
            self.deltaY = 0
    def update(self):
        self.rect.x += self.deltaX
        collisions = pygame.sprite.spritecollide(self,self.walls,False)
        for hit in collisions:
            if self.deltaX > 0:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right
        self.rect.y += self.deltaY
        collisions = pygame.sprite.spritecollide(self,self.walls,False)
        for hit in collisions:
            if self.deltaY > 0:
                self.rect.bottom = hit.rect.top
            else:
                self.rect.top = hit.rect.bottom
        
        

        
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colors["walls"])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def newWall(x,y,width,height,wallList,spriteList):
    wall= Wall(x,y,width,height)
    wallList.add(wall)
    spriteList.add(wall)

    
pygame.init()
screen = pygame.display.set_mode([screenWidth,screenHeight])
pygame.display.set_caption("the wall game")
newWall(0,0,wallSize,screenHeight,walls,sprites)
newWall(0,0,screenWidth,wallSize,walls,sprites)
newWall(0,screenHeight-wallSize,screenWidth,screenHeight,walls,sprites)#!!!
newWall(screenWidth-wallSize,0,wallSize,screenHeight,walls,sprites)
player = Player(wallSize,wallSize)
player.walls = walls
sprites.add(player)
clock=pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player.keydown(event.key,5)
        elif event.type == pygame.KEYUP:
            player.keyup(event.key)
    sprites.update()
    screen.fill(colors["screen"])
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()


