import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.randint(20, 50)
            first_asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
            first_asteroid.velocity = self.velocity.rotate(angle)
            first_asteroid.radius = self.radius - ASTEROID_MIN_RADIUS
            
            second_asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
            second_asteroid.velocity = self.velocity.rotate(-angle)
            second_asteroid.radius = self.radius - ASTEROID_MIN_RADIUS
            return first_asteroid, second_asteroid
            