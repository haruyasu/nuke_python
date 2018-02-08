import nuke
import readWrite

nuke.menu("Nuke").addCommand("utilities/create read from write", "readWrite.create_read_from_write()", "alt+j")
