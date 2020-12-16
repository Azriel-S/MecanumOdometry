from sympy import *
from contextlib import redirect_stdout
from os.path import abspath, dirname, join


init_printing(use_unicode=True, wrap_line=False)


def print_equations(velocity_robot_x, velocity_robot_y, angular_velocity_robot):
    """ print the equations to the screen """

    print('Velocity of the robot relative to itself in the x direction')
    pprint(velocity_robot_x)
    print()

    print('Velocity of the robot relative to itself in the y direction')
    pprint(velocity_robot_y)
    print()

    print('Angular Velocity of the robot relative to itself - how fast the robot is rotating')
    pprint(angular_velocity_robot)


def solve_equation(equation, variables, Wlf, Wlb, Wrf, Wrb, l, b, R):
    """ solve an equation numerically """

    print("Solve this")
    pprint(equation)

    result = equation.\
        subs(variables['Wlf'], Wlf).\
        subs(variables['Wlb'], Wlb).\
        subs(variables['Wrf'], Wrf).\
        subs(variables['Wrb'], Wrb).\
        subs(variables['l'], l). \
        subs(variables['b'], b). \
        subs(variables['R'], R). \
        evalf()

    print('Result')
    pprint(result)


def write_to_file(filename, velocity_robot_x, velocity_robot_y, angular_velocity_robot):
    """ Write the equations to a file """

    with open(filename, 'w', encoding='utf-8') as f:
        with redirect_stdout(f):
            print('Velocity of the robot relative to itself in the x direction')
            pprint(velocity_robot_x)
            print()

            print('Velocity of the robot relative to itself in the y direction')
            pprint(velocity_robot_y)
            print()

            print('Angular Velocity of the robot relative to itself - how fast the robot is rotating')
            pprint(angular_velocity_robot)


def ticks_to_radians(ticks, ticks_per_revolution):
    """ convert ticks to radians"""

    return (ticks / ticks_per_revolution * 2 * pi).evalf()


def solve_kinematics(source_path):
    # equation at the end of 2.3
    Wlf, Wlb, Wrf, Wrb = symbols('Wlf Wlb Wrf Wrb')     # Wheel angular speed in radians
    l = symbols('l')                                    # l is half the width between wheels - left right distance
    b = symbols('b')                                    # b is half the wheel base - front back distance
    R = symbols('R')                                    # Radius of wheel
    variables = {'Wlf': Wlf, 'Wlb': Wlb, 'Wrf': Wrf, 'Wrb': Wrb, 'l': l, 'b': b, 'R': R}

    M1 = Matrix([[1, 1, 1, 1], [-1, 1, -1, 1], [-1/(l + b), -1/(l + b), 1/(l + b), 1/(l + b)]])
    print("M1")
    pprint(M1)
    print()

    V1 = Matrix([[Wlf], [Wlb], [Wrb], [Wrf]])
    print("V1")
    pprint(V1)
    print()

    velocity = R / 4 * M1 * V1
    print("velocity")
    pprint(velocity)
    print()

    velocity_robot_x = velocity[0]
    velocity_robot_y = velocity[1]
    angular_velocity_robot = velocity[2]

    print_equations(velocity_robot_x, velocity_robot_y, angular_velocity_robot)

    ticks_per_revolution = 1120
    half_robot_width = 16 / 2.0
    half_robot_wheelbase = 14 / 2.0
    wheel_radius = 2

    rotation_left_front = ticks_to_radians(ticks_per_revolution / 2, ticks_per_revolution)
    rotation_left_rear = ticks_to_radians(ticks_per_revolution / 2, ticks_per_revolution)
    rotation_right_front = ticks_to_radians(ticks_per_revolution / 2, ticks_per_revolution)
    rotation_right_rear = ticks_to_radians(ticks_per_revolution / 2, ticks_per_revolution)

    print("Solve Velocity Robot X")
    solve_equation(velocity_robot_x, variables, rotation_left_front, rotation_left_rear,
                   rotation_right_front, rotation_right_rear, half_robot_width, half_robot_wheelbase, wheel_radius)

    print()
    print("Solve Velocity Robot Y")
    solve_equation(velocity_robot_y, variables, rotation_left_front, rotation_left_rear,
                   rotation_right_front, rotation_right_rear, half_robot_width, half_robot_wheelbase, wheel_radius)

    print()
    print("Solve Angular Velocity Robot")
    solve_equation(angular_velocity_robot, variables, rotation_left_front, rotation_left_rear,
                   rotation_right_front, rotation_right_rear, half_robot_width, half_robot_wheelbase, wheel_radius)

    write_to_file(source_path, velocity_robot_x, velocity_robot_y, angular_velocity_robot)


if __name__ == '__main__':
    BASE_PATH = dirname(abspath(__file__))
    SOURCE_PATH = join(BASE_PATH, 'MecanumKinematics_Output.txt')
    solve_kinematics(SOURCE_PATH)
