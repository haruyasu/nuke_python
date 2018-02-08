import nuke

def create_read_from_write():
    sel = nuke.selectedNode()

    if sel.Class() == "Write":
        read = nuke.createNode("Read")
        read.setXpos(int(sel["xpos"].getValue()))
        read.setYpos(int(sel["ypos"].getValue() + 50))

        read["file"].setValue(sel["file"].getValue())

        read["first"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["last"].setValue(int(nuke.Root()["last_frame"].getValue()))

        read["origfirst"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["origlast"].setValue(int(nuke.Root()["last_frame"].getValue()))

        read["colorspace"].setValue(int(sel["colorspace"].getValue()))
