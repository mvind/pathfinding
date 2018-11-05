import pygame
import sys
# Goal: Create nxm grid in pygame 

class Grid(pygame.sprite.Sprite):
    _dimension = [20, 20]
    
    def __init__(self, xpos, ypos):
        super().__init__()
        self._color = (211, 211, 211)
        self.xpos = xpos
        self.ypos = ypos

        self.image = pygame.Surface(self._dimension)
        self.image.fill(self._color, rect=pygame.Rect(1,1, 19,19))
        self.rect = self.image.get_rect()

        self.start = False
        self.end = False
        self.wall = False
        
    def update(self):
        # Update position and color
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.image.fill(self._color, rect=pygame.Rect(1,1, 19,19))
