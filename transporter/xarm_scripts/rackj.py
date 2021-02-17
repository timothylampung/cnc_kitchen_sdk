from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackJ(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            super().run()
            if isinstance(self.x_arm, XArmWrapperSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()

                if self.ingredient == 'SOLID':
                    self.x_arm.move_join(angle=[-161.7, 18.9, -84.7, 0.0, 65.8, 2.5], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-534.7, -176.5, -69.0, 180.0, 0.0, -164.3], radius=50, wait=True)
                    self.vacuum_in('ayam', 5000)
                    self.x_arm.move_arc_line(*[-534.7, -176.5, 51.8, 180.0, 0.0, -164.3], radius=50, wait=True)
                elif self.ingredient == 'LIQUID':
                    self.x_arm.move_join(angle=[-182.6, 19.2, -93.0, 0.0, 73.8, -4.9], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-570.1, 25.5, -66.7, 180.0, 0.0, -177.6], radius=50, wait=True)
                    self.suck(9000)
                    self.x_arm.move_arc_line(*[-570.1, 25.5, 100.1, 180.0, 0.0, -177.6], radius=50, wait=True)
                else:
                    self.x_arm.move_join(angle=[-171.2, 5.9, -67.4, 0.0, 61.5, 6.4], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-490.4, -76.1, -69.3, 180.0, 0.0, -177.6], radius=50, wait=True)
                    self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                    self.x_arm.move_arc_line(*[-490.4, -76.1, 52.3, 180.0, 0.0, -177.6], radius=50, wait=True)

                if self.requester_callback is not None:
                    self.requester_callback()
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 6
