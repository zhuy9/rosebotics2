
"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """

    # robot = rb.Snatch3rRobot()
    # robot.drive_system.go_straight_inches(10)
    # make_polygon(5)
    # follow_the_black_line()
    # beep_when_area_is_bigger_than(20)
    # IR_sensor(10)

    print('------SPRINT ONE-------')
    print("test drive system")  # OK
    # test_drive_system()
    # time.sleep(5)

    print('test follow black line')
    print('in clockwise')
    # follow_black_line()
    # follow_black_line_fancy_version()
    time.sleep(5)

    print('move forward until see black:')
    # until_color_is(1)
    # time.sleep(5)

    print('----end of sprint one------')





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

    # def Infrared_Beacon_Button():
    #     #A GUI running on your laptop has a button labeled “Infrared Beacon”.  Pressing the button makes the robot spin
    #     # (once) toward the Beacon (which must be in “beacon mode”), then move (once) toward the Beacon.
    #     rbt = rb.Snatch3rRobot()
    #     root = tkinter.Tk()
    #     root.title("test IR Beacon")
    #
    #     frame = ttk.Frame(root, padding=20)
    #     frame.grid()
    #
    #     IR_Beacon = ttk.Button(frame, text="Infrared Beacon")
    #     IR_Beacon.grid()
    #     IR_Beacon['command'] = lambda: spin_move_to_beacon(rbt)
    #
    # def spin_move_to_beacon(robot):
    #     while True:
    #         #    beacon_sensor
    #         #    beacon_button_sensor
    #         degree = robot.beacon_sensor.get_heading_to_beacon()
    #         robot.drive_system.turn_degrees(degree)
    #         distance = robot.beacon_sensor.get_distance_to_beacon()
    #         robot.drive_system.go_straight_inches(0.7 * distance / 2.54)
    #
    #         character = input(
    #             "Press the ENTER (return) key to continue, or q to quit: ")
    #         if character == "q":
    #             break

def test_drive_system():
    run_test_go_straight_pos_inches()
    run_test_go_straight_neg_inches()
    run_test_spin_in_place_pos_degrees()
    run_test_spin_in_place_neg_degrees()
    run_test_turn_pos_degrees()
    run_test_turn_neg_degrees()


def follow_black_line(): # NO ISSUE FOUND
    print('-----follow black line initiated------')
    print('Action required: Put the robot on the black line')
    print('To exist, press the touch sensor on the robot')
    rbt = rb.Snatch3rRobot()
    while True:
        if rbt.touch_sensor.get_value() == 0:
            rbt.drive_system.start_moving(80, 50)
            if rbt.color_sensor.get_color() != 1:
                rbt.drive_system.start_moving(90, -50)
        else:
            rbt.drive_system.stop_moving()
            print('-----follow black line terminated------')
            break
    #####
    # self.left_wheel.start_spinning(left_wheel_duty_cycle_percent)
    # self.right_wheel.start_spinning(right_wheel_duty_cycle_percent)
    #####


# def run_draw_polygons(x):
#     print('--------test draw polygons-------')
#     robot = rb.Snatch3rRobot()
#
#     for k in range(x):
#         robot.drive_system.start_moving(90, 90)
#         time.sleep(0.5)
#         robot.drive_system.turn_degrees(180/x)
#     robot.drive_system.stop_moving()



def until_color_is(color): # DONE & RUNNING OK
    print('----test run until color is----')
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(60, 60)
    while True:
        robot.color_sensor.wait_until_color_is(color)
        robot.drive_system.stop_moving()
        break


#################
# drive system  #
#################

def run_test_go_straight_pos_inches():
    robot = rb.Snatch3rRobot()
    print("move forward 10")
    robot.drive_system.go_straight_inches(10)
    robot.drive_system.stop_moving()
    time.sleep(5)

def run_test_go_straight_neg_inches():
    robot = rb.Snatch3rRobot()
    print('move backward 10')
    robot.drive_system.go_straight_inches(-10)
    robot.drive_system.stop_moving()
    time.sleep(5)


def run_test_spin_in_place_pos_degrees():
    robot = rb.Snatch3rRobot()
    print('Spin 90')
    robot.drive_system.spin_in_place_degrees(90)
    robot.drive_system.stop_moving()
    time.sleep(5)

def run_test_spin_in_place_neg_degrees():
    robot = rb.Snatch3rRobot()
    print('Spin -90')
    robot.drive_system.spin_in_place_degrees(-90)
    robot.drive_system.stop_moving()
    time.sleep(5)


def run_test_turn_pos_degrees():
    robot = rb.Snatch3rRobot()
    print('Turn 45')
    robot.drive_system.start_moving(50, 50)
    time.sleep(2)
    robot.drive_system.turn_degrees(45)
    robot.drive_system.stop_moving()
    time.sleep(5)

def run_test_turn_neg_degrees():
    robot = rb.Snatch3rRobot()
    print('Turn -45')
    robot.drive_system.start_moving(50, 50)
    time.sleep(2)
    robot.drive_system.turn_degrees(-45)
    robot.drive_system.stop_moving()
    time.sleep(5)





main()
