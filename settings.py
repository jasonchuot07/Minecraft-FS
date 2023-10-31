from numba import njit
import numpy as np
import glm
import math

# Resolution
WIN_RES = glm.vec2(500, 500)

# Chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# CAMERA
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # Vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO) # Horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# Player
PLAYER_SPD = 0.005
PLAYER_ROTATION_SPD = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENS = 0.002

# BG Color
BG_COLOR = glm.vec3(0.1, 0.16, 0.2)