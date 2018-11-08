"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.
Also: responds to Beacon button-presses by beeping, speaking.
This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.
Authors:  David Mutchler, his colleagues, and yuchen zhu
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)

    # initiating client
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()


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
    print('Pressing the Top-Red Beacon button makes the robot beep once.  '
          'Pressing the Top-Blue Beacon button makes the robot say “Hello. How are you?”')
    print('exit by ctrl + c ')
    while True:

        if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
            ev3.Sound.beep().wait(0.1)
        if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
            ev3.Sound.speak("hello. How are you?").wait(0.1)

        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Store the robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot


    def go_forward(self, speed_string):
        """makes the robot go forward at given speed"""
        print('telling the robot to start moving at the given speed:', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


main()
