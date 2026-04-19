"""Player ship implementation and controls."""

import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    """Player-controlled ship that can rotate, thrust, and fire."""

    rotation: float
    shot_cooldown: float

    def __init__(self, x: float, y: float) -> None:
        """Initialise the player ship at the supplied coordinates."""
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_cooldown = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        """Return the triangle vertices used to draw the ship."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        """Render the player ship."""
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> float:
        """Rotate the ship by an amount derived from the frame delta."""
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def move(self, dt: float) -> None:
        """Move the ship along its facing direction."""
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt: float) -> None:
        """Process player input for movement and shooting."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown -= dt

    def shoot(self) -> None:
        """Fire a projectile if the cooldown has expired."""
        if self.shot_cooldown > 0:
            return

        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
