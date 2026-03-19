import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        asteroid_one_direction = self.velocity.rotate(split_angle)
        asteroid_two_direction = self.velocity.rotate(-split_angle)
        asteroid_new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position[0], self.position[1], asteroid_new_radius)
        asteroid1.velocity = asteroid_one_direction * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], asteroid_new_radius)
        asteroid2.velocity = asteroid_two_direction * 1.2