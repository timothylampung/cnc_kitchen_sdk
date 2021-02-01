from transporter.arm.base_movement import BaseMotion


class Movement6(BaseMotion):

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def get_address(self):
        raise NotImplementedError()
