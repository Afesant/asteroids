import pygame
import player
import asteroid
import asteroidfield
import shot
from constants import *

def main():
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    
    new_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    new_asteroid_field = asteroidfield.AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for asteroid_object in asteroids:
            if new_player.check_collision(asteroid_object):
                print("Game over!")
            for shot_object in shots:
                if shot_object.check_collision(asteroid_object):
                    shot_object.kill()
                    asteroid_object.split()

        screen.fill('black', rect=None, special_flags=0)
        """ new_player.draw(screen)
        new_player.update(dt) """
        for entity in drawable:
            entity.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        delta_return  = clock.tick(60)
        dt = delta_return/1000

if __name__ == "__main__":
    main()
