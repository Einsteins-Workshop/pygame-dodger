import random

import pygame

class Enemy2(pygame.sprite.Sprite):

    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self)
        # set image of enemy
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        #sets the inital position of the enemy
        self.rect.center = ((random.randint(50, screen_width - 50), random.randint(-400, -100)))
        #sets the speed of the enemy
        self.xspeed = 0
        self.yspeed = random.randint(2, 6)
        # store screen size to keep enemy on screen
        self.display_width = screen_width
        self.display_height = screen_height

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        # remove sprite when it leaves the bottom of the screen
        if(self.rect.top > self.display_height):
            self.kill()


