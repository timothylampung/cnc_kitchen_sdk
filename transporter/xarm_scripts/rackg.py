from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackG(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient.type == Ingredient.SOLID:
                self.x_arm.move_join(angle=[-132.8, 8.6, -53.4, 0, 44.8, 46.9], radius=-1, wait=True)
                self.vacuum_in('ayam', 5000)
            elif self.ingredient.type == Ingredient.LIQUID:
                self.x_arm.move_join(angle=[-125.8, 39.3, -99.7, 0, 60.4, 53.9], radius=-1, wait=True)
                self.suck(XArmSDKSingleton.MAX_PULLER)
            else:
                print('wtf?')
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 15
