#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

import json
import os
from stir_fry.core.config.config import ArduinoConf as Ac
import socket


class UdpSetUp:
    GET_PORT = 8888
    GET_UDP_TIMEOUT = 180


class ArduinoUdp:
    ONLINE = True
    OFFLINE = False

    def __init__(self, ip, port=Ac.UdpSetUp.GET_PORT):
        self.ip = ip
        # if self.ping():
        #     raise Exception(f'Arduino {self.ip} is not connected')
        # else:
        #     print(f'Module {self.ip} is connected successfully')

        self.busy = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(Ac.UdpSetUp.GET_UDP_TIMEOUT)
        self.addr = (ip, port)

    def ping(self):
        hostname = self.ip  # example
        response = os.system("ping -n 1 " + hostname)
        if response == 0:
            print(hostname, 'is down!')
            return self.ONLINE
        else:
            print(hostname, 'is down!')
            return self.OFFLINE

    def recv(self):
        try:
            data, server = self.client_socket.recvfrom(1024)
            loads = json.loads(data.decode('utf-8'))
            self.busy = False
            return loads, server
        except socket.timeout:
            self.busy = False
            raise Exception('Arduino Please check ethernet connections')

    def send(self, message):
        while self.busy:
            pass
        self.busy = True
        self.client_socket.sendto(message.encode(), self.addr)
        return self.recv()
