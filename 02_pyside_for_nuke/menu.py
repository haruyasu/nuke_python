import nuke
import my_panel

menu = nuke.menu("Nuke")
test = menu.addMenu("Test")
test.addCommand("My test panel", "my_panel.start()")
