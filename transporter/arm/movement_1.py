from transporter.arm.movement_2 import BaseMotion
from transporter.arm.xarm_wrapper import XArmWrapperSingleton, SingletonException


class Movement1(BaseMotion):

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def get_address(self):
        raise NotImplementedError()
