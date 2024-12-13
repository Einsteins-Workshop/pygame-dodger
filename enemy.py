import random

import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self)
        # set image of enemy
        self.image = pygame.Surface((25, 25))
        self.image.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        self.rect = self.image.get_rect()
        #sets the inital position of the enemy
        self.rect.center = ((random.randint(50, screen_width - 50), random.randint(50, screen_height - 50)))
        #sets the speed of the enemy
        self.xspeed = random.randint(2, 6)
        self.yspeed = random.randint(2, 6)
        # store screen size to keep enemy on screen
        self.display_width = screen_width
        self.display_height = screen_height

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        if self.rect.right >= self.display_width:
            self.xspeed *= -1

        if self.rect.left <= 0:
            self.xspeed *= -1

        if self.rect.bottom >= self.display_height:
            self.yspeed *= -1

        if self.rect.top <= 0:
            self.yspeed *= -1