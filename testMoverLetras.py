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
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

        # Set up vertex array object - parte curva do J #
        self.vao_J = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_J)
        position_data_parte_curvaJ = [[-0.39775,0.65297,0], #A
        [-0.34415,0.62489,0],#B
        [-0.4,0.6,0],#C

        [-0.34415,0.62489,0],#B
        [-0.4183,0.54728,0],#D
        [-0.4,0.6,0],#C    

        [-0.39775,0.65297,0],#A  
        [-0.4,0.6,0],#C 
        [-0.44,0.56, 0],#E 

        [-0.4,0.6,0], #C
        [-0.4183,0.54728,0], #D
        [-0.44,0.56, 0], #E     

        [-0.44,0.56, 0], #E
        [-0.4183,0.54728,0], #D
        [-0.46787,0.47515, 0], #F 
#
        [-0.44,0.56, 0], #E
        [-0.46787,0.47515, 0], #F
        [-0.48856,0.48488,0], #G  
#
        [-0.46787,0.47515, 0], #F
        [-0.52554,0.39706,0], #I
        [-0.54587,0.41,0], #H  
#
        [-0.48856,0.48488,0], #G
        [-0.46787,0.47515, 0], #F
        [-0.54587,0.41,0], #H  
#
        [-0.52554,0.39706,0], #I
        [-0.58636,0.32443,0], #K
        [-0.60682,0.34169,0], #J  
#
        [-0.54587,0.41,0], #H
        [-0.52554,0.39706,0], #I
        [-0.60682,0.34169,0], #J 
#
        [-0.60682,0.34169,0], #J
        [-0.58636,0.32443,0], #K
        [-0.64523,0.26378,0], #L 
#
        [-0.60682,0.34169,0], #J
        [-0.64523,0.26378,0], #L
        [-0.69854,0.24213,0], #M 
#
        [-0.69854,0.24213,0], #M
        [-0.64523,0.26378,0], #L
        [-0.71301,0.18529,0], #N 
#
        [-0.69854,0.24213,0], #M
        [-0.71301,0.18529,0], #N
        [-0.76475,0.1728,0], #O 
#
        [-0.76475,0.1728,0], #O
        [-0.71301,0.18529,0], #N
        [-0.74869,0.14248,0], #P
#
        [-0.78733,0.21521,0], #Q
        [-0.74869,0.14248,0], #P
        [-0.76549,0.13739,0], #S

        [-0.78733,0.21521,0], #Q
        [-0.76549,0.13739,0], #S
        [-0.80237,0.21401,0], #R

        [-0.80518,0.28853,0], #U
        [-0.78733,0.21521,0], #Q
        [-0.8174,0.28649,0], #T

        [-0.8174,0.28649,0], #T
        [-0.78733,0.21521,0], #Q
        [-0.80237,0.21401,0], #R

        [-0.81994,0.36791,0], #W
        [-0.80518,0.28853,0], #U
        [-0.83266,0.36536,0], #V

        [-0.83266,0.36536,0], #V
        [-0.80518,0.28853,0], #U
        [-0.8174,0.28649,0], #T

        [-0.76475,0.1728,0], #O
        [-0.71301,0.18529,0], #N
        [-0.74869,0.14248,0], #P

        [-0.82503,0.44373,0], #Z
        [-0.81994,0.36791,0], #W
        [-0.83266,0.36536,0], #V

        [-0.84233,0.44118,0], #A1
        [-0.82503,0.44373,0], #Z
        [-0.83266,0.36536,0], #V

        [-0.82214,0.50388,0], #C1
        [-0.82503,0.44373,0], #Z
        [-0.84172,0.50388,0], #B1

        [-0.84172,0.50388,0], #B1
        [-0.82503,0.44373,0], #Z
        [-0.84233,0.44118,0], #A1

        [-0.8104,0.57323,0], #E1
        [-0.82214,0.50388,0], #C1
        [-0.83556,0.57435,0], #D1

        [-0.83556,0.57435,0], #D1
        [-0.82214,0.50388,0], #C1
        [-0.84172,0.50388,0], #B1

        [-0.82158,0.64594,0], #F1
        [-0.7953,0.64202,0], #G1
        [-0.8104,0.57323,0], #E1

        [-0.82158,0.64594,0], #F1
        [-0.8104,0.57323,0], #E1
        [-0.83556,0.57435,0], #D1

        [-0.77852,0.69627,0], #I1
        [-0.7953,0.64202,0], #G1
        [-0.82158,0.64594,0], #F1

        [-0.80799,0.68996,0], #H1
        [-0.77852,0.69627,0], #I1
        [-0.82158,0.64594,0], #F1

        [-0.80799,0.68996,0], #H1
        [-0.76845,0.71417,0], #K1
        [-0.77852,0.69627,0], #I1

        [-0.80799,0.68996,0], #H1
        [-0.76845,0.71417,0], #K1
        [-0.79919,0.71151,0], #L1

        [-0.79919,0.71151,0], #L1
        [-0.76573,0.72069,0], #M1
        [-0.76845,0.71417,0], #K1

        [-0.79919,0.71151,0], #L1
        [-0.79215,0.72713,0], #N1
        [-0.76573,0.72069,0], #M1

        [-0.79215,0.72713,0], #N1
        [-0.78263,0.74035,0], #O1
        [-0.76573,0.72069,0], #M1

        [-0.76573,0.72069,0], #M1
        [-0.78263,0.74035,0], #O1
        [-0.75919,0.73303,0], #P1

        [-0.78263,0.74035,0], #O1
        [-0.77106,0.74838,0], #Q1
        [-0.75919,0.73303,0], #P1

        [-0.77106,0.74838,0], #Q1
        [-0.75,0.735,0], #S1
        [-0.75919,0.73303,0], #P1

        [-0.77106,0.74838,0], #Q1
        [-0.75567,0.7518,0], #R1
        [-0.75,0.735,0], #S1

        [-0.75567,0.7518,0], #R1
        [-0.73988,0.74759,0], #T1
        [-0.75,0.735,0], #S1

        [-0.73988,0.74759,0], #T1
        [-0.72594,0.73812,0], #U1
        [-0.75,0.735,0], #S1

        [-0.72594,0.73812,0], #U1
        [-0.72519,0.71117,0], #W1
        [-0.75,0.735,0], #S1

        [-0.72594,0.73812,0], #U1
        [-0.70792,0.72325,0], #V1
        [-0.72519,0.71117,0]] #W1  

        self.vertex_count_parte_curvaJ = len(position_data_parte_curvaJ)
        position_attribute_parte_curvaJ = Attribute('vec3', position_data_parte_curvaJ)
        position_attribute_parte_curvaJ.associate_variable(self.program_ref, 'position')

        # Set up vertex array object - quadrado de baixo #
        self.vao_B = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_B)
        position_data_B =[[-0.70792,0.72325,0], #V1
        [-0.69587,0.71134,0], #A2
        [-0.72519,0.71117,0], #W1

        [-0.72519,0.71117,0], #W1
        [-0.69587,0.71134,0], #A2
        [-0.69761,0.68849,0], #B2

        [-0.69587,0.71134,0], #A2
        [-0.67772,0.66859,0], #C2
        [-0.69761,0.68849,0], #B2

        [-0.69587,0.71134,0], #A2
        [-0.6719,0.69028,0], #D2
        [-0.67772,0.66859,0], #C2

        [-0.6719,0.69028,0], #D2
        [-0.62384,0.64864,0], #E2
        [-0.67772,0.66859,0], #C2

        [-0.67772,0.66859,0], #C2
        [-0.62384,0.64864,0], #E2
        [-0.64142,0.62915,0], #Z1

        [-0.62384,0.64864,0], #E2
        [-0.47,0.51,0], #F2
        [-0.64142,0.62915,0], #Z1

        [-0.64142,0.62915,0], #Z1
        [-0.47,0.51,0], #F2
        [-0.49,0.49,0], #G2

        [-0.45,0.5,0], #H2
        [-0.41077,0.439,0], #I2
        [-0.46787,0.47515, 0], #F

        [-0.46787,0.47515, 0], #F
        [-0.41077,0.439,0], #I2
        [-0.42578,0.42238,0], #J2

        [-0.41077,0.439,0], #I2
        [-0.3726,0.38333,0], #L2
        [-0.39102,0.37298,0], #K2

        [-0.41077,0.439,0], #I2
        [-0.39102,0.37298,0], #K2
        [-0.42578,0.42238,0], #J2

        [-0.3726,0.38333,0], #L2
        [-0.34334,0.33312,0], #M2
        [-0.39102,0.37298,0], #K2

        [-0.39102,0.37298,0], #K2
        [-0.34334,0.33312,0], #M2
        [-0.36029,0.3269,0], #N2

        [-0.34334,0.33312,0], #M2
        [-0.31723,0.28004,0], #P2
        [-0.33375,0.2753,0], #O2

        [-0.34334,0.33312,0], #M2
        [-0.33375,0.2753,0], #O2
        [-0.36029,0.3269,0], #N2

        [-0.31723,0.28004,0], #P2
        [-0.27704,0.17674,0], #Q2
        [-0.33375,0.2753,0], #O2

        [-0.33375,0.2753,0], #O2
        [-0.27704,0.17674,0], #Q2
        [-0.28506,0.17535,0], #R2

        [-0.27704,0.17674,0], #QS
        [-0.27524,0.17268,0], #S2
        [-0.28506,0.17535,0], #R2

        [-0.28506,0.17535,0], #R2
        [-0.27524,0.17268,0], #S2
        [-0.28,0.17,0], #T2

        [-0.28,0.17,0], #T2
        [-0.27524,0.17268,0], #S2
        [-0.27502,0.16748,0], #U2

        [-0.27502,0.16748,0], #U2
        [-0.27524,0.17268,0], #S2
        [-0.27177,0.1665,0], #V2

        [-0.27177,0.1665,0], #V2
        [-0.27524,0.17268,0], #S2
        [-0.26792,0.16687,0], #W2

        [-0.26792,0.16687,0], #W2
        [-0.27524,0.17268,0], #S2
        [-0.26504,0.16894,0], #Z2

        [-0.41077,0.439,0], #I2
        [-0.39102,0.37298,0], #K2
        [-0.42578,0.42238,0], #J2

        [-0.27524,0.17268,0], #S2
        [-0.26811,0.17493,0], #A3
        [-0.26504,0.16894,0], #Z2

        [-0.26811,0.17493,0], #A3
        [-0.25686,0.17476,0], #B3
        [-0.26504,0.16894,0], #Z2

        [-0.26811,0.17493,0], #A3
        [-0.26,0.18,0], #D3
        [-0.25686,0.17476,0], #B3

        [-0.26,0.18,0], #D3
        [-0.24664,0.18068,0], #C3
        [-0.25686,0.17476,0], #B3

        [-0.26,0.18,0], #D3
        [-0.2493,0.18618,0], #E3
        [-0.24664,0.18068,0]] #C3

        
        self.vertex_count_B = len( position_data_B)
        position_attribute_B = Attribute('vec3',  position_data_B)
        position_attribute_B.associate_variable(self.program_ref, 'position')



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

      #  GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)
        GL.glBindVertexArray(self.vao_J)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count_parte_curvaJ)
        GL.glBindVertexArray(self.vao_B)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count_B)


# instantiate this class and run the program
Test().run()