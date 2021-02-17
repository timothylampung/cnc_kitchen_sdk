from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackI(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            super().run()
            if isinstance(self.x_arm, XArmWrapperSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()

                if self.ingredient == 'SOLID':
                    self.x_arm.move_join(angle=[-177.3, -19.7, -22.6, 0, 42.3, 2.4], radius=-1, wait=True)
                    self.vacuum_in('ayam', 5000)
                elif self.ingredient == 'LIQUID':
                    self.x_arm.move_join(angle=[-155.7, -2.0, -40.2, 0.0, 42.2, 24.0], radius=-1, wait=True)
                    self.suck(EIG.MAX_GRANULAR)
                else:
                    print('wtf?')

                if self.requester_callback is not None:
                    self.requester_callback(self)
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 13
