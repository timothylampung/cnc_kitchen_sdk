from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackL(BaseMovement):

    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient.type == Ingredient.SOLID:
                self.x_arm.move_join(angle=[120.3, 18.7, -60.8, -0.1, 42.8, -3.1], radius=-1, wait=True)
                self.vacuum_in('ayam', 5000)
            elif self.ingredient.type == Ingredient.LIQUID:
                self.x_arm.move_join(angle=[140.9, 28.3, -83.7, 0.2, 56.1, 17.3], radius=-1, wait=True)
                self.suck(XArmSDKSingleton.MAX_PULLER)
            else:
                print('wtf?')
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 4
