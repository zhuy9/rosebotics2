
"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    """ Runs YOUR specific part of the project """

    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(1)

    # make_polygon(5)
    # follow_the_black_line()
    # beep_when_area_is_bigger_than(20)
    # IR_sensor(10)

def make_polygon(n):
    robot = rb.Snatch3rRobot()
    for i in range(n):
        robot.drive_system.go_straight_inches(2)
        robot.drive_system.turn_degrees(180 / n)

def follow_the_black_line():
    robot = rb.Snatch3rRobot()
    color = robot.color_sensor.get_color()
    print(color)
    while True:
        robot.drive_system.start_moving(100, 100)
        if robot.color_sensor.get_color() != 1:
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(-14, 99)

def follow_black_line_advanced():
    rem_direction = 0
    robot = rb.Snatch3rRobot()

    if robot.color_sensor.get_color() == 1:
        robot.drive_system.go_straight_inches(2)
        robot.drive_system.spin_in_place_degrees(-45)

        if robot.color_sensor.get_color() == 1:
            rem_direction = 1
        else:
            rem_direction = -1
        robot.drive_system.stop_moving(45)

    while True:
        robot.drive_system.start_moving(100, 100)
        if robot.color_sensor.get_color() != 1:
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(-14 * rem_direction, 99 * rem_direction)
        # to be tested

def beep_when_area_is_bigger_than(area):
        robot = rb.Snatch3rRobot()
        while True:
            if robot.camera.get_biggest_blob().get_area() >= area:
                ev3.Sound.beep().wait()
            if robot.touch_sensor.is_pressed() is True:
                break

def IR_sensor(distance):        # in inches, not SI.  emmmmm
    robot = rb.Snatch3rRobot()
    while True:
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= distance:
            ev3.Sound.beep().wait()
        if robot.touch_sensor.is_pressed() is True:
            break


main()
