from sympy import *
from contextlib import redirect_stdout
from os.path import abspath, dirname, join


init_printing(use_unicode=True, wrap_line=False)


def solve_odometry(source_path):
    # length, width, wheel_diameter = symbols('l w R')
    # encoder_left_front, encoder_right_front, encoder_left_rear, encoder_right_rear = symbols('Elf Erf Elr Err')
    # position_left_front, position_right_front, position_left_rear, position_right_rear = symbols('Tlf Trf Tlr Trr')
    # velocity_left_front, velocity_right_front, velocity_left_rear, velocity_right_rear = symbols('Wlf Wrf Wlr Wrr')
    x_global_current, y_global_current, theta_global_current = symbols('Xgt1 Ygt1 Tgt1')
    x_global_last, y_global_last, theta_global_last = symbols('Xgt Ygt Tgt')

    M1_position_global = Matrix([[x_global_last], [y_global_last], [theta_global_last]])
    pprint(M1_position_global)
    print()

    M2_position_global = Matrix([[cos(theta_global_last), -sin(theta_global_last), 0],
                                 [sin(theta_global_last), cos(theta_global_last), 0],
                                 [0, 0, 1]])
    pprint(M2_position_global)
    print()

    position_x_robot_change, position_y_robot_change, rotation_robot_change = symbols('Delta_Xr Delta_Yr Delta_Theta_r')

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
    SOURCE_PATH = join(BASE_PATH, 'MecanumOdometry_Output.txt')
    solve_odometry(SOURCE_PATH)
