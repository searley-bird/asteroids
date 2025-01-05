import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt