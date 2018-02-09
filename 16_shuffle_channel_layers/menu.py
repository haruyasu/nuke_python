import nuke
import shuffleChannelLayers

nuke.menu("Nuke").addCommand("utilities/shuffleChannelLayers/shuffle channel layers", "shuffleChannelLayers.shuffleChannelLayers()", "Ctrl+Shift+^")
