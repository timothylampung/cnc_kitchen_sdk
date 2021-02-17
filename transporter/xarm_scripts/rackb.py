from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackB(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            self.x_arm.move_join(angle=[-156.4, 22.5, -73.1, 0, 50.6, 23.3], radius=-1, wait=True)
            self.vacuum_in('ayam', 5000)
            if self.requester_callback is not None:
                self.requester_callback()
            self.x_arm.set_is_arm_busy(False)

    def get_address(self):
        return 11
