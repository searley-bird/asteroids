import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    player.shot_group = shot_group
    
    updatable.add(player, shot_group)
    drawable.add(player,shot_group)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for shot in shot_group:
            shot.update(dt)

        for asteroid in asteroids:
            for shot in shot_group:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print ("Game over!")
                pygame.quit()
                return
        
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        
        for shot in shot_group:
            shot.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()