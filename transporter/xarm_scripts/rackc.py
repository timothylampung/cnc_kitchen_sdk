from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackC(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.move_arc_line(*[-156.4, 354.6, 19.2, 180, 0.0, 118], radius=50, wait=True)

            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[181.0, -23.5, -34.2, 0.1, 57.7, 3.6], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-342.4, -6.5, -76.9, -179.9, 0.0, 177.3], radius=50, wait=True)
                self.vacuum_in('ayam', 5000)
                self.x_arm.move_arc_line(*[-342.5, -6.5, 34.7, -179.9, 0.0, 177.3], radius=50, wait=True)
                self.x_arm.move_arc_line(*[-156.4, 354.6, 19.2, 180, 0.0, 118], radius=50, wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_join(angle=[155.3, -17.2, -41.2, 0.1, 58.4, -3.9], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-341.2, 156.1, -73.4, -179.9, 0.0, 159.2], radius=50, wait=True)
                self.suck(9000)
                self.x_arm.move_arc_line(*[-341.2, 156.1, 44.1, -179.9, 0.0, 159.2], radius=50, wait=True)
                self.x_arm.move_arc_line(*[-156.4, 354.6, 19.2, 180, 0.0, 118], radius=50, wait=True)
            else:
                self.x_arm.move_join(angle=[166.1, -25.8, -32.2, 0.1, 58.0, -15.1], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-322.2, 79.4, -66.1, -179.9, 0.0, -178.9], radius=50, wait=True)
                self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                self.x_arm.move_arc_line(*[-322.2, 79.4, 33.7, -179.9, 0.0, -178.9], radius=50, wait=True)
                self.x_arm.move_arc_line(*[-156.4, 354.6, 19.2, 180, 0.0, 118], radius=50, wait=True)

            if self.requester_callback is not None:
                self.requester_callback()
            self.x_arm.set_is_arm_busy(False)

    def get_address(self):
        return 10
