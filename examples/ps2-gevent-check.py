#!/usr/bin/env python3


from gevent import sleep, spawn
from gevent.socket import create_connection

from tango import DevState
from tango.server import Device, attribute, command, device_property

def connect(host, port):
    sock = create_connection((host, port))
    return sock.makefile('rwb', newline=b'\n', buffering=0)

def write_readline(conn, msg):
    conn.write(msg)
    return conn.readline()


class PowerSupply(Device):

    host = device_property(str, default_value='localhost')
    port = device_property(int, default_value=45000)

    def init_device(self):
        super().init_device()
        self.calibration_task = None
        self.conn = connect(self.host, self.port)

    @attribute(dtype=float)
    def voltage(self):
        return float(write_readline(self.conn, b'VOL?\n'))

    @command
    def calibrate(self):
        if self.calibration_task is not None:
            raise Exception('Calibration already in place')
        self.calibration_task = spawn(self.do_calibration)

    def do_calibration(self):
        self.set_state(DevState.RUNNING)
        try:        
            write_readline(self.conn, b'CALIB 1\n')
            while int(write_readline(self.conn, b'stat?\n')):
                sleep(0.1)
        finally:
            self.set_state(DevState.ON)
            self.calibration_task = None
            

if __name__ == '__main__':
    from tango import GreenMode
    PowerSupply.run_server(green_mode=GreenMode.Gevent)
