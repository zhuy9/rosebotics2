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
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """

    def go_forward(self, speed_string):
        """Makes the robot go forward at the given speed."""
        print("Telling the robot to start moving at", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


main()