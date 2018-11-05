
class InfraredAsBeaconSensor(object):
    """
    A class for the infrared sensor when it is in the mode in which it
    measures the heading and distance to the Beacon when the Beacon is emitting
    its signal continuously ("beacon mode") on one of its 4 channels (1 to 4).
    Primary authors:  The ev3dev authors, David Mutchler, Dave Fisher,
    their colleagues, and the entire team.
    """

    def __init__(self, channel=1):
        self.channel = channel
        self._underlying_ir_sensor = ev3.BeaconSeeker(channel=channel)

    def set_channel(self, channel):
        """
        Makes this sensor look for signals on the given channel. The physical
        Beacon has a switch that can set the channel to 1, 2, 3 or 4.
        """
        self.channel = channel
        self._underlying_ir_sensor = ev3.BeaconSeeker(channel=channel)

    def get_channel(self):
        return self.channel

    def get_heading_and_distance_to_beacon(self):
        """
        Returns a 2-tuple containing the heading and distance to the Beacon.
        Looks for signals at the frequency of the given channel,
        or at the InfraredAsBeaconSensor's channel if channel is None.
         - The heading is in degrees in the range -25 to 25 with:
             - 0 means straight ahead
             - negative degrees mean the Beacon is to the left
             - positive degrees mean the Beacon is to the right
         - Distance is from 0 to 100, where 100 is about 70 cm
         - -128 means the Beacon is not detected.
        """
        return self._underlying_ir_sensor.heading_and_distance

    def get_heading_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._underlying_ir_sensor.heading

    def get_distance_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._underlying_ir_sensor.distance


class InfraredAsBeaconButtonSensor(object):
    """
    A class for the infrared sensor when it is in the mode in which it
    measures which (if any) of the Beacon buttons are being pressed.
    Primary authors:  The ev3dev authors, David Mutchler, Dave Fisher,
    their colleagues, the entire team, and PUT_YOUR_NAME_HERE.
    """
    # TODO: In the above line, put the name of the primary author of this class.

    def __init__(self, channel=1):
        self.channel = channel
        self._underlying_ir_sensor = ev3.RemoteControl(channel=channel)
        self.button_names = {
            "red_up": TOP_RED_BUTTON,
            "red_down": BOTTOM_RED_BUTTON,
            "blue_up": TOP_BLUE_BUTTON,
            "blue_down": BOTTOM_BLUE_BUTTON,
            "beacon": BEACON_BUTTON
        }


    def set_channel(self, channel):
        """
        Makes this sensor look for signals on the given channel. The physical
        Beacon has a switch that can set the channel to 1, 2, 3 or 4.
        """
        self.channel = channel
        self._underlying_ir_sensor = ev3.RemoteControl(channel=channel)

    def get_channel(self):
        return self.channel

    # def get_buttons_pressed(self):
    #     """
    #     Returns a list of the numbers corresponding to buttons on the Beacon
    #     which are currently pressed.
    #     """
    #     button_list = self._underlying_ir_sensor.buttons_pressed
    #     for k in range(len(button_list)):
    #         button_list[k] = self.button_names[button_list[k]]

    def is_top_red_button_pressed(self):
        return self._underlying_ir_sensor.red_up

    def is_bottom_red_button_pressed(self):
        return self._underlying_ir_sensor.red_down

    def is_top_blue_button_pressed(self):
        return self._underlying_ir_sensor.blue_up

    def is_bottom_blue_button_pressed(self):
        return self._underlying_ir_sensor.blue_down
