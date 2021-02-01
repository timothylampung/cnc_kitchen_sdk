#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

from transporter.arm.base_movement import BaseMotion

MOTION_MAPPING = {
    0: {0: BaseMotion(), 1: BaseMotion(), 2: BaseMotion(), 3: BaseMotion()},
    1: {0: BaseMotion(), 1: BaseMotion(), 2: BaseMotion(), 3: BaseMotion()}
}
