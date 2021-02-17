from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackH(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[165.4, 36.7, -110.6, 0.1, 73.9, 31.4], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-619.0, 161.1, -72.6, -179.9, 0.0, 133.9], radius=50, wait=True)
                self.vacuum_in('ayam', 5000)
                self.x_arm.move_arc_line(*[-619.0, 160.6, 45.6, -179.9, 0.1, 134.0], radius=50,
                                         wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_join(angle=[148.3, 41.3, -115.6, 0.1, 74.4, -34.4], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-556.6, 343.3, -67.3, -179.9, 0.0, -177.3], radius=50,
                                         wait=True)
                self.suck(9000)
                self.x_arm.move_arc_line(*[-556.6, 343.3, 30.5, -179.9, 0.0, -177.3], radius=50,
                                         wait=True)
            else:
                self.x_arm.move_join(angle=[154.1, 20.0, -86.7, 0.1, 66.7, -28.7], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-511.4, 248.3, -64.3, -179.9, 0.0, -177.3], radius=50, wait=True)
                self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                self.x_arm.move_arc_line(*[-511.4, 248.3, 54.3, -179.9, 0.0, -177.3], radius=50, wait=True)

            if self.requester_callback is not None:
                self.requester_callback()
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 14
