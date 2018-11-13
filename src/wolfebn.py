"""
  Capstone Project.  Code written by Bryan Wolfe.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import rosebotics_new as rbnew
import time


def main():
    """ Runs YOUR specific part of the project """

    #apptest()
    armtest()


def apptest():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(8)
    robot.drive_system.stop_moving()
    time.sleep(1)
    robot.drive_system.spin_in_place_degrees(360)
    robot.drive_system.stop_moving()
    time.sleep(1)
    robot.drive_system.turn_degrees(90)
    robot.drive_system.stop_moving()
    time.sleep(1)
def armtest():
    robot = rbnew.Snatch3rRobot()
    robot.arm.calibrate()



main()
