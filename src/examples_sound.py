""" Examples of how to make sounds with the EV3. """

import ev3dev.ev3 as ev3  # You need this!
import time


def main():
    print("Beeping:")
    ev3.Sound.beep().wait()

    time.sleep(1)
    print("Speaking:")
    ev3.Sound.speak("How are you?").wait()  # Must be a SHORT phrase

    time.sleep(1)
    print("Playing a note:")
    ev3.Sound.tone(440, 1500)  # Frequency 440 Hz, for 1.5 seconds

    # time.sleep(1)
    # print("Playing several notes:")
    # ev3.Sound.tone([
    #     (440, 500, 500),  # 440 Hz for 0.5 seconds, then 0.5 seconds rest
    #     (880, 200, 0)  # 880 Hz for 0.2 seconds, no rest (straight to next note)
    #     (385, 1.75, 300)  # 385 Hz for 1.75 seconds, 0.3 seconds rest
    # ]).wait()

    time.sleep(1)
    print("Changing the volume:")
    ev3.Sound.set_volume(25)  # 25% volume
    ev3.Sound.speak("Say it a little quieter now...").wait()

    time.sleep(1)
    ev3.Sound.set_volume(100)  # Full volume
    ev3.Sound.speak("Say it a little LOUDER now").wait()
    ev3.Sound.speak("You know you make me wanna (Shout!)").wait()

    # time.sleep(3)
    # print("Playing a song:")
    # ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav").wait()


main()