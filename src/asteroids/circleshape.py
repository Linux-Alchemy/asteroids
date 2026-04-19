"""Shared base type for circular game sprites."""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects represented by a position and radius."""

    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float

    def __init__(self, x: float, y: float, radius: float) -> None:
        """Initialise the sprite and register it with configured groups."""
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the sprite to the provided surface."""
        raise NotImplementedError

    def update(self, dt: float) -> None:
        """Advance the sprite state by the elapsed frame time."""
        raise NotImplementedError

    def collides_with(self, other: "CircleShape") -> bool:
        """Return ``True`` when two circular sprites overlap."""
        return self.position.distance_to(other.position) <= self.radius + other.radius
