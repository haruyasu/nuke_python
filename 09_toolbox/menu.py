import nuke
import toolbox

menu = nuke.menu("Nuke")
python = menu.addMenu("Python")
python.addCommand("Hotbox", "toolbox.start()", "n")
