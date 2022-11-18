from cuoo.thingy.component.broker import Broker as BaseBroker


class Broker(BaseBroker):
    from .devices.dummy_device import DummyDevice

    devices = [
        DummyDevice
    ]