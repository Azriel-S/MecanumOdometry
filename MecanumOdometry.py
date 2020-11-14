from sympy import *
from contextlib import redirect_stdout
from os.path import abspath, dirname, join


init_printing(use_unicode=False, wrap_line=False)


def solve_odometry(source_path):
    x_global_last, y_global_last, theta_global_last = symbols('x_global_last, y_global_last, theta_global_last')

    M1_position_global = Matrix([[x_global_last], [y_global_last], [theta_global_last]])
    pprint(M1_position_global)
    print()

    M2_position_global = Matrix([[cos(theta_global_last), -sin(theta_global_last), 0],
                                 [sin(theta_global_last), cos(theta_global_last), 0],
                                 [0, 0, 1]])
    pprint(M2_position_global)
    print()

    position_x_robot_change, position_y_robot_change, rotation_robot_change = \
        symbols('position_x_robot_change, position_y_robot_change, rotation_robot_change')

    M3_position_global = Matrix([[sin(rotation_robot_change)/rotation_robot_change, -(1-cos(rotation_robot_change))/rotation_robot_change, 0],
                                 [(1-cos(rotation_robot_change))/rotation_robot_change, sin(rotation_robot_change)/rotation_robot_change, 0],
                                 [0,0,1]])
    pprint(M3_position_global)
    print()

    M4_position_global = Matrix([[position_x_robot_change], [position_y_robot_change], [rotation_robot_change]])
    pprint(M4_position_global)
    print()

    position_global_current = M1_position_global + M2_position_global*M3_position_global*M4_position_global
    pprint(position_global_current)
    print()

    print('Current X position in the global coordinate system')
    x_position_global_current = position_global_current[0]
    pprint(x_position_global_current)
    print()

    print('Current Y position in the global coordinate system')
    y_position_global_current = position_global_current[1]
    pprint(y_position_global_current)
    print()

    print('Current rotation in the global coordinate system')
    rotation_global_current = position_global_current[2]
    pprint(rotation_global_current)

    with open(source_path, 'w', encoding='utf-8') as f:
        with redirect_stdout(f):
            print('Current X position in the global coordinate system')
            pprint(x_position_global_current)
            print()

            print('Current Y position in the global coordinate system')
            pprint(y_position_global_current)
            print()

            print('Current rotation in the global coordinate system')
            pprint(rotation_global_current)


if __name__ == '__main__':
    BASE_PATH = dirname(abspath(__file__))
    SOURCE_PATH = join(BASE_PATH, 'MecanumOdometry_Output2.txt')
    solve_odometry(SOURCE_PATH)
