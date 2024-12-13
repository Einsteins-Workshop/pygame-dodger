import random
import pygame
from os import path

class Player(pygame.sprite.Sprite):

    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self)
        # define how it looks

        # setup assets folders
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")

        # use image from img file as player
        self.player_img = pygame.image.load(path.join(img_folder, "player_image.png")).convert()
        self.image = pygame.transform.scale(self.player_img,(50,50))
        self.image.set_colorkey((0, 0, 0))
        # set bounding box based on image size
        self.rect = self.image.get_rect()
        #set initial position and speed
        self.rect.center = ((random.randint(50, screen_width - 50), random.randint(50, screen_height - 50)))
        self.x_speed = 0
        self.y_speed = 0
        # save screen decisions for later
        self.display_width = screen_width
        self.display_height = screen_height
        self.speed = 4

    def update(self):
        #make sure player stays on screenn during update
        # off right size?
        if self.rect.right >= self.display_width:
            self.x_speed *= -1
            self.rect.right = self.display_width - 1
        # off left side?
        if self.rect.left <= 0:
            self.x_speed *= -1
            self.rect.left = 0 + 1
        # has the bottom of our player left the bottom of the screen
        if self.rect.bottom >= self.display_height:
            self.y_speed *= -1
            self.rect.bottom = self.display_height -1
            # has the top of our player left the top of the screen
        if self.rect.top <= 0:
            self.y_speed *= -1
            self.rect.top = 0 + 1

        # update player pos based on speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    #player movement using keys
    def moveLeft(self):
        #set xspeed to negative number
        self.x_speed = -self.speed


    def moveRight(self):
        #set xspeed to postive number
        self.x_speed = self.speed

    def moveUp(self):
        #set yspeed to a negative number
        self.y_speed = -self.speed

    def moveDown(self):
        #set yspeed to positive number
        self.y_speed = self.speed

    def moveStopX(self):
        #stop the player from moving in x direction
        self.x_speed = 0

    def moveStopY(self):
        # stop the player from moving in y direction
        self.y_speed = 0
