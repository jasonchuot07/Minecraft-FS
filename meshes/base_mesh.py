import numpy as np


#001 - I don't know what this does yet and how it's going to be usefull
#002 - I know what this is but not exactly how it works
#003 - Error, it doesn't work

class BaseMesh: 
    def __init__(self):
        # OpenGL context
        self.ctx = None

        # Shader Program: 
        self.program = None

        # Vertex buffer data type format: "3f 3f"
        
        self.vbo_format = None

        # Attribute names according to the format: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None

        # Vertex Array Object
        self.vao = None
    #001
    def get_vertex_data(self) -> np.array:...

    def get_vao(self):
        vertext_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertext_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        return vao
    # 001 end
    def render(self):
        self.vao.render()
