#!/usr/bin/env python

import socket
import code
import threading
import sys

host = "localhost"
port = 49001
buff = 1024

sys.ps1 = "Rhino > "

class SocketWrapper:
    def __init__(self, s):
        self.s = s
    def read(self, len):
        return self.s.recv(len)
    def write(self, str):
        return self.s.send(str)
    def readline(self):
        return self.read(256)

def handler(client, addr):
    try:
        c = SocketWrapper(client)
        sys.stdin = c
        sys.stdout = c
        sys.stderr = c
        code.interact()
    except (SystemExit, KeyboardInterrupt):
        print addr, "closed connection"
        client.shutdown(0)
        client.close()
        return

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)

    print "Waiting for connection... listening on port", port
    client, addr = server.accept()
    print "... connected from:", addr

    thread = threading.Thread(target=handler, args=(client, addr))
    thread.start()

    # Execute after client connects
