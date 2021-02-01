from transporter.arm.base_movement import BaseMotion
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class Movement12(BaseMotion):

    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        if isinstance(self.xArm, XArmWrapperSingleton):
            self.xArm.set_is_arm_busy(True)
            self.xArm.initial_position()
            self.xArm.move_join(angle=[120.3, 18.7, -60.8, -0.1, 42.8, -3.1], radius=-1, wait=True)

            # if self.requester_callback is not None:
            #     self.requester_callback(self)
            self.xArm.set_is_arm_busy(False)

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def get_address(self):
        raise NotImplementedError()


if __name__ == '__main__':
    move = Movement12()
    move.start()