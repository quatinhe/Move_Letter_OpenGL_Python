"""Demonstrating functionality"""
import math
from turtle import position
import OpenGL.GL as GL
import time
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform
import numpy as np

class Test(Base):
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

        self.base_color = Uniform('vec3', [0.4353, 0.2941, 0.5843])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.dx = 0.01
        self.dy = 0.01
        #mouse state variables
        self.mouse_down = False
        self.prev_mouse_pos = None




     def is_point_in_triangle(self, y, z, triangle):
        #Returns True if the point is inside the triangle, False otherwise
        # Unpack the points
        p1, p2, p3 = triangle
  
        print(p2, p3)
 

        print("x: ", y)
        print("y: ", z)
        # Calculate the areas of the three triangles formed by the point and the sides of the triangle
        A1 = 0.5 * abs(p2[0]*p3[1] + p3[0]*z + y*p2[1] - p3[0]*p2[1] - y*p3[1] - p2[0]*z)
        A2 = 0.5 * abs(p1[0]*p3[1] + p3[0]*z + y*p1[1] - p3[0]*p1[1] - y*p3[1] - p1[0]*z)
        A3 = 0.5 * abs(p1[0]*p2[1] + p2[0]*z + y*p1[1] - p2[0]*p1[1] - y*p2[1] - p1[0]*z)
    
        # Calculate the area of the triangle
        total_area = A1 + A2 + A3
    
        # If the sum of the areas of the three triangles is equal to the area of the triangle,
        # then the point is inside the triangle
        return abs(total_area - 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p2[0]*p1[1] - p3[0]*p2[1] - p1[0]*p3[1])) < 1e-6

     def normalize_mouse_pos(self, mouse_pos, window_size):
        x, y = mouse_pos
        w, h = window_size
        x_norm = (2.0 * x / w) - 1.0
        y_norm = 1.0 - (2.0 * y / h)
        return (x_norm, y_norm)

        #Verificar se o mouse está dentro do objeto
     def is_mouse_inside_object(self, mouse_pos, position_data, vertex_count):
     # Create list of all x,y pairs in position_data
        points = [(position_data[i], position_data[i+1], position_data[i+2]) for i in range(0, vertex_count, 3)]
        normalized_pos = self.normalize_mouse_pos(mouse_pos, (512, 512))
        print ("mouse_pos_norm: ", normalized_pos)
        # Check if mouse_pos is inside any of the triangles
        for p1, p2, p3 in points:
            triangle = p1, p2, p3
            if self.is_point_in_triangle(normalized_pos[0],normalized_pos[1], triangle):
                return True
        return False


       
     def update(self):
        """debug printing"""
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

        # Handle mouse events

        if self.input.isMousePressed(0) and not self.mouse_down:
            mouse_pos = self.input.mouse_pos

            if self.is_mouse_inside_object(mouse_pos, position_data, len(position_data)):
                print("esta dentro do objeto")
                self.mouse_down = True
                self.prev_mouse_pos = mouse_pos
        elif not self.input.isMousePressed(0) and self.mouse_down:
            self.mouse_down = False
            self.prev_mouse_pos = None
        elif self.mouse_down:
            # Calculate object translation based on mouse movement
            curr_mouse_pos = self.input.mouse_pos
            dx = curr_mouse_pos[0] - self.prev_mouse_pos[0]
            dy = curr_mouse_pos[1] - self.prev_mouse_pos[1]
            self.translation.data[0] += dx * 0.0080
            self.translation.data[1] -= dy * 0.0080
            self.prev_mouse_pos = curr_mouse_pos
            print("curr_mouse_posssssssssssssss: ", curr_mouse_pos)
            for i in range(len(position_data)):
                position_data[i][0] += dx * 0.0080
                position_data[i][1] -= dy * 0.0080
    
        GL.glClearColor(0, 0, 0, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)

# instantiate this class and run the program
Test().run()