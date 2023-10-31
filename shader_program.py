from settings import *

class ShaderProgram:
    def __init__(self,app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player #001

        # SHADERS #
        self.chunk = self.get_program(shader_name='quad')
        # self.quad = self.get_program(shader_name='quad')
        # --------#

        self.set_uniforms_on_init()
    
    #001
    def set_uniforms_on_init(self):

        self.chunk['m_proj'].write(self.player.m_proj)
        # self.quad['m_proj'].write(self.player.m_proj)

        self.chunk['m_model'].write(glm.mat4())
        # self.quad['m_model'].write(glm.mat4())

    def update(self):
        self.chunk['m_view'].write(self.player.m_view)
        # self.quad['m_view'].write(self.player.m_view)
    #001 ends 
    
    def get_program(self, shader_name):
        with open(f'shaders/quad.vert') as file:
            vertex_shader = file.read()
        
        with open(f'shaders/quad.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
        return program