"""Triangle moves along a circular path"""
import math
from turtle import position
import OpenGL.GL as GL
import time
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle moving in a circular path around the origin """
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
        # Render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        position_data =  [[-0.2,-0.3,0],
                          [-0.1,-0.3,0],
                          [-0.2,0.3,0],
                          [-0.1,-0.3,0],
                          [-0.1,0.3,0],
                          [-0.2,0.3,0],
                          [-0.1,0.2,0],
                          [0.1,0.3,0],
                          [-0.1,0.3,0],
                          [-0.1,0.2,0],
                          [0.1,0.2,0],
                          [0.1,0.3,0],
                          [0.1,0.2,0],
                          [0.135137,0.299347,0],
                          [0.1,0.3,0],
                          [0.1,0.2,0],
                          [0.156635,0.288033,0],
                          [0.135137,0.299347,0],
                          [0.1,0.2,0],
                          [0.177001,0.268798,0],
                          [0.135137,0.299347,0],
                          [0.1,0.2,0],
                          [0.189447,0.245038,0],
                          [0.177001,0.268798,0],
                          [0.1,0.2,0],
                          [0.198498,0.221277,0],
                          [0.189447,0.245038,0],
                          [0.1,0.2,0],
                          [0.2,0.2,0],
                          [0.198498,0.221277,0],
                          [0.1,0.2,0],
                          [0.2,0.1,0],
                          [0.2,0.2,0],
                          [0.1,0.1,0],
                          [0.2,0.1,0],
                          [0.1,0.2,0],
                          [0.1,0.1,0],
                          [0.198498,0.0753214,0],
                          [0.2,0.1,0],
                          [0.1,0.1,0],
                          [0.190578,0.053824,0],
                          [0.198498,0.0753214,0],
                          [0.1,0.1,0],
                          [0.175869,0.0379838,0],
                          [0.190578,0.053824,0],
                          [0.1,0.1,0],
                          [0.158898,0.0221437,0],
                          [0.175869,0.0379838,0],
                          [0.1,0.1,0],
                          [0.138532,0.0142236,0],
                          [0.158898,0.0221437,0],
                          [0.1,0.1,0],
                          [0.120429,0.00630346,0],
                          [0.138532,0.0142236,0],
                          [0.1,0.1,0],
                          [0.1,0,0],
                          [0.120429,0.00630346,0],
                          [0,0,0],
                          [0.1,-0.3,0],
                          [0.1,0,0],
                          [-0.1,0,0],
                          [0.1,0,0],
                          [-0.1,0.1,0],
                          [-0.1,0.1,0],
                          [0.1,0,0],
                          [0.1,0.1,0],
                          [0.1,-0.3,0],
                          [0.2,-0.3,0],
                          [0.1,0,0]]
#-0.12
#min: -0.807107


        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.4353, 0.2941, 0.5843])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

       


    def update(self):
        """ Update data """

        self.translation.data[0] = math.sin(time.time())
        self.translation.data[1] = math.cos(time.time())
        
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()