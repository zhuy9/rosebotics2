"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Bryan Wolfe.
"""
# ------------------------------------------------------------------------------
# Done: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, review the "big picture" of laptop-robot
# Done:    communication, per the comment in mqtt_sender.py.
# Done:    Once you understand the "big picture", delete this Done.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # Done: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # Done: 4. Add code that constructs a   com.MqttClient   that will
    # Done:    be used to receive commands sent by the laptop.
    # Done:    Connect it to this robot.  Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    client = com.MqttClient(rc)
    client.connect_to_pc()
    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, robot):
        self.robot = robot
        self.T = 0 #Robot's Travel Time
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """

    def go_forward(self, speed_string):
        """Makes the robot go forward at the given speed."""
        print("Telling the robot to start moving at", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def get_distance(self):
        dist = self.robot.proximity_sensor.get_distance_to_nearest_object()
        print(dist, 'cm away from sensor')

    def raise_arm(self):
        self.robot.arm.raise_arm_and_close_claw()
        print('Raising Arm')

    def lower_arm(self):
        self.robot.arm.motor.start_spinning(-100)
        self.robot.arm.motor.reset_degrees_spun()
        while True:
            if self.robot.arm.motor.get_degrees_spun() <= 14.2 * -360:
                self.robot.arm.motor.stop_spinning()
                break
        print('Lowering Arm')

    def reverse(self):
       # self.robot.drive_system.spin_in_place_degrees(180)
        self.robot.drive_system.left_wheel.start_spinning(40)
        self.robot.drive_system.right_wheel.start_spinning(-40)
        time.sleep(4)
        self.robot.drive_system.left_wheel.start_spinning(0)
        self.robot.drive_system.right_wheel.start_spinning(0)
        print("Reversing Direction")


    def travel_to_target(self):
        t = time.time()
        self.robot.drive_system.start_moving(30, 30)
        while True:
            #print(self.robot.proximity_sensor.get_distance_to_nearest_object())
            if self.robot.proximity_sensor.get_distance_to_nearest_object() <= 3:
                self.robot.drive_system.stop_moving()
                T = time.time() - t
                self.T = T
                break

    def stop(self):
        self.robot.drive_system.stop_moving()

    def go_home(self):
        self.robot.drive_system.left_wheel.start_spinning(40)
        self.robot.drive_system.right_wheel.start_spinning(40)
        time.sleep(self.T)
        self.robot.drive_system.left_wheel.start_spinning(0)
        self.robot.drive_system.right_wheel.start_spinning(0)

    def back_up(self):
        self.robot.drive_system.left_wheel.start_spinning(-40)
        self.robot.drive_system.right_wheel.start_spinning(-40)
        time.sleep(2)
        self.robot.drive_system.left_wheel.start_spinning(0)
        self.robot.drive_system.right_wheel.start_spinning(0)

    def fetch(self, client):
        self.travel_to_target()
        time.sleep(0.2)
        self.raise_arm()
        time.sleep(0.2)
        self.reverse()
        time.sleep(0.2)
        self.go_home()
        time.sleep(0.2)
        self.lower_arm()
        time.sleep(0.2)
        self.back_up()
        time.sleep(0.2)
        self.reverse()
        override(client, 'Item Delivered')

def override(client, string):
    client.send_message('override', [string])

main()
