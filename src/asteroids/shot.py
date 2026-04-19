"""Projectile sprite implementation."""

import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """A projectile fired by the player ship."""

    def __init__(self, x: float, y: float) -> None:
        """Create a shot at the supplied coordinates."""
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        """Render the projectile as a small circle."""
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt: float) -> None:
        """Move the projectile according to its velocity."""
        self.position += self.velocity * dt
