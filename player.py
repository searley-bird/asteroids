import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *

PLAYER_RADIUS = 20

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return
    
    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            if hasattr(self, 'shot_group'):
                self.shot_group.add(shot)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shoot_timer -= dt
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        velocity = direction * PLAYER_SPEED * dt
        self.position += velocity