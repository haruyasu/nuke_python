import nuke
import nukescripts


class FramePanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Go to Frame", "uk.co.thefoundry.FramePanel")
        self.frame = nuke.Int_Knob("frame", "Frame:")
        self.addKnob(self.frame)
        self.frame.setValue(nuke.frame())

    def knobChanged(self, knob):
        if knob == self.frame:
            nuke.frame(self.frame.value())


def testPanel():
    return FramePanel().addToPane()


menu = nuke.menu("Pane")
menu.addCommand("Frame Panel", testPanel)
nukescripts.registerPanel("uk.co.thefoundry.FramePanel", testPanel)
