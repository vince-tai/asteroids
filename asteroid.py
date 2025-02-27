import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface = screen, 
            color = "white",
            center = self.position, 
            radius = self.radius, 
            width = 2
            )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        rad = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, rad)
        second_asteroid = Asteroid(self.position.x, self.position.y, rad)

        first_asteroid.velocity = first_vector * 1.2
        second_asteroid.velocity = second_vector * 1.2