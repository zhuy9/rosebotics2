"""
  Capstone Project.  This module contains high-level code that should be useful
  for a variety of applications of the robot.  Augment as appropriate.

  Team # PUT_YOUR_TEAM_NUMBER_HERE.
  Team members:  PUT_YOUR_NAMES_HERE.
  Fall term, 2018-2019.
"""

from ev3dev import ev3
from enum import Enum
import low_level_rosebotics as rb
import time


class StopAction(Enum):
    COAST = 'coast'
    BRAKE = 'brake'
    HOLD = 'hold'


class Color(Enum):
    NO_COLOR = 0
    BLACK = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5
    WHITE = 6
    BROWN = 7


class Snatch3rRobot(object):
    """ An EV3 Snatch3r Robot. """

    def __init__(self,
                 left_wheel_port=ev3.OUTPUT_B,
                 right_wheel_port=ev3.OUTPUT_C,
                 arm_port=ev3.OUTPUT_A,
                 touch_sensor_port=ev3.INPUT_1,
                 camera_port=ev3.INPUT_2,
                 color_sensor_port=ev3.INPUT_3,
                 infrared_sensor_port=ev3.INPUT_4):
        # All the methods in this class "delegate" their work to the appropriate
        # subsystem:  drive_system, touch_sensor, camera, olor_sensor, etc.
        self.drive_system = DriveSystem(left_wheel_port, right_wheel_port)
        # self.arm = ArmAndClaw(arm_port)
        self.touch_sensor = TouchSensor(touch_sensor_port)
        # self.camera = Camera(camera_port)
        self.color_sensor = ColorSensor(color_sensor_port)
        # self.infrared_sensor = InfraredSensor(infrared_sensor_port)


class DriveSystem(object):
    """
    A class for driving (moving) the robot.
    Primary authors:  entire team plus PUT_YOUR_NAME_HERE.
    """

    def __init__(self,
                 left_wheel_port=ev3.OUTPUT_B,
                 right_wheel_port=ev3.OUTPUT_C):
        self.left_wheel = rb.Wheel(left_wheel_port)
        self.right_wheel = rb.Wheel(right_wheel_port)

    def start_moving(self,
                     left_wheel_duty_cycle_percent=100,
                     right_wheel_duty_cycle_percent=100):
        """ Start moving at the given wheel speeds (-100 to 100)."""
        self.left_wheel.start_spinning(left_wheel_duty_cycle_percent)
        self.right_wheel.start_spinning(right_wheel_duty_cycle_percent)

    def stop_moving(self, stop_action=StopAction.BRAKE):
        """ Stop moving, using the given StopAction. """
        self.left_wheel.stop_spinning(stop_action)
        self.right_wheel.stop_spinning(stop_action)

    def move_for_seconds(self,
                         seconds,
                         left_wheel_duty_cycle_percent=100,
                         right_wheel_duty_cycle_percent=100,
                         stop_action=StopAction.BRAKE):
        """
        Move for the given number of seconds at the given wheel speeds.
        Speeds are -100 to 100, where negative means moving backwards.
        """
        self.start_moving(left_wheel_duty_cycle_percent,
                          right_wheel_duty_cycle_percent)
        # For pedagogical purposes, we use a WHILE loop to keep  going for a
        # given number of seconds, instead of using the simpler alternative:
        #      time.sleep(seconds)
        self.start_moving(left_wheel_duty_cycle_percent,
                          right_wheel_duty_cycle_percent)
        start_time = time.time()
        while True:
            if time.time() - start_time > seconds:
                self.stop_moving(stop_action)
                break

    def go_straight_inches(self,
                           inches,
                           duty_cycle_percent=100,
                           stop_action=StopAction.BRAKE):
        """
        Go straight at the given speed (-100 to 100, negative is backwards)
        for the given number of inches, stopping with the given StopAction.
        """
        # TODO: Do a few experiments to determine the constant that converts
        # TODO:   from wheel-degrees-spun to robot-inches-moved.
        # TODO:   Assume that the conversion is linear with respect to speed.

    def spin_in_place_degrees(self,
                              degrees,
                              duty_cycle_percent=100,
                              stop_action=StopAction.BRAKE):
        """
        Spin in place (i.e., both wheels move, in opposite directions)
        the given number of degrees, at the given speed (-100 to 100,
        where positive is clockwise and negative is counter-clockwise),
        stopping by using the given StopAction.
        """
        # TODO: Do a few experiments to determine the constant that converts
        # TODO:   from wheel-degrees-spun to robot-degrees-spun.
        # TODO:   Assume that the conversion is linear with respect to speed.
    def turn_degrees(self,
                     degrees,
                     duty_cycle_percent=100,
                     stop_action=StopAction.BRAKE):
        """
        Turn (i.e., only one wheel moves)
        the given number of degrees, at the given speed (-100 to 100,
        where positive is clockwise and negative is counter-clockwise),
        stopping by using the given StopAction.
        """
        # TODO: Do a few experiments to determine the constant that converts
        # TODO:   from wheel-degrees-spun to robot-degrees-turned.
        # TODO:   Assume that the conversion is linear with respect to speed.


