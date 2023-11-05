from settings import *
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram
from scene import Scene
from player import Player

#001 - I don't know what this does yet and how it's going to be usefull
#002 - I know what this is but not exactly how it works
#003 - Error, it doesn't work

class VoxelEngine:
    def __init__(self):
        # Start pygame
        pg.init()

        # These are the attributes that need to be set first - Necessary setup
        #001 - Set OpenGL context attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        # Setup window's resolution | from flags - 001
        #002 - Create a window with OpenGL context
        pg.display.set_mode((500, 500), flags=pg.OPENGL | pg.DOUBLEBUF)
        # Setup OpenGL context
        self.ctx = mgl.create_context()

        #001 - Enabling depth testing and color blending
        #003 - Enable depth testing and face culling in the OpenGL context
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        #002 - Enabling garbage collecting mode, so unused gl objects are not automatically deleted
        #001 - Set the garbage collection mode for OpenGL context
        self.ctx.gc_mode = 'auto'

        # Setting up time so we can keep track
        # Initialize Pygame clock for timing
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        # Hide mouse cursor and grab input
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        # Check if your app is running
        self.is_running = True

        # On self Init
        self.on_init()

    def on_init(self):
        # Create player, shader program, and scene
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)
        
    def update(self):
        # Update player, shader program, and scene
        self.player.update()

        # Updating Shader
        self.shader_program.update()

        self.scene.update()
        
        # Updating the time itself 
        self.delta_time = self.clock.tick()

        self.time = pg.time.get_ticks() * 0.0001

        # Display frames per second in the window title
        pg.display.set_caption(f' Frames per second: {self.clock.get_fps(): .0f} | Voxel Engine 1.0')
        #-------#

    def render(self):
        # Clear the OpenGL context with a specified color
        self.ctx.clear(color=(BG_COLOR))

        # Render the scene
        self.scene.render()

        # Display the new frame
        pg.display.flip()


    def handle_events(self):
        # Check for events, such as quitting the game
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        # Main game loop
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()

        # Quit Pygame and exit the program
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    # Create an instance of the VoxelEngine and run the game
    app = VoxelEngine()
    app.run()