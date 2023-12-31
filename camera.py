from settings import *

"""
1. Projection Matrix (m_proj):

Think of this as the "lens" of the camera. It determines how the 3D scene gets projected onto a 2D plane (your computer screen). Changing this matrix can affect the field of view, perspective, etc.

2. Model Matrix (m_model):
This matrix represents the position, rotation, and scale of an object in the 3D world. The identity matrix (glm.mat4()) means no transformation, so the object is initially at its default position.


3. View Matrix (m_view):
This matrix represents the position and orientation of the "camera" or the viewer. Changing this matrix moves the "camera" around the scene.
"""

class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = glm.vec3(position)

        self.yaw = glm.radians(yaw)

        self.pitch = glm.radians(pitch)

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, vel):
        self.position -= self.right * vel

    def move_right(self, vel):
        self.position += self.right * vel

    def move_up(self, vel):
        self.position += self.up * vel

    def move_down(self, vel):
        self.position -= self.up * vel

    def move_forward(self, vel):
        self.position += self.forward * vel

    def move_back(self, vel):
        self.position -= self.forward * vel




        