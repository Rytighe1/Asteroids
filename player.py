import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player (CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def rotate (self, amount, dt):
        self.rotation += amount * (PLAYER_TURN_SPEED * dt)

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)

    def move(self, amount, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += amount * rotated_with_speed_vector

