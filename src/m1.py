"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_drive_system()


def run_test_drive_system():
    """ Tests the  drive_system  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the drive system.")
    print("Move at (20, 50) - that is, veer left slowly")
    robot.drive_system.start_moving(20, 50)
    time.sleep(2)
    robot.drive_system.stop_moving()

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    time.sleep(1)
    print()
    print("Spin clockwise at half speed for 2.5 seconds")
    robot.drive_system.move_for_seconds(2.5, 50, -50)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun(2000)

    time.sleep(1)
    print()
    print("Move forward at full speed for 1.5 seconds, coast to stop")
    robot.drive_system.start_moving()
    time.sleep(1.5)
    robot.drive_system.stop_moving(rb.StopAction.COAST)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())


main()
