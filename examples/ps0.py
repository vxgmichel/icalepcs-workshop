#!/usr/bin/env python3

from time import sleep

from tango.server import Device, attribute, command


class PowerSupply(Device):

    @attribute(dtype=float)
    def voltage(self):
        return 1.23

    @command
    def calibrate(self):
        sleep(0.1)


if __name__ == '__main__':
    PowerSupply.run_server()
