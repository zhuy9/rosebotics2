"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """


main()

    robot = rb.Snatch3rRobot()


def make_polygon(self, sides, scale):
    deg = 360/sides
    for k in range(sides):
        robot.move_forward_inches(scale)
        robot.turn_in_place(deg)

