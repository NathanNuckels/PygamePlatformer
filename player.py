#NATHANATORBOT
#-------------------------------------------------------------------------------------
import pygame
class Player(pygame.sprite.Sprite):
    right = False
    left = False
    up = False
    down = False
    speed = 0
    def __init__(self,x,y,w,h,color):
        super().__init__()
        self.image = pygame.Surface([w,h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.deltaX = 0
        self.deltaY = 0
        self.room = None
    def keydown(self,key,speed):
        self.speed = speed
        if key == pygame.K_LEFT:
            self.left = True
        if key == pygame.K_RIGHT:
            self.right = True
        if key == pygame.K_UP:
            self.up= True
        if key == pygame.K_DOWN:
            self.down = True
    def keyup(self,key):
        if key == pygame.K_LEFT:
            self.left = False
        if key == pygame.K_RIGHT:
            self.right = False
        if key == pygame.K_UP:
            self.up = False
        if key == pygame.K_DOWN:
            self.down = False
    def update(self):
        if self.left:
            self.deltaX = -self.speed
        if self.right:
            self.deltaX = self.speed
        if self.up:
            self.deltaY = -self.speed
        if self.down:
            self.deltaY = self.speed
        if not self.left and not self.right:
            self.deltaX = 0
        if not self.up and not self.down:
            self.deltaY = 0
        self.rect.x += self.deltaX
        collisions = pygame.sprite.spritecollide(self,self.room.collition_blocks,False)
        for hit in collisions:
            if self.deltaX > 0:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right
        self.rect.y += self.deltaY
        collisions = pygame.sprite.spritecollide(self,self.room.collition_blocks,False)
        for hit in collisions:
            if self.deltaY > 0:
                self.rect.bottom = hit.rect.top
            else:
                self.rect.top = hit.rect.bottom
    def set_room(self,room):
        self.room = room
#-------------------------------------------------------------------------------------
