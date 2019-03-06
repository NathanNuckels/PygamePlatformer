#NATHANATORBOT
#INIT---------------------------------------------------------------------------------
import pygame
import sys
from player import Player
from room import Room
#lesson1.room
#from pygame import stuff
colors={"screen":(144,219,255),"walls":(0,0,204),"player":(0,204,102)}
sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
wallSize = 10
screenWidth = 1280
screenHeight = 720
curentRoom = 0
rooms=[Room(screenWidth,screenHeight,"level1.txt"), Room(screenWidth,screenHeight,"level1.txt")]
def shift_room(direction,player):
    global curentRoom
    if direction == "left":
        curentRoom -= 1
        player.rect.x = screenWidth - player.rect.width - 5
    if direction == "right":
        curentRoom += 1
        player.rect.x = player.rect.width + 5
    if curentRoom < 0:
        curentRoom = len(rooms)-1
    elif curentRoom >= len(rooms):
        curentRoom = 0
def main():
    global curentRoom
    pygame.init()
    screen = pygame.display.set_mode([screenWidth,screenHeight])
    pygame.display.set_caption("Walls and rooms")
    sprites = pygame.sprite.Group()
    player = Player(100,50,70,70,colors["player"])
    clock = pygame.time.Clock()
    curentRoom = 0
    done = False
    sprites.add(player)
    #GAME LOOP----------------------------------------------------------------------------
    while not done:
        #EVENT PROSESING-----------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                player.keydown(event.key,5)
            elif event.type == pygame.KEYUP:
                player.keyup(event.key)
        #GAME LOGIC----------------------------------------------
        player.set_room(rooms[curentRoom])
        sprites.update()
        rooms[curentRoom].update()
        if player.rect.x <= -player.rect.width:
            shift_room("left",player)
        elif player.rect.x >= screenWidth+player.rect.width:
            shift_room("right",player)
        #DRAWING-------------------------------------------------
        rooms[curentRoom].draw(screen)
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
if __name__ == '__main__':
    main()
        
    #END----------------------------------------------------------------------------------
    pygame.quit()
    sys.exit()
