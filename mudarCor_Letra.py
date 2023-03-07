"""Passar dados entre shaders"""
import math
from turtle import position
import OpenGL.GL as GL
import time
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform

class Example(Base):
    """ Render shapes with vertex colors """
    def initialize(self):
        print("Initializing program...")

        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)

        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attributes #
        position_data = [[0.2,0.3,0],
                         [-0.1,0.3,0],
                         [0.2,0.2,0],
                         [-0.1,0.2,0],
                         [0.2,0.2,0],
                         [-0.1,0.3,0],
                         [-0.1,0.2,0],
                         [-0.1,0.3,0],
                         [-0.14,0.28,0],
                         [-0.1,0.2,0],
                         [-0.14,0.28,0],
                         [-0.18,0.24,0],
                         [-0.2,0.2,0],
                         [-0.1,0.2,0],
                         [-0.18,0.24,0],
                         [-0.1,0.05,0],
                         [-0.1,0.2,0],
                         [-0.2,0.2,0],
                         [-0.1,0.05,0],
                         [-0.2,0.2,0],
                         [-0.2,0.05,0],
                         [-0.1,0.05,0],
                         [-0.2,0.05,0],
                         [-0.18,0,0],
                         [-0.1,0.05,0],
                         [-0.18,0,0],
                         [-0.14,-0.04,0],
                         [-0.1,0.05,0],
                         [-0.14,-0.04,0],
                         [-0.1,-0.05,0],
                         [0.1,0.05,0],
                         [-0.1,0.05,0],
                         [-0.1,-0.05,0],
                         [0.1,0.05,0],
                         [-0.1,-0.05,0],
                         [0.1,-0.05,0],
                         [0.1,-0.05,0],
                         [0.15819,0.028,0],
                         [0.1,0.05,0],
                         [0.1,-0.05,0],
                         [0.18,0,0],
                         [0.15819,0.028,0],
                         [0.1,-0.05,0],
                         [0.2,-0.05,0],
                         [0.18,0,0],
                         [0.1,-0.05,0],
                         [0.2,-0.2,0],
                         [0.2,-0.05,0],
                         [0.1,-0.2,0],
                         [0.2,-0.2,0],
                         [0.1,-0.05,0],
                         [0.1,-0.2,0],
                         [0.18,-0.24,0],
                         [0.2,-0.2,0],
                         [0.1,-0.2,0],
                         [0.14,-0.28,0],
                         [0.18,-0.24,0],
                         [0.1,-0.2,0],
                         [0.1,-0.3,0],
                         [0.14,-0.28,0],
                         [0.1,-0.3,0],
                         [0.1,-0.2,0],
                         [-0.2,-0.2,0],
                         [0.1,-0.3,0],
                         [-0.2,-0.2,0],
                         [-0.2,-0.3,0]]
  
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 1.0, 1.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.increment = 0.005;
       
        
    def update(self):
        self.base_color.data[0] += self.increment  
        self.base_color.data[1] += self.increment  
        self.base_color.data[2] += self.increment 
        if(self.base_color.data[0] >= 1 or 0 >= self.base_color.data[0]):
            self.increment = 0 - self.increment 
        
        
        
        GL.glClearColor(0.4353, 0.2941, 0.5843, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)
        


# Instantiate this class and run the program
Example().run()