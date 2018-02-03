import nuke
from clipboard import clipboardCore

menu = nuke.menu("Nuke")
python = menu.addMenu("Python")
python.addCommand("Clipboard", "clipboardCore.start()")
