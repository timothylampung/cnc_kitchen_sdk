from transporter.arm.base_movement import BaseMotion


class Movement7(BaseMotion):

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def get_address(self):
        raise NotImplementedError()