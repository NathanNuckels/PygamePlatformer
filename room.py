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
            can_colide = True
            image = None
            for char in line:
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
                walls.append((x,y,width,height,color,char))
                column+=1
            row+=1
        return background_blocks, collition_blocks
class Room(object):
    '''wall_list =None
    coin_list = None'''
    background_Blocks = None
    collition_blocks = None
    screen_width: int = 0
    screen_height: int = 0
    def __init__(self,screenWidth,screenHeight,filename):
        '''self.wall_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()'''
        self.screen_width = screenWidth
        self.screen_height = screenHeight
        '''walls = createRoom(filename)
        for item in walls:
            if item[5] is not ".":
                wall = Wall(item[0],item[1],item[2],item[3],item[4])
                self.wall_list.add(wall)'''
#-------------------------------------------------------------------------------------
