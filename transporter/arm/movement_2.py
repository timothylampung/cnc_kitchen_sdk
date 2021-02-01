from transporter.arm.base_movement import BaseMotion
from transporter.arm.xarm_wrapper import XArmWrapperSingleton, SingletonException


class Movement2(BaseMotion):

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def get_address(self):
        raise NotImplementedError()
