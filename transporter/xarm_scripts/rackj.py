from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackJ(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            super().run()
            if isinstance(self.x_arm, XArmSDKSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()

                if self.ingredient.type == Ingredient.SOLID:
                    self.x_arm.move_join(angle=[161.6, -18.4, -16.4, 0.8, 35.4, 37.4], radius=-1, wait=True)
                    self.vacuum_in('ayam', 5000)
                elif self.ingredient.type == Ingredient.LIQUID:
                    self.x_arm.move_join(angle=[181.2, -7.0, -27.3, 1.1, 34.7, -9.4], radius=-1, wait=True)
                    self.suck(XArmSDKSingleton.MAX_PULLER)
                else:
                    print('wtf?')

                if self.requester_callback is not None:
                    self.requester_callback(self)
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 6
