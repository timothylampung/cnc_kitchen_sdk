from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackD(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.move_join(angle=[168.5, 13.2, -52.6, 0.8, 40, 44.4], radius=-1, wait=True)
            self.vacuum_in('ayam', 5000)
            if self.requester_callback is not None:
                self.requester_callback()
            self.x_arm.set_is_arm_busy(False)

    def get_address(self):
        return 3
