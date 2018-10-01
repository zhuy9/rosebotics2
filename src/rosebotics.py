from ev3dev import ev3

from enum import Enum

StopAction = Enum('StopAction', 'COAST BRAKE HOLD')


class Snatch3rRobot(object):
    def __init__(self,
                 left_wheel_port=ev3.OUTPUT_B,
                 right_wheel_port = ev3.OUTPUT_C):
        self.left_wheel = Wheel(left_wheel_port)
        self.right_wheel = Wheel(right_wheel_port)

    def go(self,
           left_wheel_duty_cycle_percent=None,
           right_wheel_duty_cycle_percent=None):
        self.left_wheel.start_spinning(left_wheel_duty_cycle_percent)
        self.right_wheel.start_spinning(left_wheel_duty_cycle_percent)

    def stop(self, stop_action=None):
        self.left_wheel.stop_spinning(stop_action)
        self.right_wheel.stop_spinning(stop_action)


class Wheel(object):
    def __init__(self, port, default_duty_cycle_percent=100,
                 default_stop_action=StopAction.BRAKE):
        self.default_duty_cycle_percent = default_duty_cycle_percent
        self.default_stop_action = default_stop_action

        self.motor = ev3.LargeMotor(port)

    def start_spinning(self, duty_cycle_percent=None):
        """ """
        if duty_cycle_percent is None:
            duty_cycle_percent = self.default_duty_cycle_percent
        self.motor.run_direct(duty_cycle_sp=duty_cycle_percent)

    def stop_spinning(self, stop_action=None):
        if stop_action is None:
            stop_action = self.default_stop_action
        self.motor.stop(stop_action=stop_action)

