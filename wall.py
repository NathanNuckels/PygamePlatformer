#NATHANATORBOT
#-------------------------------------------------------------------------------------
import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
def newWall(x,y,width,height,wallList,spriteList):
    wall= Wall(x,y,width,height)
    wallList.add(wall)
    spriteList.add(wall)
#-------------------------------------------------------------------------------------
