"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    apptest(robot, 8, 360, 90)


def apptest(robot, inches, deg, deg2):

    robot.drive_system.go_straight_inches(inches)
    robot.drive_system.stop_moving()
    time.sleep(1)
    robot.drive_system.spin_in_place_degrees(deg)
    time.sleep(1)
    robot.drive_system.turn_degrees(deg2)
    time.sleep(1)
    robot.arm.calibrate()



main()
