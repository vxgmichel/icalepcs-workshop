#!/usr/bin/env python3

import time
import random
import logging
import gevent.server

DEFAULT_BIND = ''
DEFAULT_PORT = 45000

class Attr:
    def __init__(self, *, initial_value=0.,
                 encode=lambda x: bytes(str(x), 'ascii'),
                 decode=float):
        self.value = initial_value
        self.encode = encode
        self.decode = decode

    def get(self):
        return self.encode(self.value)

    def set(self, value):
        self.value = self.decode(value)


class Calibrate(Attr):

    def set(self, value):
        self.ts = time.time()
        super().set(value)


class State(Attr):
    def __init__(self, calib, *args, **kwargs):
        kwargs['initial_value'] = 0
        kwargs['decode'] = int
        super().__init__(*args, **kwargs)
        self.calib = calib
        calib.ts = 0

    def get(self):
        self.value = 0
        if time.time() - self.calib.ts < 2:
            self.value = 1
        return super().get()


class PSSimulator(gevent.server.StreamServer):

    class Error(Exception):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logging.getLogger(f'simulator.{self.server_port}')
        calib = Calibrate(initial_value=0)
        self.attrs = {
            b'stat': State(calib),
            b'vol': Attr(initial_value=0.1),
            b'curr': Attr(initial_value=0.),
            b'calib': calib,
        }

    def __getitem__(self, name):
        return self.attrs[name].get()

    def __setitem__(self, name, value):
        self.attrs[name].set(value)

    def handle(self, sock, addr):
        log = self.log
        log.info('new connection from %r', addr)
        fileobj = sock.makefile(mode='rb')
        while True:
            request = fileobj.readline()
            if not request:
                log.info('disconnected %r', addr)
                break
            log.info('request %r', request)
            reply = b'ERROR'
            try:
                reply = self.handle_request(request)
            except PSSimulator.Error:
                pass
            except:
                log.exception('Unforseen error')
            gevent.sleep(1e-1)
            sock.sendall(reply + b'\n')
            log.info('replyed %r', reply)
        fileobj.close()

    def handle_request(self, request):
        req_lower = request.strip().lower()
        is_query = b'?' in req_lower
        pars = req_lower.split()
        name = pars[0]
        if is_query:
            name = name[:-1] # take out '?'
        if is_query:
            return self[name]
        self[name] = pars[1]
        return b'OK'


def main(number=1, bind=DEFAULT_BIND, port=DEFAULT_PORT, **kwargs):
    servers = []
    logging.info('starting simulator...')
    for i in range(number):
        address = bind, port+i
        server = PSSimulator(address)
        server.start()
        servers.append(server)
        server.log.info('simulator listenning on %r!', address)
    try:
        while True:
            # gevent.joinall(servers)
            gevent.sleep(1)
    except KeyboardInterrupt:
        logging.info('Ctrl-C pressed. Bailing out!')
        for server in servers:
            server.stop()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=DEFAULT_PORT)
    parser.add_argument('--bind', default=DEFAULT_BIND)
    parser.add_argument('--log-level', default='info')
    parser.add_argument('--number', type=int, default=1)
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level.upper())
    main(**vars(args))
