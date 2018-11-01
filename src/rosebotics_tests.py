"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    # run_test_ir()
    run_test_drive_system()
    # run_test_touch_sensor()
    # run_test_color_sensor()
    run_test_arm()


def run_test_arm():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()
    time.sleep(1)
    robot.arm.raise_arm_and_close_claw()
    time.sleep(1)
    robot.arm.move_arm_to_position(300)


def run_test_ir():
    robot = rb.Snatch3rRobot()

    while True:
        # TODO: Print the value of the following, one at a time. For each,
        # TODO:   do the appropriate user actions (e.g. try pressing a button
        # TODO:   on the Beacon and see what the beacon_button_sensor produces).
        # TODO:   Discover what values the sensors produce in which situations.
        #    touch_sensor
        #    color_sensor
        #    camera
        #    proximity_sensor
        #    beacon_sensor  NOT YET IMPLEMENTED
        #    beacon_button_sensor  NOT YET IMPLEMENTED
        print("Touch sensor:",
              robot.touch_sensor.get_value(),
              robot.touch_sensor.is_pressed())

        character = input(
            "Press the ENTER (return) key to continue, or q to quit: ")
        if character == "q":
            break


def run_test_drive_system():
    """ Tests the  drive_system  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  drive_system  of the robot.")
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
    robot.drive_system.stop_moving(rb.StopAction.COAST.value)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())


def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  touch_sensor  of the robot.")
    print("Repeatedly press and release the touch sensor.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Color sensor value/color/intensity is: ",
              "{:3} {:3} {:3}".format(robot.color_sensor.get_value()[0],
                                      robot.color_sensor.get_value()[1],
                                      robot.color_sensor.get_value()[2]),
              "{:4}".format(robot.color_sensor.get_color()),
              "{:4}".format(robot.color_sensor.get_reflected_intensity()))
        time.sleep(0.5)
        count = count + 1


main()
