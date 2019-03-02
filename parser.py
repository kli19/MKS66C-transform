from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.read().split("\n")
    i = 0
    while i < len(lines):
        command = lines[i]
        #print(command)
        if command == "line":
            c = [int(x) for x in lines[i+1].split(" ")]
            add_edge(points, c[0], c[1], c[2], c[3], c[4], c[5])
            i += 2
            #print(c)
        elif command == "ident":
            ident(transform)
            i += 1
            #print_matrix(transform)
        elif command == "scale":
            c = [int(c) for c in lines[i+1].split(" ")]
            s = make_scale(c[0], c[1], c[2])
            matrix_mult(s, transform)
            i += 2
            #print(c)
        elif command == "move":
            c = [int(c) for c in lines[i+1].split(" ")]
            t = make_translate(c[0], c[1], c[2])
            matrix_mult(t, transform)
            i += 2
            #print(c)
        elif command == "rotate":
            c = lines[i+1].split()
            axis = c[0]
            theta = int(c[1])
            if axis == "x":
                r = make_rotX(theta)
            elif axis == "y":
                r = make_rotY(theta)
            else:
                r = make_rotZ(theta)
            matrix_mult(r, transform)
            i += 2
            #print_matrix(transform)
        elif command == "apply":
            matrix_mult(transform, points)
            i += 1
            #print_matrix(points)
        elif command == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            i += 1
        elif command == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, lines[i+1])
            i += 2
        elif command == "quit":
            i = len(lines)
        else:
            i += 1
