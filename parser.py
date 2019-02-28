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
    lines = f.read().split()
    i = 0
    while i < len(lines):
        command = lines[i]
        if command == "line":
            c = [int(c) for c in lines[i+1].split(" ")]
            add_edge(points, c[0], c[1], c[2], c[3], c[4], c[5])
            n += 2
        elif command == "ident"
            ident(transform)
            n += 1
        elif command == "scale"
            c = [int(c) for c in lines[i+1].split(" ")]
            s = make_scale(c[0], c[1], c[2])
            matrix_mult(s, transform)
            n += 2
        elif command == "rotate"
            pass
        elif command == "translate"
            pass
        elif command == "apply"
            pass
        elif command == "display"
            pass
        elif command == "save"
            pass
        elif command = "quit"
            pass
        else:
            x += 1
