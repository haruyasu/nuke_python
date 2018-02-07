import nuke
import os
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtMultimedia import *

# renderFinished settings
show_notification = True
play_sound = True
# sound_file = "{}/finish.mp3".format(os.path.dirname(__file__))
sound_file = "F:/nuke_python/11_render_finished/finish.mp3"

def notify_user():
    if play_sound:
        pass
        # QSound.play(sound_file)

    if show_notification:
        nuke.message("Finished Rendering!!")
