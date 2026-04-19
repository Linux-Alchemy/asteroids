"""Central game configuration values."""

# Screen settings
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

# Player settings
PLAYER_RADIUS: int = 20
LINE_WIDTH: int = 2
PLAYER_TURN_SPEED: int = 300
PLAYER_SPEED: int = 200
PLAYER_SHOOT_COOLDOWN_SECONDS: float = 0.3

# Asteroid settings
ASTEROID_MIN_RADIUS: int = 20
ASTEROID_KINDS: int = 3
ASTEROID_SPAWN_RATE_SECONDS: float = 0.8
ASTEROID_MAX_RADIUS: int = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Bullet settings
SHOT_RADIUS: int = 5
PLAYER_SHOOT_SPEED: int = 500
