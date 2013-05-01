#!/usr/bin/env python

import sys
import socket
import threading
import rhinoscriptsyntax as rs
import atexit
from code import InteractiveConsole

host = "localhost"
port = 49001 # Any non-reserved port will do

startup_commands = ["import sys", "import rhinoscriptsyntax as rs"]

class Console(InteractiveConsole):
    def __init__(self, file, inv=None):
        InteractiveConsole.__init__(self)
        self.file = sys.stdout = file
        self.cmds = inv
        self.ps1 = ">>> "
        self.ps2 = "... "
        self.banner = ("---------------------------------------------\n" +
                       "RhiPyL - The Rhino-Python-Loop for Rhino OS X\n" +
                       "---------------------------------------------\n\n" +
                       "     [ Python %s on %s ]\n\n" %
                       (sys.version, sys.platform))
        self.resetbuffer()

    def write(self, data):
        self.file.write(data)
        self.file.flush()

    def raw_input(self, prompt=""):
        self.write(prompt)
        return self.file.readline()

    def interact(self, banner=None):
        self.write(self.banner)
        for cmd in self.cmds:
            self.write(self.ps1 + cmd + "\n")
            self.push(cmd)
        multiline = 0
        while 1:
            try:
                if multiline:
                    prompt = self.ps2
                else:
                    prompt = self.ps1
                try:
                    line = self.raw_input(prompt)
                except EOFError:
                    self.write("\n")
                    break
                else:
                    more = self.push(line)
            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer
                more = 0

def handler(client, addr):
    try:
        file = client.makefile()
        console = Console(file, startup_commands)
        console.interact()
    except:
        pass

    client.shutdown(socket.SHUT_RDWR)
    client.close()
    return

def shutdown_server():
    print "Closed connection"
    server.close()

def start_server():
    server.bind((host, port))
    server.listen(1)

    print "Listening on port", port
    client, addr = server.accept()
    print "... connected from:", addr

    # Keeps Rhino from going to the beach
    thread = threading.Thread(target=handler, args=(client, addr))
    thread.start()

    shutdown = atexit.register(shutdown_server())

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    dialog = rs.MessageBox("Host: " + host + "\nPort: " + str(port),
                           buttons=65, title="Launch REPL server")
    if dialog == 1:
        start_server()
    else:
        print "Connection aborted"
