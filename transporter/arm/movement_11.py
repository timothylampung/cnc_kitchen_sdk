from transporter.arm.base_movement import BaseMotion
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class Movement11(BaseMotion):

    def __init__(self):
        super().__init__()

        def start(self):
            super().start()
            if isinstance(self.xArm, XArmWrapperSingleton):
                self.xArm.set_is_arm_busy(True)
                self.xArm.initial_position()
                self.xArm.move_join(angle=[152.5, 27.1, -73.7, 0.5, 47.2, 28.7], radius=-1, wait=True)

                # if self.requester_callback is not None:
                #     self.requester_callback(self)
                self.xArm.set_is_arm_busy(False)

        def get_eta(self):
            """in seconds"""
            raise NotImplementedError()

        def get_address(self):
            raise NotImplementedError()


if __name__ == '__main__':
    move = Movement11()
    move.start()
