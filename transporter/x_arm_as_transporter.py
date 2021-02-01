#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

import threading
from transporter.arm.base_movement import BaseMotion
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class XarmTransporter(threading.Thread):
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, motion: BaseMotion, requester, multiplier, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.motion = motion
        self.requester = requester
        self.multiplier = multiplier
        self.x_arm: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()

    def return_left(self):
        raise NotImplementedError()

    def return_left_2(self):
        raise NotImplementedError()

    def return_right(self):
        raise NotImplementedError()

    def return_right_2(self):
        raise NotImplementedError()

    def return_to_requester(self, movement: BaseMotion):
        if self.LEFT == self.requester:
            if movement.get_address() > 9:
                self.return_left_2()
            else:
                self.return_left()
        elif self.RIGHT == self.requester:
            if movement.get_address() > 9:
                self.return_right()
            else:
                self.return_right_2()

    def run(self):
        self.motion.set_requester(requester_callback=self.return_to_requester)
        while self.x_arm.is_arm_busy():
            pass
        self.motion.start()
