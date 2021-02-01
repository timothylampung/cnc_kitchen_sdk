#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

class EndEffectorResponseCode:
    MOVE_CYLINDER_SUCCESS = 'move_cylinder'
    MOVE_PULLER_SUCCESS = 'move_puller'
    MOVE_SYRINGE_SUCCESS = 'move_syringe'
    VACUUM_SUCCESS = 'vacuum'


EndEffectorCodeMap = {
    100: {
        'en': {
            'title': 'Arduino Udp Timeout please check the Ethernet cable'
        }
    }
}
