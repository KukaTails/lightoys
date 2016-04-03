#!/usr/bin/env python
# This program is used to download data from HTTP server.

import argparse
import http.client

REMOTE_SERVER_HOST = "www.baidu.com"
REMOTE_SERVER_PATH = '/'


class HTTPClient:
    def __init__(self, host):
        self.host = host

    def fetch(self, path):
        http_conn = http.client.HTTPSConnection(self.host)

        # Prepare header
        http_conn.putrequest("GET", path)
        http_conn.putheader("User-Agent", __file__)
        http_conn.putheader("Host", self.host)
        http_conn.endheaders()

        reponse = http_conn.getresponse()
        return reponse.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Client Example")
    parser.add_argument("--host", action="store", dest="host", default=REMOTE_SERVER_HOST)
    parser.add_argument("--path", action="store", dest="path", default=REMOTE_SERVER_PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print(client.fetch(path))