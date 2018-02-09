import subprocess
import os, sys

def open_foloder(path):
    if sys.platform == "win32":
        os.startfile(path)

    # if sys.platform == "darwin":
    #     subprocess.check_call(["open", path])
    # if sys.platform == "linux2":
    #     subprocess.check_call(["gnome-open", path])
