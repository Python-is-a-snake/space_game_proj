import pygame
#sprites was made with PIXILART : https://www.pixilart.com
#class of 1 alien
class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien_octo.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

#Printing aliens
    def draw(self):
        self.screen.blit(self.image, self.rect)

#Aliens movement
    def update(self):
        self.y += 0.1
        self.rect.y = self.y


