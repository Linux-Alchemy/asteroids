"""Asteroid sprite behaviour."""

import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    """A drifting asteroid that can split into smaller rocks."""

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Initialise an asteroid at the supplied position and size."""
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        """Render the asteroid as a wireframe circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        """Move the asteroid according to its current velocity."""
        self.position += self.velocity * dt

    def split(self) -> tuple["Asteroid", "Asteroid"] | None:
        """Destroy the asteroid and create two smaller ones when possible."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(new_angle)
        new_vector2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2
        return new_asteroid1, new_asteroid2
