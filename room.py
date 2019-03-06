#NATHANATORBOT
#INIT---------------------------------------------------------------------------------
import pygame
from wall import Wall
lightblue = (0,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
def createRoom(filename):
    walls=[]
    with open(filename,'r') as f:
        lines = f.readlines()
        row = 0
        for line in lines:
            line = line.strip()
            x = 0
            y = 0
            width = 20
            height = 20
            column = 0
            for char in line:
                x = width *column
                y = height * row
                if char ==".":
                    color = black
                elif char == "r":
                    color=red
                elif char == "g":
                    color = green
                elif char == "b":
                    color = blue
                else:
                    color = white
                walls.append((x,y,width,height,color,char))
                column+=1
            row+=1
        return walls
class Room(object):
    wall_list =None
    coin_list = None
    screen_width: int = 0
    screen_height: int = 0
    def __init__(self,screenWidth,screenHeight,filename):
        self.wall_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.screen_width = screenWidth
        self.screen_height = screenHeight
        walls = createRoom(filename)
        for item in walls:
            if item[5] is not ".":
                wall = Wall(item[0],item[1],item[2],item[3],item[4])
                self.wall_list.add(wall)
#-------------------------------------------------------------------------------------
