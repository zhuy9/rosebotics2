"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Bryan Wolfe.
"""
# ------------------------------------------------------------------------------
# Done: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, discuss the "big picture" of laptop-robot
# Done:    communication:
# Done:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# Done:        user presses a button intended to make something happen on the
# Done:        ROBOT, the LAPTOP program sends a message to its MQTT client
# Done:        indicating what it wants the ROBOT to do, and the MQTT client
# Done:        SENDS that message TO a program running on the ROBOT.
# Done:
# Done:      - Another program runs on the ROBOT. It stays in a loop, responding
# Done:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# Done:        It also, in the background, listens for messages TO the ROBOT
# Done:        FROM the program running on the LAPTOP.  When it hears such a
# Done:        message, it calls the method in the DELAGATE object's class
# Done:        that the message indicates, sending arguments per the message.
# Done:
# Done:  Once you understand the "big picture", delete this Done (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 10
# Done:    to use YOUR robot's number instead of 99.
# Done:    Commit and push the change, then other team members Update Project.
# Done:    Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 4. Run this module.
# Done:    Study its code until you understand how the GUI is set up.
# Done:    Then delete this Done.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    client = com.MqttClient()
    client.connect_to_ev3()

    setup_gui(root, client)

    root.mainloop()
    # --------------------------------------------------------------------------
    # Done: 5. Add code above that constructs a   com.MqttClient   that will
    # Done:    be used to send commands to the robot.  Connect it to this ev3.
    # Done:    Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------


def setup_gui(root_window, client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, client)


def handle_go_forward(entry_box, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    client.send_message('go_forward', [speed_string])
    print('Sending the go_forward message with speed', speed_string)
    # --------------------------------------------------------------------------
    # TODO: 6. This function needs the entry box in which the user enters
    # TODO:    the speed at which the robot should move.  Make the 2 changes
    # TODO:    necessary for the entry_box constructed in  setup_gui
    # TODO:    to make its way to this function.  When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 7. For this function to tell the robot what to do, it needs
    # TODO:    the MQTT client constructed in main.  Make the 4 changes
    # TODO:    necessary for that object to make its way to this function.
    # TODO:    When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


main()
