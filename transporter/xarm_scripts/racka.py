from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton


class RackA(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[140.7, 4.8, -70.1, 0.0, 65.3, -9.8], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-384.0, 314.1, -82.6, -180.0, 0.1, 150.5], radius=50, wait=True)
                self.vacuum_in('ayam', 5000)
                self.x_arm.move_arc_line(*[-384.3, 314.6, 76.3, 180.0, 0.0, 150.5], radius=50, wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_syringe(0)
                self.x_arm.move_join(angle=[123.7, 15.0, -89.0, 0.0, 74.1, 5.6], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-306.2, 458.4, -67.1, 180.0, 0.1, 118.1], radius=50, wait=True)
                self.suck(9000)
                self.x_arm.move_arc_line(*[-306.2, 458.4, 110.7, 180.0, 0.1, 118.1], radius=50, wait=True)
            else:
                self.x_arm.move_join(angle=[129.9, -1.5, -53.1, 0.0, 54.8, -1.6], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-286.0, 341.6, -76.3, -180.0, 0.1, 131.5], radius=50, wait=True)
                self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                self.x_arm.move_arc_line(*[-286.0, 341.6, 20.7, 180.0, 0.1, 131.5], radius=50,
                                         wait=True)

            if self.requester_callback is not None:
                print('running callbacks')
                self.requester_callback()
            self.x_arm.set_is_arm_busy(False)

    def get_address(self):
        return 12
