"""Changing color with time"""
import math
from tokenize import Double
from unittest import mock
import OpenGL.GL as GL


from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle changing its color """
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
        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex array object - parte curva do J #
        self.vao_J = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_J)
         ###################ALPHA###################
        position_data_parte_curvaJ = [[-0.17783,0.84389,0], #A
        [-0.11598,0.80004,0],#B
        [-0.2,0.6,0],#C

        [-0.17783,0.84389,0],#A
        [-0.2,0.6,0],#C
        [-0.25854,0.64126, 0],#D    

        [-0.2,0.6,0],#C  
        [-0.2978,0.40793, 0],#E 
        [-0.25854,0.64126, 0],#D 

        [-0.25854,0.64126, 0], #D
        [-0.2978,0.40793, 0], #E
        [-0.36873,0.40182, 0], #F     

        [-0.36873,0.40182, 0], #F
        [-0.4548,0.09345, 0], #G
        [-0.53532,0.08769, 0], #H 

        [-0.2978,0.40793, 0], #E
        [-0.4548,0.09345, 0], #G
        [-0.36873,0.40182, 0], #F  

        [-0.8,0.2,0], #A
        [-0.42572,-0.11972,0], #H
        [-0.78044,0.05909,0], #C   

        [-0.42572,-0.11972,0], #H
        [-0.4548,0.09345, 0], #G
        [-0.56149,0.01154,0], #I  

        [-0.42572,-0.11972,0], #H
        [-0.56149,0.01154,0], #I
        [-0.63289,0.04485,0], #J  

        [-0.42572,-0.11972,0], #H
        [-0.63289,0.04485,0], #J
        [-0.67334,0.15908,0], #K 

        [-0.42572,-0.11972,0], #H
        [-0.67334,0.15908,0], #K
        [-0.65669,0.38041,0], #L  

        [-0.65669,0.38041,0], #L
        [-0.67334,0.15908,0], #K
        [-0.79977,0.63037,0], #M 

        [-0.65669,0.38041,0], #L
        [-0.79977,0.63037,0], #M
        [-0.74236,0.75403,0], #N 

        [-0.74236,0.75403,0], #N
        [-0.79977,0.63037,0], #M
        [-0.76109,0.87978,0], #P 

        [-0.76109,0.87978,0], #P
        [-0.79977,0.63037,0], #M
        [-0.80826,0.93616,0], #O

        [-0.80826,0.93616,0], #O
        [-0.73348,0.97067,0], #Q
        [-0.76109,0.87978,0], #P

        [-0.73348,0.97067,0], #Q
        [-0.62303,0.92005,0], #R
        [-0.76109,0.87978,0], #P 

        [-0.76109,0.87978,0], #p
        [-0.62303,0.92005,0], #R
        [-0.68858,0.85608,0], #S 

        [-0.62303,0.92005,0], #R
        [-0.50276,0.71982,0], #T
        [-0.68858,0.85608,0], #S 

        [-0.62303,0.92005,0], #r
        [-0.39706,0.71395,0], #U
        [-0.50276,0.71982,0], #T

        [-0.50276,0.71982,0], #t
        [-0.39706,0.71395,0], #U
        [-0.39559,0.61485,0], #A1 

        [-0.39706,0.71395,0], #U
        [-0.28,0.59,0], #B1
        [-0.39559,0.61485,0], #A1


        [-0.39559,0.61485,0], #a1
        [-0.28,0.59,0], #B1
        [-0.31,0.54,0], #c1

        [-0.24,0.52,0], #z
        [-0.17214,0.25867,0], #w
        [-0.28,0.44,0], #v

        [-0.24,0.52,0], #z
        [-0.07737,0.20396,0], #d1
        [-0.17214,0.25867,0], #w

        [-0.07737,0.20396,0], #d1
        [-0.04645,0.05992,0], #e1
        [-0.17214,0.25867,0], #w

        [-0.07737,0.20396,0], #d1
        [-0.02197,0.11603,0], #g1
        [-0.04645,0.05992,0], #e1

        [-0.02197,0.11603,0], #g1
        [0.01956,0.11981,0], #h1
        [-0.04645,0.05992,0], #e1

        [-0.02197,0.11603,0], #g1
        [0.01484,0.1585,0], #i1
        [0.01956,0.11981,0], #h1


        #######################SIGMA#######################

        [0.56956,0.50942,0], #A
        [0.50901,0.417,0], #C
        [0.47395,0.47755,0], #B

        [0.47395,0.47755,0], #B
        [0.50901,0.417,0], #G
        [0.47395,0.47755,0], #F

        [0.47395,0.47755,0], #B
        [0.50901,0.417,0], #C
        [0.50901,0.417,0], #G

        [0.47395,0.47755,0], #F
        [0.50901,0.417,0], #G
        [0.25087,0.30228,0], #H

        [0.25087,0.30228,0], #H
        [0.50901,0.417,0], #G
        [0.29549,0.09513,0], #I

        [0.25087,0.30228,0], #H
        [0.29549,0.09513,0], #I
        [0.23812,-0.11839,0], #J

        [0.29549,0.09513,0], #I
        [0.3178,-0.13751,0], #K
        [0.23812,-0.11839,0], #J

        [0.23812,-0.11839,0], #J
        [0.3178,-0.13751,0], #K
        [0.26999,-0.27136,0], #L

        [0.3178,-0.13751,0], #K
        [0.45802,-0.34147,0], #N
        [0.33692,-0.35103,0], #M

        [0.45802,-0.34147,0], #N
        [0.58231,-0.43708,0], #O
        [0.33692,-0.35103,0], #M

        [0.45802,-0.34147,0], #N
        [0.63967,-0.34784,0], #D
        [0.58231,-0.43708,0], #O

        [0.63967,-0.34784,0], #D
        [0.79264,-0.36697,0], #E
        [0.58231,-0.43708,0], #O

        [0.63967,-0.34784,0], #D
        [0.88506,-0.22993,0], #P
        [0.79264,-0.36697,0], #E

        [0.63967,-0.34784,0], #D
        [0.94,0,0], #Q
        [0.88506,-0.22993,0], #P

        [0.84,-0.12,0], #S
        [0.93923,0.23854,0], #R
        [0.94,0,0], #Q

        [0.9,0.08,0], #U
        [0.84682,0.43613,0], #T
        [0.93923,0.23854,0], #R

        [0.86,0.33,0], #V
        [0.56956,0.50942,0], #A
        [0.84682,0.43613,0], #T

        [0.56956,0.50942,0], #A
        [0.86,0.33,0], #V
        [0.50901,0.417,0], #C

        [0.3178,-0.13751,0], #K
        [0.33692,-0.35103,0], #M
        [0.26999,-0.27136,0], #L

        [0.56956,0.50942,0], #A
        [0.95517,0.55404,0], #W
        [0.96473,0.50624,0], #Z

        [0.97864,0.5016,0], #Z
        [0.69,0.48,0], #A1
        [0.56956,0.50942,0], #A
        ] #W1  

        self.vertex_count_parte_curvaJ = len(position_data_parte_curvaJ)
        position_attribute_parte_curvaJ = Attribute('vec3', position_data_parte_curvaJ)
        position_attribute_parte_curvaJ.associate_variable(self.program_ref, 'position')



        # Set up uniform for translation of parte_curvaJ
        self.translation_parte_curvaJ = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_parte_curvaJ.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

        self.move_x = 0
        self.move_y = 0

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
            self.translation_parte_curvaJ.data[0] += dx * 0.0080
            self.translation_parte_curvaJ.data[1] -= dy * 0.0080
            self.prev_mouse_pos = curr_mouse_pos
            print("curr_mouse_posssssssssssssss: ", curr_mouse_pos)
            for i in range(len(position_data)):
                position_data[i][0] += dx * 0.0080
                position_data[i][1] -= dy * 0.0080





        """ Update data """
        if self.input.isKeyPressed('right'):
            self.move_x += 0.05
        if self.input.isKeyPressed('left'):
            self.move_x -= 0.05
        if self.input.isKeyPressed('up'):
            self.move_y += 0.05
        if self.input.isKeyPressed('down'):
            self.move_y -= 0.05

        if self.move_x > 1 + 0.1:
            self.move_x = 1 + 0.1
        if self.move_x < -1 + 0.8:
            self.move_x = -1 + 0.8
        if self.move_y > 1 + 0.1:
            self.move_y = 1 + 0.1
        if self.move_y < -1 + 0.5:
            self.move_y = -1 + 0.5

        # Modify position_data_parte_curvaJ array based on move_x and move_y values
        position_data_parte_curvaJ = [[-0.8 + self.move_x,0.2 + self.move_y,0], #A
        ###################ALPHA###################
        [-0.91141 + self.move_x ,0.06636 + self.move_y,0],#B
        [-0.78044 + self.move_x ,0.05909 + self.move_y,0],#C
        [-0.91141 + self.move_x,0.06636 + self.move_y,0],#B
        [-0.78044 + self.move_x,0.05909 + self.move_y,0],#C
        [-0.94504 + self.move_x,-0.16431 + self.move_y, 0],#D    

        [-0.78044 + self.move_x,0.05909 + self.move_y,0],#C  
        [-0.67856 + self.move_x,-0.73163 + self.move_y, 0],#E 
        [-0.94504 + self.move_x,-0.16431 + self.move_y, 0],#D 

        [-0.49796 + self.move_x,-0.22221 + self.move_y,0], #L
        [-0.4 + self.move_x,-0.2 + self.move_y,0], #F
        [-0.7 + self.move_x,-0.57 + self.move_y, 0], #G     

        [-0.4 + self.move_x,-0.2 + self.move_y,0], #F
        [-0.67856 + self.move_x,-0.73163 + self.move_y, 0], #E
        [-0.7 + self.move_x,-0.57 + self.move_y, 0], #G 

        [-0.49796 + self.move_x,-0.22221 + self.move_y,0], #L
        [-0.15708 + self.move_x,0.241 + self.move_y,0], #N
        [-0.4 + self.move_x,-0.2 + self.move_y,0], #F  

        [-0.8 + self.move_x,0.2 + self.move_y,0], #A
        [-0.42572 + self.move_x,-0.11972 + self.move_y,0], #H
        [-0.78044 + self.move_x,0.05909 + self.move_y,0], #C   

        [-0.78044 + self.move_x,0.05909 + self.move_y,0], #C
        [-0.42572 + self.move_x,-0.11972 + self.move_y,0], #H
        [-0.49796 + self.move_x,-0.22221 + self.move_y,0], #L  

        [-0.4 + self.move_x,-0.2 + self.move_y,0], #F
        [-0.33734 + self.move_x,-0.4155 + self.move_y,0], #I
        [-0.45 + self.move_x,-0.29 + self.move_y,0], #G  

        [-0.4 + self.move_x,-0.2 + self.move_y,0], #F
        [-0.07425 + self.move_x,-0.60495 + self.move_y,0], #A1
        [-0.33734 + self.move_x,-0.4155 + self.move_y,0], #I  

        [-0.3373 + self.move_x,-0.4155 + self.move_y,0], #I
        [-0.07425 + self.move_x,-0.60495 + self.move_y,0], #a1
        [-0.07328 + self.move_x,-0.71223 + self.move_y,0], #J  

        [-0.07425 + self.move_x,-0.60495 + self.move_y,0], #A1
        [0.07917 + self.move_x,-0.57339 + self.move_y,0], #K
        [-0.07328 + self.move_x,-0.71223 + self.move_y,0], #J 

        [-0.94504 + self.move_x,-0.16431 + self.move_y,0], #D
        [-0.67856 + self.move_x,-0.73163 + self.move_y,0], #e
        [-0.91 + self.move_x,-0.39 + self.move_y,0], #h1 

        [-0.91095 + self.move_x,-0.3925 + self.move_y,0], #h1
        [-0.67856 + self.move_x,-0.73163 + self.move_y,0], #E
        [-0.8 + self.move_x,-0.6 + self.move_y,0], #k1 

        [-0.86 + self.move_x,-0.35 + self.move_y,0], #j1
        [-0.67856 + self.move_x,-0.73163 + self.move_y,0], #E
        [-0.8 + self.move_x,-0.6 + self.move_y,0], #k1 

        #######################SIGMA#######################

        [0.56956,0.50942,0], #A
        [0.50901,0.417,0], #C
        [0.47395,0.47755,0], #B

        [0.47395,0.47755,0], #B
        [0.50901,0.417,0], #G
        [0.47395,0.47755,0], #F

        [0.47395,0.47755,0], #B
        [0.50901,0.417,0], #C
        [0.50901,0.417,0], #G

        [0.47395,0.47755,0], #F
        [0.50901,0.417,0], #G
        [0.25087,0.30228,0], #H

        [0.25087,0.30228,0], #H
        [0.50901,0.417,0], #G
        [0.29549,0.09513,0], #I

        [0.25087,0.30228,0], #H
        [0.29549,0.09513,0], #I
        [0.23812,-0.11839,0], #J

        [0.29549,0.09513,0], #I
        [0.3178,-0.13751,0], #K
        [0.23812,-0.11839,0], #J

        [0.23812,-0.11839,0], #J
        [0.3178,-0.13751,0], #K
        [0.26999,-0.27136,0], #L

        [0.3178,-0.13751,0], #K
        [0.45802,-0.34147,0], #N
        [0.33692,-0.35103,0], #M

        [0.45802,-0.34147,0], #N
        [0.58231,-0.43708,0], #O
        [0.33692,-0.35103,0], #M

        [0.45802,-0.34147,0], #N
        [0.63967,-0.34784,0], #D
        [0.58231,-0.43708,0], #O

        [0.63967,-0.34784,0], #D
        [0.79264,-0.36697,0], #E
        [0.58231,-0.43708,0], #O

        [0.63967,-0.34784,0], #D
        [0.88506,-0.22993,0], #P
        [0.79264,-0.36697,0], #E

        [0.63967,-0.34784,0], #D
        [0.94,0,0], #Q
        [0.88506,-0.22993,0], #P

        [0.84,-0.12,0], #S
        [0.93923,0.23854,0], #R
        [0.94,0,0], #Q

        [0.9,0.08,0], #U
        [0.84682,0.43613,0], #T
        [0.93923,0.23854,0], #R

        [0.86,0.33,0], #V
        [0.56956,0.50942,0], #A
        [0.84682,0.43613,0], #T

        [0.56956,0.50942,0], #A
        [0.86,0.33,0], #V
        [0.50901,0.417,0], #C

        [0.3178,-0.13751,0], #K
        [0.33692,-0.35103,0], #M
        [0.26999,-0.27136,0], #L

        [0.56956,0.50942,0], #A
        [0.95517,0.55404,0], #W
        [0.96473,0.50624,0], #Z

        [0.97864,0.5016,0], #Z
        [0.69,0.48,0], #A1
        [0.56956,0.50942,0], #A
                         ],
                         #W1

        # Update the Attribute object with new data
        position_attribute_parte_curvaJ = Attribute('vec3', position_data_parte_curvaJ)
        position_attribute_parte_curvaJ.associate_variable(self.program_ref, 'position')

        # Draw the triangle with updated position data
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)



        self.translation_parte_curvaJ.upload_data()
        self.base_color.upload_data()
        GL.glBindVertexArray(self.vao_J)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count_parte_curvaJ)





# Instantiate this class and run the program
Example().run()