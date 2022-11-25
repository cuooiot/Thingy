from cuoo.thingy.web import Web as BaseWeb

class Web(BaseWeb):
    controllers = BaseWeb.controllers + [
    ]