class ArmAndClaw(object):
    def __init__(self, touch_sensor, port=ev3.OUTPUT_A):
        self.motor = ev3.MediumMotor(port)
        self.touch_sensor = touch_sensor
        self.calibrate()  # Sets the motor's position to 0 at the DOWN position.


    def calibrate(self):
        """
        Raise the arm to until the touch sensor is pressed.
        Then lower the arm XXX units.
        Set the motor's position to 0 at that point.
        (Hence, 0 means all the way DOWN and XXX means all the way UP).
        """
        # TODO

    def raise_arm_and_close_claw(self):
        """
        Raise the arm (and hence close the claw).
        Stop when the touch sensor is pressed.
        """
        # TODO

    def lower_arm_and_open_claw(self):
        """
        Raise the arm (and hence close the claw).
        Stop when the touch sensor is pressed.
        """
        # TODO

    def move_arm_to_position(self, position):
        """ Spin the arm's motor until it reaches the given position. """
        # TODO


class TouchSensor(rb.TouchSensor):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """

    def __init__(self, port=ev3.INPUT_1):
        super().__init__(port)

    def wait_until_pressed(self):
        """ Waits (doing nothing new) until the touch sensor is pressed. """
        while True:
            if self.get_value() == 1:
                break



        # Done.

    def wait_until_released(self):
        """ Waits (doing nothing new) until the touch sensor is released. """
        while True:
            if self.get_value() == 0:
                break


        # Done


class Camera(object):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """


class ColorSensor(rb.ColorSensor):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """

    def __init__(self, port=ev3.INPUT_3):
        super().__init__(port)

    def wait_until_intensity_is_less_than(self, reflected_light_intensity):
        """
        Waits (doing nothing new) until the sensor's measurement of reflected
        light intensity is less than the given value (threshold), which should
        be between 0 (no light reflected) and 100 (maximum light reflected).
        """
        while True:
            if self.get_reflected_intensity()>reflected_light_intensity:
                break






        # Done.

    def wait_until_intensity_is_greater_than(self, reflected_light_intensity):
        """
        Waits (doing nothing new) until the sensor's measurement of reflected
        light intensity is greater than the given value (threshold), which
        should be between 0 (no light reflected) and 100 (max light reflected).
        """
        while True:
            if self.get_reflected_intensity()<reflected_light_intensity:
                break



        # Done.

    def wait_until_color_is(self, color):
        """
        Waits (doing nothing new) until the sensor's measurement
        of what color it sees is the given color.
        The given color must be a Color (as defined above).
        """
        while True:
            if self.get_color() == color:
                break


        # Done.

    def wait_until_color_is_one_of(self, colors):
        """
        Waits (doing nothing new) until the sensor's measurement
        of what color it sees is any one of the given sequence of colors.
        Each item in the sequence must be a Color (as defined above).
        """
        while True:
            for k in range(len(colors)):
                if self.get_color() == colors[k]:
                    break



        # Done.


class InfraredSensorAsProximitySensor(object):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """
    def __init__(self, port=ev3.INPUT_4):
        super().__init__(port)


class InfraredSensorAsBeaconSensor(object):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """

class InfraredSensorAsBeaconButtonSensor(object):
    """ Primary author of this class:  PUT_YOUR_NAME_HERE. """