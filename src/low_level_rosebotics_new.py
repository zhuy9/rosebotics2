"""
  Capstone Project.  Low-level robot code.
  ** STUDY THIS MODULE but DO NOT MODIFY it. **
  Author: David Mutchler, extending work by Dave Fisher and others.
  Fall term, 2018-2019.
"""

from ev3dev import ev3


class Wheel(object):
    def __init__(self,
                 port,
                 default_duty_cycle_percent=100,
                 default_stop_action=ev3.Motor.STOP_ACTION_BRAKE,
                 is_arm=False):
        """
        Constructs a LargeMotor at the given port, where port should be one of:
          -- ev3.OUTPUT_A       ev3.OUTPUT_B    ev3.OUTPUT_C

        Sets the defaults for the:
          -- duty_cycle_percent:  The duty cycle is the fraction of the time
               to which power is supplied to the motor.  Hence, we can think
               of the duty_cycle_percent as the "power level" sent to the motor
               when we ask the motor to start spinning.
          -- stop_action:  What the motor should do when told to stop.  One of:
               -- StopAction.BRAKE.value      StopAction.COAST.value
                      StopAction.HOLD.value
        Resets the wheel positions to 0.

          :type  default_duty_cycle_percent:  int
          :type  default_stop_action:         StopAction
        """
        if is_arm:
            self.motor = ev3.MediumMotor(port)
        else:
            self.motor = ev3.LargeMotor(port)
        assert self.motor.connected,\
            ("A wheel motor appears to not be connected.\n"
             + "  Check the A, B and C jacks.  Are the plugs connected securely?")

        self.default_duty_cycle_percent = default_duty_cycle_percent
        self.default_stop_action = default_stop_action
        self.reset_degrees_spun()
        self.reset_degrees_spun()

    def start_spinning(self, duty_cycle_percent=None):
        """
        Starts this Wheel's motor spinning at the given duty_cycle_percent.
          --  100 -> full power, spin clockwise
          -- -100 -> full power, spin counter-clockwise

          :type  duty_cycle_percent:  int
        """
        if duty_cycle_percent is None:
            duty_cycle_percent = self.default_duty_cycle_percent
        self.motor.run_direct(duty_cycle_sp=duty_cycle_percent)

    def stop_spinning(self, stop_action=None):
        """
        Stops this Wheel's motor from spinning, using the given stop_action,
        which must be one of:
          -- StopAction.BRAKE   StopAction.COAST    StopAction.HOLD

          :type  stop_action:  StopAction
        """
        if stop_action is None:
            stop_action = self.default_stop_action
        self.motor.stop(stop_action=stop_action)

    def get_degrees_spun(self):
        return self.motor.position

    def reset_degrees_spun(self, position=0):
        self.motor.position = position


class TouchSensor(object):
    def __init__(self, port):
        """
        Constructs a TouchSensor at the given port,
        where  port  should be one of:
          ev3.INPUT_1    ev3.INPUT_2    ev3.INPUT_3    ev3.INPUT_4
        """
        self.port = port
        self.sensor = ev3.TouchSensor(port)
        assert self.sensor.connected,\
            ("The touch sensor appears to not be connected.\n"
             + "  Check the jack labelled 1.  Is the plug connected securely?")

    def get_value(self):
        """
        Returns 1 if the TouchSensor is currently pressed,
                0 if it is not currently pressed.
        """
        return self.sensor.is_pressed


class Camera(object):
    """ The Pixy camera. """

    def __init__(self, port=ev3.INPUT_2):
        """
        Constructs a Sensor at the given port, where  port  should be one of:
          ev3.INPUT_1    ev3.INPUT_2    ev3.INPUT_3    ev3.INPUT_4
        """
        self.port = port
        self.sensor = ev3.Sensor(port, driver_name="pixy-lego")
        assert self.sensor.connected,\
            ("The camera sensor appears to not be connected.\n"
             + "  Check the jack labelled 2.  Is the plug connected securely?")


class ColorSensor(object):
    """
    A ColorSensor sends red, then green, then blue light, rotating very quickly
    through all three, and measures the amount of light reflected.

    The sensor can thus measure lightness/darkness of whatever surface
    is closest to the sensor, as well as the approximate color of the surface.
    Surfaces that are about 0.1 inch from the sensor provide the best accuracy.
    """

    def __init__(self, port=ev3.INPUT_3):
        """
        Constructs a ColorSensor at the given port,
        where  port  should be one of:
          ev3.INPUT_1    ev3.INPUT_2    ev3.INPUT_3    ev3.INPUT_4
        """
        self.port = port
        self.sensor = ev3.ColorSensor(port)
        assert self.sensor.connected,\
            ("The color sensor appears to not be connected.\n"
             + "  Check the jack labelled 3.  Is the plug connected securely?")

    def get_value(self):
        """
        Returns a 3-tuple (R, G, B) where
          - R/G/B is the amount of Red/Green/Blue light reflected, respectively,
          - each number is in the range from 0 (none reflected) to 1020.
        """
        return self.sensor.raw

    def get_color(self):
        """
        Returns its best guess as to the color of the object upon which it is
        shining R/G/B pulses of light.  The value returned is one of:
          Color.NO_COLOR   Color.BLACK   Color.BLUE    Color.GREEN
          Color.YELLOW     Color.RED     Color.WHITE   Color.BROWN
        """
        return self.sensor.color

    def get_reflected_intensity(self):
        """
        Returns how much light is reflected by the light emitted by the sensor,
        ranging from 0 (no light reflected) to 100 (maximum light reflected).
        """
        return self.sensor.reflected_light_intensity

    def red(self):
        """ Returns the amount of light reflected by a RED light. """
        return self.sensor.red

    def green(self):
        """ Returns the amount of light reflected by a GREEN light. """
        return self.sensor.green

    def blue(self):
        """ Returns the amount of light reflected by a BLUE light. """
        return self.sensor.blue


class InfraredSensor(object):
    def __init__(self, port):
        """
        Constructs an InfraredSensor at the given port,
        where  port  should be one of:
          ev3.INPUT_1    ev3.INPUT_2    ev3.INPUT_3    ev3.INPUT_4
        """
        self.port = port
        self.proximity_sensor = ev3.InfraredSensor(port)

        assert self.proximity_sensor.connected,\
            ("The IR sensor appears to not be connected.\n"
             + "  Check the jack labelled 4.  Is the plug connected securely?")

    def get_distance_to_nearest_object(self):
        return self.proximity_sensor.proximity


class BeaconButtonController(ev3.RemoteControl):
    """ Controls the buttons on the Beacon. """


class BrickButtonSensor(ev3.Button):
    """ Controls the buttons on the Brick. """
