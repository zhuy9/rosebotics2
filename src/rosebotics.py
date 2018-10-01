"""
  Capstone Project.  Code shared by the team.
  Team members:  PUT_YOUR_NAMES_HERE.
  Fall term, 2018-2019.
"""

from ev3dev import ev3
from enum import Enum


class StopAction(Enum):
    COAST = 'coast'
    BRAKE = 'brake'
    HOLD = 'hold'


class Snatch3rRobot(object):
    """ A Snatch3r robot. """

    # With students, write __init__, go, stop.
    def __init__(self,
                 left_wheel_port=ev3.OUTPUT_B,
                 right_wheel_port=ev3.OUTPUT_C):
        self.left_wheel = Wheel(left_wheel_port)
        self.right_wheel = Wheel(right_wheel_port)

        self.left_wheel.reset_degrees_spun()
        self.right_wheel.reset_degrees_spun()

    def go(self,
           left_wheel_duty_cycle_percent=None,
           right_wheel_duty_cycle_percent=None):
        self.left_wheel.start_spinning(left_wheel_duty_cycle_percent)
        self.right_wheel.start_spinning(right_wheel_duty_cycle_percent)

    def stop(self, stop_action=None):
        self.left_wheel.stop_spinning(stop_action)
        self.right_wheel.stop_spinning(stop_action)


class Wheel(object):
    def __init__(self, port, default_duty_cycle_percent=100,
                 default_stop_action=StopAction.BRAKE.value):
        """
        Constructs a LargeMotor at the given port, where port should be one of:
          -- ev3.OUTPUT_A
          -- ev3.OUTPUT_B
          -- ev3.OUTPUT_C

        Sets the defaults for the:
          -- duty_cycle_percent:  The duty cycle is the fraction of the time
               to which power is supplied to the motor.  Hence, we can think
               of the duty_cycle_percent as the "power" sent to the motor
               when we ask the motor to start spinning.
          -- stop_action:  What the motor should do when told to stop.  One of:
               -- StopAction.BRAKE.value
               -- StopAction.COAST.value
               -- StopAction.HOLD.value

          :type default_duty_cycle_percent: int
          :type default_stop_action:        str
        """
        self.motor = ev3.LargeMotor(port)
        self.default_duty_cycle_percent = default_duty_cycle_percent
        self.default_stop_action = default_stop_action

    def start_spinning(self, duty_cycle_percent=None):
        """
        Starts this Wheel's motor spinning at the given duty_cycle_percent.
          --  100 -> full power, spin clockwise
          -- -100 -> full power, spin counter-clockwise

          :type duty_cycle_percent: int
        """
        if duty_cycle_percent is None:
            duty_cycle_percent = self.default_duty_cycle_percent
        self.motor.run_direct(duty_cycle_sp=duty_cycle_percent)

    def stop_spinning(self, stop_action=None):
        """
        Stops this Wheel's motor from spinning, using the given stop_action,
        which must be one of:
          -- StopAction.BRAKE.value
          -- StopAction.COAST.value
          -- StopAction.HOLD.value

          :type stop_action: str
        """
        if stop_action is None:
            stop_action = self.default_stop_action
        self.motor.stop(stop_action=stop_action)

    def get_degrees_spun(self):
        return self.motor.position

    def reset_degrees_spun(self, position=0):
        self.motor.position = position
