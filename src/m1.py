import rosebotics as rb
from ev3dev import ev3
import time


def main():
    run_test_go_stop()


def run_test_go_stop():
    robot = rb.Snatch3rRobot()

    robot.go(50)
    time.sleep(2)
    robot.stop()


main()