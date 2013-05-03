# RhiPyL
## Rhino Python Loop (REPL) ##

### Install/usage

    > cd ~/wherever/you/keep/scripts
    > git clone https://github.com/ianclarksmith/RhiPyL.git
    > open -a "Rhinoceros"

Enter RunPythonScript into the Rhino command bar, open server.py, then hit OK to run the server or cancel to abort. Then back to your shell...

    > nc localhost 49001

That's it! You should receive a prompt to get going right away. When you're done, exit the server with `sys.exit()`.

### Notes

After you hit OK to run the server, Rhino will freeze until you connect. Once you're connected though it should go back to normal and let you work as usual *while* connected from the shell– so you can walk around, create objects, etc. in whatever combination you want to!

Lastly, it should go without saying that you should always save and backup your work. Do not run *any* scripts, including this one, on critical data which you do not have backed up!

---
Rhino OSX™ is a registered trademark of Robert McNeel & Associates.