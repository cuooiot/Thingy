import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer

from cuoo.thingy.component.device import Device
from cuoo.thingy.component.sensor import Sensor


class DummySensor(Sensor):
    async def create(self):
        self.broker.ready()
        device: 'DummyDevice' = self.context.device

        while True:
            device.server.handle_request()
            await asyncio.sleep(0)

        print('Sensor ready')

    def tick(self):
        pass


class DummyDevice(Device):
    sensors = [
        DummySensor
    ]

    async def create(self):
        device: 'Device' = self

        class _(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                device.context.store['a'] = self.path[2:]
                self.wfile.write(b'Updated to \'' + bytes(device.context.store['a'], 'utf-8') + b'\'')

        self.server = HTTPServer(('0.0.0.0', 8081), _)
        self.server.timeout = 0
        self.server.server_activate()

        self.broker.ready()

        print('Device ready')

    def tick(self):
        pass

    def destroy(self):
        print('Device stoped')
