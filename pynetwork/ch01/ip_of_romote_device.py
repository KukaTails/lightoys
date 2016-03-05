#!/usr/bin/env python
# This program is used to get IP address by name of remote host.

import socket


def get_romote_machine_ip():
    romote_host_name = "www.bing.com"
    try:
        print("IP address of {} is {}".format(romote_host_name, socket.gethostbyname(romote_host_name)))
    except socket.error:
        print(romote_host_name, socket.error)


if __name__ == "__main__":
    get_romote_machine_ip()