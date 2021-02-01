#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133
import queue
import threading


class RecipeWorker(threading.Thread):
    def __init__(self, q: queue.Queue, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)
        q.qsize()

    def run(self):
        pass
