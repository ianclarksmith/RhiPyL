# RhiPyL
## Rhino Python Loop (REPL) ##

---

Something something about jamming rhinoceri and pythons through sockets so that one might yell commands from a netcat...

At the moment this is just a server script which you can run by entering **RunPythonScript** in your Rhino command bar. It is hardcoded to port 49001 because I know nothing about sockets and heard that that particular port was more in my league.

The Rhino interface will start playing with the beachball until you initiate a client. Netcat or something similar should do the trick.

    nc localhost 49001

The original goal was to make it easier to test out a script I was working on from emacs, but since I know nothing about emacs and have barely even used python before, this is what happened.

### Caveats

- It may not exit like you'd expect. Apparently getting IronPython to play nice with a simple `exit()` or `sys.exit()` is not the easiest thing in the world, and so until further notice the best way to shut it down is to:

        import sys
        sys.exit()
...and then you can `Ctrl-D` out of your shell since it's not going to give you a prompt again anyway.
- Assuming you've done that, you *may* have to actually quit and relaunch Rhino before opening a new session in order to connect to the socket.
- You may notice that the socket is running in a new thread. That's because before, I was having all sorts of problems getting Rhino to respond (beachballin'). Maybe it's not necessary.

### Todo
- client.py
- Learn python
- Fix caveats

---

Rhino OSX™ is a registered trademark of Robert McNeel & Associates.