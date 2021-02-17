#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133
from transporter.xarm_scripts.racka import RackA
from transporter.xarm_scripts.rackb import RackB
from transporter.xarm_scripts.rackc import RackC
from transporter.xarm_scripts.rackd import RackD
from transporter.xarm_scripts.racke import RackE
from transporter.xarm_scripts.rackf import RackF
from transporter.xarm_scripts.rackg import RackG
from transporter.xarm_scripts.rackh import RackH
from transporter.xarm_scripts.racki import RackI
from transporter.xarm_scripts.rackj import RackJ
from transporter.xarm_scripts.rackk import RackK
from transporter.xarm_scripts.rackl import RackL

X_ARM_MOTIONS_DIRECTORY = {
    1: {1: RackA(), 2: RackB(), 3: RackC(), 4: RackD(), 5: RackE(), 6: RackF()},
    2: {1: RackG(), 2: RackH(), 3: RackI(), 4: RackJ(), 5: RackK(), 6: RackL()},
}
