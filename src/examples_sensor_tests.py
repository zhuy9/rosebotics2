"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  Fall term, 2018-2019.
"""

import rosebotics_even_newer as rb
import time


def main():
    """ Runs tests. """
    run_test_sensors()


def run_test_sensors():
    """ Print sensor values each time the user presses the ENTER key. """
    robot = rb.Snatch3rRobot()

    while True:
        print()
        print("Touch sensor (value, is_pressed):",
              robot.touch_sensor.get_value(),
              robot.touch_sensor.is_pressed())
        print("Color sensor (reflected intensity, color):",
              robot.color_sensor.get_reflected_intensity(),
              robot.color_sensor.get_color())
        print("Camera:", robot.camera.get_biggest_blob())
        print("Brick buttons:",
              robot.brick_button_sensor.is_back_button_pressed(),
              robot.brick_button_sensor.is_top_button_pressed(),
              robot.brick_button_sensor.is_bottom_button_pressed(),
              robot.brick_button_sensor.is_left_button_pressed(),
              robot.brick_button_sensor.is_right_button_pressed())

        # ----------------------------------------------------------------------
        # On each run, use just ONE of the following 3 sensors:
        # ----------------------------------------------------------------------
        print("Proximity sensor (inches):",
              robot.proximity_sensor.get_distance_to_nearest_object_in_inches())
        # print("Beacon sensor (cm, degrees):",
        #       robot.beacon_sensor.get_distance_to_beacon(),
        #       robot.beacon_sensor.get_heading_to_beacon())
        # print("Beacon button sensor (top/bottom red, top/bottom blue):",
        #       robot.beacon_button_sensor.is_top_red_button_pressed(),
        #       robot.beacon_button_sensor.is_bottom_red_button_pressed(),
        #       robot.beacon_button_sensor.is_top_blue_button_pressed(),
        #       robot.beacon_button_sensor.is_bottom_blue_button_pressed())

        character = input(
            "Press the ENTER (return) key to get next sensor reading, or q to quit: ")
        if character == "q":
            break


main()
