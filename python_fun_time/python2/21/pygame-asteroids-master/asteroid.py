import pygame
from utils import Location
import random

class Asteroid(object):
    def __init__(self):
        self.location = Location(0,0)
        self.reset() #Randomly pick a starting location

        self.size = Location(40,40)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("asteroid.png").convert()
        self.sprite.rect = self.sprite.image.get_rect()

    def update(self):
        self.location.y += 10
        if self.location.y > 500:
            self.reset()

    def reset(self):
        # We have reached the bottom of the screen so reset
        self.location.y = 0
        self.location.x = random.randint(0, 560)

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())

    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y and diffy > (self.size.y * -1):
                return True
        return False
