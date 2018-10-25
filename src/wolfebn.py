"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """


main()
    color = 'blue'
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(100,100)
    robot.color_sensor.wait_until_color_is(color)