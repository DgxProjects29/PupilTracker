import os
import pickle
import serial
import time


class BluePy:

    def __init__(self):
        self.port = None

    def start(self):

        # Loading the data settings
        parent = os.path.abspath(os.path.join('classes', os.pardir))
        data_settings = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        print(data_settings['blue_com'], data_settings['blue_bauds'])
        self.port = serial.Serial(data_settings['blue_com'], data_settings['blue_bauds'])

        time.sleep(2)

    def is_connected(self):
        return self.port.isOpen()

    def send_neutro_command(self):
        self.port.write(b'1')

    def send_left_command(self):
        self.port.write(b'2')

    def send_right_command(self):
         self.port.write(b'3')

    def send_blink_command(self):
         self.port.write(b'0')

    def send_turn_off_command(self):
        self.port.write(b'4')

    def close(self):
        self.port.close()

    # Extra methods

    def reset_buffer(self):
        self.port.flushInput()

    def reset_oput_buffer(self):
        self.port.flushOutput()
