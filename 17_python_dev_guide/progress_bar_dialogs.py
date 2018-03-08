import threading
import time
import nuke


def selfDestruct():
    task = nuke.ProgressTask("Self Destructing")
    task.setMessage("Deleting files")
    for i in xrange(0, 100):
        if task.isCancelled():
            nuke.executeInMainThread(nuke.message, args=("Stop!"))
            break
        task.setProgress(i)
        time.sleep(0.5)


threading.Thread(None, selfDestruct).start()
