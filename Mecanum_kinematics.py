from sympy import *
init_printing(use_unicode=True, wrap_line=False)


def solve_kinematics():
    # equation at the end of 2.3
    Wlf, Wlb, Wrf, Wrb = symbols('Wlf Wlb Wrf Wrb')     # Wheel angular speed in radians
    l = symbols('l')                                    # l is half the width between wheels - left right distance
    b = symbols('b')                                    # b is half the wheel base - front back distance
    R = symbols('R')                                    # Radius of wheel
    M1 = Matrix([[1, 1, 1, 1], [-1, 1, -1, 1], [-1/(l + b), -1/(l + b), 1/(l + b), 1/(l + b)]])
    pprint(M1)
    print()

    V1 = Matrix([[Wlf], [Wlb], [Wrb], [Wrf]])
    pprint(V1)
    print()

    velocity = R / 4 * M1 * V1
    pprint(velocity)
    print()

    print('Velocity of the robot relative to itself in the x direction')
    velocity_robot_x = velocity[0]
    pprint(velocity_robot_x)
    print()

    print('Velocity of the robot relative to itself in the y direction')
    velocity_robot_y = velocity[1]
    pprint(velocity_robot_y)
    print()

    print('Angular Velocity of the robot relative to itself - how fast the robot is rotating')
    angular_velocity_robot = velocity[2]
    pprint(angular_velocity_robot)


if __name__ == '__main__':
    solve_kinematics()
