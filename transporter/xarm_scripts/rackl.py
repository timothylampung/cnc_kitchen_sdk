from transporter.arm.xarm_wrapper import XArmWrapperSingleton
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG


class RackL(BaseMovement):

    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[-134.0, 42.2, -122.6, 0.0, 80.4, 11.0], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-456.2, -473.2, -73.3, 180.0, 0.0, -145.0], radius=50,  wait=True)
                self.vacuum_in('ayam', 5000)
                self.x_arm.move_arc_line(*[-456.6, -472.9, 64.1, 180.0, 0.0, -145.0], radius=50, wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_join(angle=[-149.0, 36.7, -118.7, 0.0, 82.0, 21.9], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-547.8, -328.6, -69.0, 180.0, 0.0, -171.0], radius=50, wait=True)
                self.suck(9000)
                self.x_arm.move_arc_line(*[-547.8, -328.6, 95.2, 180.0, 0.0, -171.0], radius=50, wait=True)
            else:
                self.x_arm.move_join(angle=[-135.0, 27.8, -101.1, 0.0, 73.3, 41.9], radius=50, wait=False)
                self.x_arm.move_arc_line(*[-428.8, -428.5, -63.5, 180.0, 0.0, -176.9], radius=50, wait=True)
                self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                self.x_arm.move_arc_line(*[-428.8, -428.5, 72.9, 180.0, 0.0, -176.9], radius=50, wait=True)

            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 4
