from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.core.config.config import EndEffectorInstructionReg as EIG
from transporter.arm.xarm_wrapper import XArmWrapperSingleton

class RackE(BaseMovement):

    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            super().run()
            if isinstance(self.x_arm, XArmWrapperSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()

                if self.ingredient == 'SOLID':
                    self.x_arm.move_join(angle=[-135.7, -7.7, -51.1, 0.0, 58.8, 10.7], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-303.5, -296.2, -73.2, 180.0, 0.0, -146.4], radius=50, wait=True)
                    self.vacuum_in('ayam', 5000)
                    self.x_arm.move_arc_line(*[-303.5, -296.2, 48.0, 180.0, 0.0, -146.4], radius=50, wait=True)
                elif self.ingredient == 'LIQUID':
                    self.x_arm.move_join(angle=[-157.6, -15.5, -42.1, 0.0, 57.6, 6.0], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-353.4, -145.8, -75.8, 180.0, 0.0, -163.6], radius=50, wait=True)
                    self.suck(9000)
                    self.x_arm.move_arc_line(*[-353.4, -145.8, 40.1, 180.0, 0.0, -163.6], radius=50, wait=True)
                else:
                    self.x_arm.move_join(angle=[-139.4, -23.3, -39.9, 0.0, 63.2, 24.2], radius=50, wait=False)
                    self.x_arm.move_arc_line(*[-268.2, -212.7, -71.8, 180.0, 0.0, -163.6], radius=50, wait=True)
                    self.vacuum_powder("ayam", EIG.MAX_GRANULAR)
                    self.x_arm.move_arc_line(*[-268.2, -230.0, 67.0, 180.0, 0.0, -163.6], radius=50, wait=True)

                if self.requester_callback is not None:
                    self.requester_callback()
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 2
