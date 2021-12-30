SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60

BLACK = ((0, 0, 0))

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 32
PLAYER_IMAGE = "images\\player.png"
PLAYER_START_X = SCREEN_WIDTH / 2
PLAYER_START_Y = SCREEN_HEIGHT
PLAYER_SPEED = 6

WEAPON_COOLDOWN = 1
WEAPON_IMAGE = "images\\weapon.png"

BULLET_IMAGE = "images\\bullet.png"
BULLET_SPEED = 6

OBSTACLE_START_X = 50
OBSTACLE_START_Y = SCREEN_HEIGHT / 1.25

OBSTACLE_SHAPE = [
    "  ****************  ",
    " ****************** ",
    "********************",
    "********************",
    "********************",
    "********************",
    "*****          *****",
    "****            ****"
]

BLOCK_SIZE = 4

OBSTACLE_WIDTH = len(OBSTACLE_SHAPE[0]) * BLOCK_SIZE
OBSTACLE_HEIGHT = len(OBSTACLE_SHAPE)

WIDTH_OBSTACLE = len(OBSTACLE_SHAPE[0]) * BLOCK_SIZE

# Главное, чтобы image соответствовал
# Размеру блока относительно метода
# fill_obstacle()
BLOCK_IMAGE = "images\\block.png"
BLOCK_COLOUR = (255, 0, 0)

OFFSET_BETWEEN_OBSTACLES = 64

SQUAD_IMAGES = [
    PLAYER_IMAGE,
]

SQUAD_SHAPE = [
    "0000",
    "0000",
    "0000",
    "0000"
]