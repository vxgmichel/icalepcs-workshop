import random
from time import sleep
from tango.server import Device, attribute, command

class PowerSupply(Device):

    @attribute(dtype=float)
    def voltage(self):
        return 1.23

    @command
    def calibrate(self):
        sleep(0.1)

    @attribute(
        dtype=float,
        polling_period=500,  # ms
        rel_change=1e-3)
    def random(self):
        return random.random()


if __name__ == '__main__':
    PowerSupply.run_server()
