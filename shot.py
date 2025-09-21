import circleshape
import pygame

from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt