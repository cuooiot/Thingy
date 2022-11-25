from app.engine import Engine
from app.broker import Broker
from app.web import Web

engine = Engine()
engine.attach(Broker)
engine.attach(Web)

if __name__ == '__main__':
    engine.ignite()
