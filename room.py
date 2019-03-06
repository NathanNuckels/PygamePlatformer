#NATHANATORBOT
#INIT---------------------------------------------------------------------------------
import pygame
from block import Block
lightblue = (0,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
def createRoom(filename):
    background_blocks = pygame.sprite.Group()
    collition_blocks = pygame.sprite.Group()
    
    with open(filename,'r') as f:
        lines = f.readlines()
        row = 0
        for line in lines:
            line = line.strip()
            x = 0
            y = 0
            width = 70
            height = 70
            column = 0
            for char in line:
                image = None
                can_colide = True
                x = width *column
                y = height * row
                if char ==".":
                    color = black
                    can_colide = False
                elif char == "r":
                    color=red
                elif char == "g":
                    color = green
                elif char == "b":
                    color = blue
                else:
                    color = white
                block = Block(x,y,width,height,color,image,can_colide)
                if can_colide:
                    collition_blocks.add(block)
                else:
                    background_blocks.add(block)
                column+=1
            row+=1
        return background_blocks, collition_blocks
class Room(object):
    '''wall_list =None
    coin_list = None'''
    background_Blocks = None
    background_color = white
    collition_blocks = None
    screen_width: int = 0
    screen_height: int = 0
    def __init__(self,screenWidth,screenHeight,filename):
        self.background_blocks, self.collition_blocks = createRoom(filename)
        self.screen_width = screenWidth
        self.screen_height = screenHeight
    def update(self):
        self.background_blocks.update()
        self.collition_blocks.update()
    def draw(self,screen):
        screen.fill(self.background_color)
        self.background_blocks.draw(screen)
        self.collition_blocks.draw(screen)
#-------------------------------------------------------------------------------------
