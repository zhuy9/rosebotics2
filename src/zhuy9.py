
"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(1)

    # make_polygon(5)
    # follow_the_black-line()

def make_polygon(n):
    robot = rb.Snatch3rRobot()
    for i in range(n):
        robot.drive_system.go_straight_inches(2)
        robot.drive_system.turn_degrees(180 / n)

def follow_the_black_line():
    robot = rb.Snatch3rRobot()
    robot.color_sensor.get_color()
    while True:
        robot.drive_system.start_moving(100, 100)
        if robot.color_sensor.get_color() != 1:
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(-14, 99)

main()
