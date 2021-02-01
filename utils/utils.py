#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

import json


def obj_to_json_string(obj):
    dumps = json.dumps(obj.__dict__)
    return dumps
