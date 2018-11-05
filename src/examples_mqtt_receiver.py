""" A simple example of using MQTT for RECEIVING messages. """

import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):

    def say_it(self, message):
        print("Message received!", message)


def main():
    name1 = input("Enter one name: ")
    name2 = input("Enter another name: ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
