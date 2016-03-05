#!/usr/bin/env python
# This program is used to get serve name by port and protocol name.

import socket


def find_service_by_port(protocol_name, port):
    print("protocol name: {}, port: {}, service: {}".format(
        protocol_name, port, socket.getservbyport(port)))

if __name__ == "__main__":
    while True:
        protocol_name = input()
        port = int(input())
        find_service_by_port(protocol_name, port)