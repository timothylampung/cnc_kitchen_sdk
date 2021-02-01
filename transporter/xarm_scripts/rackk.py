from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackK(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            super().run()
            if isinstance(self.x_arm, XArmSDKSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()

                if self.ingredient.type == Ingredient.SOLID:
                    self.x_arm.move_join(angle=[137.6, -1.8, -33.2, 0.3, 35.7, 13.8], radius=-1, wait=True)
                    self.vacuum_in('ayam', 5000)
                elif self.ingredient.type == Ingredient.LIQUID:
                    self.x_arm.move_join(angle=[154.2, 0.0, -35.4, 0.7, 36.0, -36.0], radius=-1, wait=True)
                    self.suck(XArmSDKSingleton.MAX_PULLER)
                else:
                    print('wtf?')
                if self.requester_callback is not None:
                    self.requester_callback(self)
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 5
